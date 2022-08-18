def main():
    print('Welcome to Movements')
    testSets = [movementSet(135, 10, 'Warm Up'), movementSet(155,10,'Warm Up'), movementSet(185, 8 ,'Working', 3)]

    print(*[aset for aset in testSets],sep=', ')
    testMovement = movement('Barbell Squats', testSets)
    print(testMovement)

class movement():
    def __init__(self, name, movementSets):
        self.name = name
        self.movementSets = movementSets
    def __str__(self) -> str:
        return f'{self.name}: ' + str([f'{aset}' for aset in self.movementSets])
        
class movementSet():
    def __init__(self, weight, repCount, setType, repeatSet = 1) -> None:
        self.weight = weight
        self.repCount = repCount
        self.setType = setType
        self.repeatSet = repeatSet


    def __str__(self) -> str:
        return f'{self.repeatSet} x {self.repCount} @ {self.weight} - {self.setType} Set'

main()