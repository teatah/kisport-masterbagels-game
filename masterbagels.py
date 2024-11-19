import random

class Game:
    def __init__(self):
        self.T = {} # rand num
        self.S = 0 # num of total tries
        self.I = 0 # num of cur tries
        self.N = 0 # num of games

    def start(self):
        print("\t\t\tMASTERBAGELS")
        print("\t\tCREATIVE COMPUTING")
        print("\t\tMORRISTOWN, NEW JERSEY")

        S = input("TEACH? ").strip()
        if S != "N":
            print("  HI, THIS IS A LOGIC GAME DESIGNED TO TEST YOUR DEDUCTIVE")
            print("ABILITY.  I WILL CHOOSE A RANDOM NUMBER AND YOU ISOLATE IT.")
            print("WHEN PROMPTED, ENTER A VALID NUMBER, AND I WILL THEN RESPOND")
            print("WITH THE # OF DIGITS THAT ARE RIGHT AND IN THE RIGHT POSITION")
            print("AND THE # RIGHT BUT IN THE WRONG POSITION.  IF I THINK YOU")
            print("ARE HOPELESSLY LOST, I WILL TELL YOU THE ANSWER AND WE")
            print("WILL GO ON TO THE NEXT NUMBER.  TO RECAP YOUR ENTRIES")
            print("ENTER A 0, TO QUIT ON A NUMBER ENTER 1, AND TO STOP ENTER 2")
        self.start_game()


    def start_game(self):
        illegal_range = False
        while True:
            if illegal_range:
                first_input_text = "?? "
            else:
                first_input_text = "HOW MANY #'S(1-100), # DIGITS(2-6), AND MAX VALUE(2-9): "
                print()

            J = get_valid_input(first_input_text)
            A = get_valid_input("?? ")
            B = get_valid_input("?? ")

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
                H = [(0, 0, 0)]
                self.S = 0
                self.I = 0
                while self.I < A + B + 1:
                    V = int(input("GUESS: "))
                    if V == 0:
                        for x in H:
                            print(f"{x[0]},{x[1]}={x[2]}")
                        continue
                    elif V == 1:
                        self.I = A - 1 + B + 1
                        self.show_result(True)
                        break
                    elif V == 2:
                        return

                    M = [int(d) for d in str(V).zfill(A)]

                    if any(m < 1 or m > B for m in M):
                        print(f"BAD NUMBER IN {V}")
                        continue

                    self.I += 1

                    F1 = sum(1 for x in range(A) if M[x] == self.T[x])
                    F2 = sum(1 for x in range(A) for y in range(A) if M[x] == self.T[y] and x != y and M[x] != self.T[x])

                    print(f"{F1},{F2}")
                    H.append((F1, F2, V))

                    if F1 == A:
                        self.show_result(False)
                        break
                    elif F1 != A and self.I == A + B:
                        self.show_result(True)
            S = input("RUN AGAIN? ").strip().upper()
            if S != "Y":
                break


    def show_result(self, is_fault):
        if is_fault:
            print(f"ANSWER IS {''.join(map(str, self.T))}")
        self.S += self.I
        average = self.S / self.N
        if average.is_integer():
            average = int(average)

        print(f"{self.I} TRIES, {average} AVERAGE FOR {self.N} NUMBERS")


def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input and user_input[0].isdigit():
            return int(user_input[0])  # Возвращаем первый символ, если он цифра
        print('!NUMBER EXPECTED - RETRY INPUT LINE')


if __name__ == "__main__":
    game = Game()
    game.start()
