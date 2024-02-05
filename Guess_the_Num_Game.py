import sys
import random

def queAndAns(randomNum):
    counter = 2
    for i in range(counter):
        print("limit number of times: " + str(counter - i))
        sys.stdout.buffer.write(b'type guess number:')
        sys.stdout.flush()
        guessNum = int(sys.stdin.buffer.readline())
        if randomNum == guessNum:
            return True;

    return False

def main():
    sys.stdout.buffer.write(b'mix number:')
    sys.stdout.flush()
    minNum = int(sys.stdin.readline())

    sys.stdout.buffer.write(b'max number:')
    sys.stdout.flush()
    maxNum = int(sys.stdin.readline())

    if minNum > maxNum:
        print("max number must have a higher value than min number")
        return

    randNum = random.randint(minNum, maxNum)

    if queAndAns(randNum):
        print("number is " + str(randNum) + ". you won!")
    else:
        print("you died.")


main()