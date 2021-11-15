from daycare import daycare
from common import inputString

def main():
    care = daycare("Test Care")
    care.do("help")

    while True:
        if care.do(input(inputString())) == 0:
            print("Pigeon Breeder Ended")
            break

main()
