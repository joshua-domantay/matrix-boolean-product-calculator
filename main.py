# Joshua Anthony Domantay
# Matrix Boolean Product Calculator
# 27 February 2021

rowsA = input("Matrix A, number of rows: ")
colsA = input("Matrix A, number of columns: ")
rowsB = input("Matrix B, number of rows: ")
colsB = input("Matrix B, number of columns: ")

print()
if(not rowsA.isdigit() or not colsA.isdigit() or not rowsB.isdigit() or not colsB.isdigit()):
    print("ERROR: At least one input is not a digit.")
elif(colsA != rowsB):
    print("ERROR: The number of rows from Matrix A is not equal to the number of columns in Matrix B.")
else:
    pass