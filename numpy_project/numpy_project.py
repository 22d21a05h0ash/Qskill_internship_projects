import numpy as np

def inp_mat(prompt):
    print(prompt)
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of cols: "))

    print("Enter the values row by row:")
    matrix = []

    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))

        if len(row) != cols:
            print("Columns mismatch!")
            return None

        matrix.append(row)

    return np.array(matrix)


def operation():

    while True:

        print("\n---- MATRIX OPERATIONS ----")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Exit")

        choice = input("Choose (1-6): ")

        if choice == "6":
            print("Thank You!")
            break


        # Addition
        if choice == "1":
            mat1 = inp_mat("Matrix 1:")
            mat2 = inp_mat("Matrix 2:")

            if mat1.shape == mat2.shape:
                print("Result:\n", mat1 + mat2)
            else:
                print("Same dimensions required!")


        # Subtraction
        elif choice == "2":
            mat1 = inp_mat("Matrix 1:")
            mat2 = inp_mat("Matrix 2:")

            if mat1.shape == mat2.shape:
                print("Result:\n", mat1 - mat2)
            else:
                print("Same dimensions required!")


        # Multiplication
        elif choice == "3":
            mat1 = inp_mat("Matrix 1:")
            mat2 = inp_mat("Matrix 2:")

            if mat1.shape[1] == mat2.shape[0]:
                print("Result:\n", np.dot(mat1, mat2))
            else:
                print("Invalid size for multiplication!")


        # Transpose
        elif choice == "4":
            mat = inp_mat("Matrix:")

            print("Transpose:\n", mat.T)


        # Determinant
        elif choice == "5":
            mat = inp_mat("Matrix:")

            if mat.shape[0] == mat.shape[1]:
                print("Determinant:", np.linalg.det(mat))
            else:
                print("Only square matrix allowed!")


        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    operation()
