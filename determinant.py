import numpy as np

def calc_determinant(matrix):
    return np.linalg.det(matrix)

if __name__ == "__main__":
    n = int(input("Введите размер квадратной матрицы: "))
    matrix = [list(map(int, input(f"Строка {i+1}: ").split())) for i in range(n)]
    det = calc_determinant(matrix)
    print(f"Определитель матрицы: {det}")