from daycare import daycare
from common import inputString

def main():
    care = daycare("Test Care")
    care.do("help")

    while True:
        try:
            if care.do(input(inputString())) == 0:
                break
        except EOFError:
                print("\n")
                break

main()
