def main():
    lines = open("input/test.in", "r").read().strip().split("\n")
    constraints = lines[0].split(" ")
    rows = int(constraints[0])
    columns = int(constraints[1])
    minimumNumberOfEachIngredient = int(constraints[2])
    minimumNumberOfCellsPerSlice = minimumNumberOfEachIngredient * 2
    maximumCellsPerSlice = int(constraints[3])
    
    print("Rows: " + str(rows)
    + "\nColumns " + str(columns)
    + "\nmin ingridients per slice: " + str(minimumNumberOfEachIngredient)
    + "\nmin cells per slice: " + str(minimumNumberOfCellsPerSlice)
    + "\nmax cells per slice: " + str(maximumCellsPerSlice))

    pizza = []
    
    lines.pop(0)
    for line in lines:
        pizza.append(list(line))
    
    for row in pizza:
        print(row)

    possibleSlices = getPossibleSlices(minimumNumberOfCellsPerSlice, maximumCellsPerSlice)

    for size in possibleSlices:
        pr = str(size)
        for possibleSlice in possibleSlices[size]:
            pr = pr + " " + str(possibleSlice)
        print(pr)

def getPossibleSlices(minimumNumberOfCellsPerSlice, maximumCellsPerSlice):
    possibleSlices = {}
    for sliceSize in range(minimumNumberOfCellsPerSlice, maximumCellsPerSlice + 1):
        possibleSlices[sliceSize] = []
        factors = getFactors(sliceSize)
        numberOfFactors = len(factors)
        for i in range(numberOfFactors // 2):
            possibleSlices[sliceSize].append(PizzaSlice(factors[i], factors[-1-i]))
            possibleSlices[sliceSize].append(PizzaSlice(factors[-1-i], factors[i]))

        if(numberOfFactors % 2 != 0):
            centerFactor = round(numberOfFactors / 2) - 1
            possibleSlices[sliceSize].append(PizzaSlice(factors[centerFactor], factors[centerFactor]))
        
        print(factors)
    return possibleSlices

def getFactors(x):
   # This function takes a number and prints the factors
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    return factors

class PizzaSlice:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def __str__(self):
        return str(self.rows) + "x" + str(self.columns)

if __name__ == "__main__":
    main()