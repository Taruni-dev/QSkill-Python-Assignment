import numpy as np

def input_matrix(rows, cols):
    matrix = []
    print(f"Enter elements for {rows}x{cols} matrix:")
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return np.array(matrix)

print("Matrix Operations Tool")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Transpose")
print("5. Determinant")

choice = int(input("Enter your choice (1-5): "))

if choice in [1, 2, 3]:
    r1 = int(input("Enter rows of first matrix: "))
    c1 = int(input("Enter columns of first matrix: "))
    r2 = int(input("Enter rows of second matrix: "))
    c2 = int(input("Enter columns of second matrix: "))

    if choice in [1, 2] and (r1 != r2 or c1 != c2):
        print("Matrices must have same dimensions.")
    elif choice == 3 and c1 != r2:
        print("Invalid dimensions for multiplication.")
    else:
        mat1 = input_matrix(r1, c1)
        mat2 = input_matrix(r2, c2)

        if choice == 1:
            print("Result:\n", mat1 + mat2)
        elif choice == 2:
            print("Result:\n", mat1 - mat2)
        elif choice == 3:
            print("Result:\n", np.dot(mat1, mat2))

elif choice == 4:
    r = int(input("Enter rows: "))
    c = int(input("Enter columns: "))
    mat = input_matrix(r, c)
    print("Transpose:\n", mat.T)

elif choice == 5:
    n = int(input("Enter order of square matrix: "))
    mat = input_matrix(n, n)
    print("Determinant:", np.linalg.det(mat))

else:
    print("Invalid choice")
