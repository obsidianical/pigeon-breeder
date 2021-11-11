from daycare import daycare

def main():
    testCare = daycare("Test")
    testCare.generateRandomCreature()
    testCare.reproduce([testCare.historicCreatures["0"]], 2)
    testCare.breed(testCare.historicCreatures["0"], testCare.historicCreatures["1"])
    print(testCare.creatures)
    
    testCare.death(testCare.historicCreatures["0"])
    print(testCare.creatures)

main()
