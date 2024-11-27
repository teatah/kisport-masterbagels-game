import random

class Game:
    def __init__(self):
        self.T = {} # rand num
        self.S = 0 # num of total tries
        self.I = 0 # num of cur tries
        self.N = 0 # num of games


    async def start(self):
        print(" " * 23 + "MASTERBAGELS")
        print(" " * 20 + "CREATIVE COMPUTING")
        print(" " * 18 + "MORRISTOWN, NEW JERSEY")

        S = await prompt("TEACH? ")
        S = S.strip()
        if S != "N":
            print("  HI, THIS IS A LOGIC GAME DESIGNED TO TEST YOUR DEDUCTIVE")
            print("ABILITY.  I WILL CHOOSE A RANDOM NUMBER AND YOU ISOLATE IT.")
            print("WHEN PROMPTED, ENTER A VALID NUMBER, AND I WILL THEN RESPOND")
            print("WITH THE # OF DIGITS THAT ARE RIGHT AND IN THE RIGHT POSITION")
            print("AND THE # RIGHT BUT IN THE WRONG POSITION.  IF I THINK YOU")
            print("ARE HOPELESSLY LOST, I WILL TELL YOU THE ANSWER AND WE")
            print("WILL GO ON TO THE NEXT NUMBER.  TO RECAP YOUR ENTRIES")
            print("ENTER A 0, TO QUIT ON A NUMBER ENTER 1, AND TO STOP ENTER 2")
        await self.start_game()


    async def start_game(self):
        illegal_range = False
        while True:
            if illegal_range:
                first_input_text = "?? "
            else:
                first_input_text = "HOW MANY #'S(1-100), # DIGITS(2-6), AND MAX VALUE(2-9)? "
                print()

            J = await get_valid_input(first_input_text)
            A = await get_valid_input("?? ")
            B = await get_valid_input("?? ")

            illegal_range = False
            if A <= 0 or A > 6 or B < 2 or B > 9:
                print("ILLEGAL RANGE, RE-ENTER RUN PARAMETERS")
                illegal_range = True
                continue

            if J > 100:
                J = 100

            for N in range(1, J + 1):
                self.N = N
                self.T = [random.randint(1, B) for _ in range(A)]
                H = []
                self.S = 0
                self.I = 0
                guess = "GUESS? "
                while self.I < A + B + 1:
                    V = await get_valid_input(guess)
                    if V == 0:
                        guess = "GUESS? "
                        if len(H) == 0:
                            print(" 0 , 0 = 0 ")
                        else:
                            for x in H:
                                print(f" {x[0]} , {x[1]} = {x[2]} ")
                            continue
                    elif V == 1:
                        self.I = A - 1 + B + 1
                        self.show_result(True)
                        break
                    elif V == 2:
                        return
                    elif not V:
                        guess = "? "
                        continue

                    M = [int(d) for d in str(V).zfill(A)]

                    if any(m < 1 or m > B for m in M):
                        print(f"BAD NUMBER IN {V} ")
                        continue

                    self.I += 1

                    F1 = 0
                    F2 = 0
                    used_values = []
                    for x in range(A):
                        if M[x] == self.T[x]:
                            used_values.append(M[x])
                            F1 += 1
                        else:
                            for y in range(A):
                                if M[x] == self.T[y] and x != y and not M[x] in used_values:
                                    used_values.append(M[x])
                                    F2 += 1
                                    break

                    print(f" {F1} , {F2} ")
                    H.append((F1, F2, V))

                    if F1 == A:
                        self.show_result(False)
                        break
                    elif F1 != A and self.I == A + B:
                        self.show_result(True)
            S = await prompt("RUN AGAIN? ")
            S = S.strip().upper()
            if S != "Y":
                break


    def show_result(self, is_fault):
        if is_fault:
            print(f"ANSWER IS {''.join(map(str, self.T))} ")
        self.S += self.I
        average = self.S / self.N
        if average.is_integer():
            average = int(average)

        print(f" {self.I} TRIES, {average} AVERAGE FOR {self.N} NUMBERS")


async def prompt(text = ''):
    return input(text)


async def get_valid_input(text):
    while True:
        user_input = await prompt(text)
        if user_input and user_input[0].isdigit():
            return int(user_input)
        else:
            print('!NUMBER EXPECTED - RETRY INPUT LINE')
            return ''


async def main():
    game = Game()
    await game.start()
