import subprocess
import asyncio

async def a_process(command):
    return await asyncio.create_subprocess_exec(
        *command.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE
    )


def process(command):
        return subprocess.Popen(
            command.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            shell=True
        )


async def a_expect(proc, pattern):
    pattern = pattern.strip("\n").replace("\n", "\r\n")
    buffer = ""
    while True:
        if buffer and buffer != ' ' and buffer == pattern: #pattern.endswith(buffer):
            return True, buffer

        char = await proc.stdout.read(1)
        buffer += char.decode()
        print(buffer)


def expect(proc, pattern):
    pattern = pattern.strip("\n").replace("\n", "\r\n")
    buffer = ""
    while True:
        if buffer and buffer != ' ' and buffer == pattern: #pattern.endswith(buffer):
            return True, buffer
        char = proc.stdout.read(1).decode()
        buffer += char
        print(buffer)


async def a_write(proc, text):
    proc.stdin.write(f'{text}\n'.encode())
    await proc.stdin.drain()
    return text


def write(proc, text):
    proc.stdin.write(f'{text}\n'.encode())
    proc.stdin.flush()
    return text


async def test():
    print("Launching processes")
    try:
        bas = process('masterbagels_norand.bas')
        py = await a_process('python masterbagels_console_norand.py')

        expected_greetings = '''
                       MASTERBAGELS
                    CREATIVE COMPUTING
                  MORRISTOWN, NEW JERSEY
TEACH?
'''
        print("expecting answers...")
        expect(bas, expected_greetings)
        await a_expect(py, expected_greetings)
        print("[+] TEST 1 - PASSED")

        print("sending keys...")
        write(bas, 'Y')
        await a_write(py, 'Y')
        print("[+] KEYS SENT")
        instruction = '''
   HI, THIS IS A LOGIC GAME DESIGNED TO TEST YOUR DEDUCTIVE
ABILITY.  I WILL CHOOSE A RANDOM NUMBER AND YOU ISOLATE IT.
WHEN PROMPTED, ENTER A VALID NUMBER, AND I WILL THEN RESPOND
WITH THE # OF DIGITS THAT ARE RIGHT AND IN THE RIGHT POSITION
AND THE # RIGHT BUT IN THE WRONG POSITION.  IF I THINK YOU
ARE HOPELESSLY LOST, I WILL TELL YOU THE ANSWER AND WE
WILL GO ON TO THE NEXT NUMBER.  TO RECAP YOUR ENTRIES
ENTER A 0, TO QUIT ON A NUMBER ENTER 1, AND TO STOP ENTER 2

HOW MANY #'S(1-100), # DIGITS(2-6), AND MAX VALUE(2-9)? 
'''
        print("expecting results")
        expect(bas, instruction)
        await a_expect(py, instruction)
        print("[+] TEST 2 - PASSED")

        numbers, digits, max_value = 1, 3, 3
        print("sending keys...")
        write(bas, numbers)
        await a_write(py, numbers)
        print("[+] KEYS SENT")
        print("expecting answers...")
        expect(bas, "?")
        await a_expect(py, "?")
        print("[+] TEST 3 - PASSED")

        print("sending keys...")
        write(bas, digits)
        await a_write(py, digits)
        print("[+] KEYS SENT")
        print("expecting answers...")
        expect(bas, "? ?? ")
        await a_expect(py, "? ?? ")
        print("[+] TEST 4 - PASSED")

        print("sending keys...")
        write(bas, max_value)
        await a_write(py, max_value)
        print("[+] KEYS SENT")
        print("expecting answers...")
        expect(bas, "GUESS? ")
        await a_expect(py, "GUESS? ")
        print("[+] TEST 5 - PASSED")

        guess = '112'
        print("sending keys...")
        write(bas, guess)
        await a_write(py, guess)
        print("[+] KEYS SENT")
        print("expecting answers...")
        expect_value = '''
 1 , 1 
GUESS? 
'''
        expect(bas, expect_value)
        await a_expect(py, expect_value)
        print("[+] TEST 6 - PASSED")

        guess = '213'
        print("sending keys...")
        write(bas, guess)
        await a_write(py, guess)
        print("[+] KEYS SENT")
        print("expecting answers...")
        expect_value = '''
 1 , 2 
GUESS? 
'''
        expect(bas, expect_value)
        await a_expect(py, expect_value)
        print("[+] TEST 7 - PASSED")

        guess = 300
        print("sending keys...")
        write(bas, guess)
        await a_write(py, guess)
        print("[+] KEYS SENT")
        print("expecting answers...")
        expect_value = '''
BAD NUMBER IN 300 
GUESS? 
'''
        expect(bas, expect_value)
        await a_expect(py, expect_value)
        print("[+] TEST 8 - PASSED")

        guess = 0
        print("sending keys...")
        write(bas, guess)
        await a_write(py, guess)
        print("[+] KEYS SENT")
        print("expecting answers...")
        expect_value = '''
 1 , 1 = 112 
 1 , 2 = 213 
GUESS? 
'''
        expect(bas, expect_value)
        await a_expect(py, expect_value)
        print("[+] TEST 9 - PASSED")

        guess = 'g112'
        print("sending keys...")
        write(bas, guess)
        await a_write(py, guess)
        print("[+] KEYS SENT")
        print("expecting answers...")
        expect_value = '''
!NUMBER EXPECTED - RETRY INPUT LINE
? 
'''

        expect(bas, expect_value)
        await a_expect(py, expect_value)
        print("[+] TEST 10 - PASSED")

        guess = 1
        print("sending keys...")
        write(bas, guess)
        await a_write(py, guess)
        print("[+] KEYS SENT")
        print("expecting answers...")
        expect_value = '''
ANSWER IS 123 
 6 TRIES, 6 AVERAGE FOR 1 NUMBERS
RUN AGAIN? 
'''
        expect(bas, expect_value)
        await a_expect(py, expect_value)
        print("[+] TEST 11 - PASSED")

        bas.kill()
        bas.wait()

        py.kill()
        await py.wait()
    except Exception as ex:
        print(ex)


asyncio.run(test())