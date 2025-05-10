
def find_min(matrix):
    min_val = matrix[0][0]
    indices = (0, 0)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
                indices = (i, j)
    return min_val, indices

if __name__ == "__main__":
    n = int(input("Введите количество строк: "))
    m = int(input("Введите количество столбцов: "))
    matrix = [list(map(int, input(f"Строка {i+1}: ").split())) for i in range(n)]
    val, idx = find_min(matrix)
    print(f"Минимальный элемент: {val} на позиции {idx}")