
def diagonal_sums(matrix):
    n = len(matrix)
    main_diag = sum(matrix[i][i] for i in range(n))
    anti_diag = sum(matrix[i][n - i - 1] for i in range(n))
    return main_diag, anti_diag

if __name__ == "__main__":
    n = int(input("Введите размер квадратной матрицы: "))
    matrix = [list(map(int, input(f"Строка {i+1}: ").split())) for i in range(n)]
    main, anti = diagonal_sums(matrix)
    print(f"Сумма главной диагонали: {main}")
    print(f"Сумма побочной диагонали: {anti}")