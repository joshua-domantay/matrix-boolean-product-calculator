# Joshua Anthony Domantay
# Matrix Boolean Product Calculator
# 27 February 2021

def getMatrix(matrixChar, rows, cols):
    matrix = []
    for i in range(rows):
        col = []
        for j in range(cols):
            x = input("Enter matrix " + matrixChar + " row " + str(i) + " column " + str(j) + ": ")
            if(not x.isdigit()):
                print("\nERROR: Input is not a digit.")
                quit()
            col.append(int(x))
        matrix.append(col)
    return matrix

rowsA = input("Matrix A, number of rows: ")
colsA = input("Matrix A, number of columns: ")
rowsB = input("Matrix B, number of rows: ")
colsB = input("Matrix B, number of columns: ")

print()
if(not rowsA.isdigit() or not colsA.isdigit() or not rowsB.isdigit() or not colsB.isdigit()):
    print("ERROR: At least one input is not a digit.")
    quit()
elif(colsA != rowsB):
    print("ERROR: The number of rows from Matrix A is not equal to the number of columns in Matrix B.")
    quit()

# Convert rows and cols to int
rowsA = int(rowsA)
colsA = int(colsA)
rowsB = int(rowsB)
colsB = int(colsB)

print("Matrix A")
matrixA = getMatrix("A", rowsA, colsA)
print("\nMatrix B")
matrixB = getMatrix("B", rowsB, colsB)

matrixC = []
for i in range(rowsA):
    col = []
    for j in range(colsB):
        col.append(0)
    matrixC.append(col)
