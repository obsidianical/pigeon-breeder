from daycare import daycare

def main():
    testCare = daycare("Test")
    testCare.generateRandomCreature()
    testCare.reproduce([testCare.historicCreatures["0"]])

    testCare.breed(testCare.historicCreatures["0"], testCare.historicCreatures["1"])
    print(testCare.historicCreatures)

main()
