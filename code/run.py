from daycare import daycare

def main():
    testCare = daycare("Test")
    testCare.generateRandomCreature()
    testCare.reproduce([testCare.historicCreatures["0"]])
    print(testCare.historicCreatures)

main()
