from daycare import daycare
from common import inputString

def main():
    care = daycare("Test Care")
    care.do("help")
    while True:
        print("\n")
        p = care.do(input(inputString()))
        if p == 0:
            print("Pigeon Breeder Ended")
            break
main()
