import random
import math


# Вариант 1, задание 1 Вычислить сумму и число положительных элементов матрицы A[N,N], находящихся над главной диагональю
def calculate_sum_and_count_positive_above_diagonal():

    N = int(input("Введите размер матрицы N: "))
    A = []
    print("Введите элементы матрицы A:")
    for i in range(N):
        row = []
        for j in range(N):
            row.append(int(input(f"A[{i}][{j}]: ")))
        A.append(row)
    
    print("\nМатрица A:")
    for row in A:
        print(row)
    
    sum_pos = 0
    count_pos = 0
    
    for i in range(N):
        for j in range(N):
            if j > i and A[i][j] > 0:  # Элементы над главной диагональю
                sum_pos += A[i][j]
                count_pos += 1
    
    print(f"\nСумма положительных элементов над главной диагональю: {sum_pos}")
    print(f"Число положительных элементов над главной диагональю: {count_pos}")
    return sum_pos, count_pos


# Вариант 2, задание 1 Определить, является ли квадратная матрица магическим квадратом
def check_magic_square():
    
    n = int(input("Введите порядок матрицы n: "))
    matrix = []
    print("Введите элементы матрицы:")
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input(f"Элемент [{i}][{j}]: ")))
        matrix.append(row)
    
    print("\nМатрица:")
    for row in matrix:
        print(row)
    
    # Вычисляем сумму первой строки для сравнения
    target_sum = sum(matrix[0])
    
    is_magic = True
    
    # Проверяем суммы строк
    for i in range(n):
        if sum(matrix[i]) != target_sum:
            is_magic = False
            break
    
    # Проверяем суммы столбцов
    if is_magic:
        for j in range(n):
            col_sum = sum(matrix[i][j] for i in range(n))
            if col_sum != target_sum:
                is_magic = False
                break
    
    # Проверяем главную диагональ
    if is_magic:
        diag_sum = sum(matrix[i][i] for i in range(n))
        if diag_sum != target_sum:
            is_magic = False
    
    # Проверяем побочную диагональ
    if is_magic:
        anti_diag_sum = sum(matrix[i][n-1-i] for i in range(n))
        if anti_diag_sum != target_sum:
            is_magic = False
    
    if is_magic:
        print(f"Матрица является магическим квадратом (сумма = {target_sum})")
    else:
        print("Матрица НЕ является магическим квадратом")
    return is_magic, target_sum if is_magic else None


# Вариант 3, задание 1 Определить, является ли квадратная матрица симметричной относительно главной диагонали
def check_symmetric_matrix():
    
    n = int(input("Введите порядок матрицы n: "))
    matrix = []
    print("Введите элементы матрицы:")
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input(f"Элемент [{i}][{j}]: ")))
        matrix.append(row)
    
    print("\nМатрица:")
    for row in matrix:
        print(row)
    
    is_symmetric = True
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                is_symmetric = False
                break
        if not is_symmetric:
            break
    
    if is_symmetric:
        print("Матрица симметрична относительно главной диагонали")
    else:
        print("Матрица НЕ симметрична относительно главной диагонали")
    return is_symmetric


# Вариант 4, задание 1 Найти строку с наибольшей и строку с наименьшей суммой элементов
def find_rows_max_min_sum():
    
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    
    matrix = []
    print("Введите элементы матрицы:")
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Элемент [{i}][{j}]: ")))
        matrix.append(row)
    
    print("\nМатрица:")
    for row in matrix:
        print(row)
    
    sums = []
    for i in range(rows):
        row_sum = sum(matrix[i])
        sums.append(row_sum)
        print(f"Строка {i}: сумма = {row_sum}")
    
    max_sum_idx = sums.index(max(sums))
    min_sum_idx = sums.index(min(sums))
    
    print(f"\nСтрока с наибольшей суммой: строка {max_sum_idx}")
    print(f"Элементы: {matrix[max_sum_idx]}, сумма = {sums[max_sum_idx]}")
    print(f"\nСтрока с наименьшей суммой: строка {min_sum_idx}")
    print(f"Элементы: {matrix[min_sum_idx]}, сумма = {sums[min_sum_idx]}")
    return max_sum_idx, min_sum_idx, sums[max_sum_idx], sums[min_sum_idx]


# Вариант 5, задание 1 Упорядочить по возрастанию элементы каждой строки матрицы
def sort_matrix_rows_ascending():
    
    n = int(input("Введите количество строк n: "))
    m = int(input("Введите количество столбцов m: "))
    
    matrix = []
    print("Введите элементы матрицы:")
    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(input(f"Элемент [{i}][{j}]: ")))
        matrix.append(row)
    
    print("\nИсходная матрица:")
    for row in matrix:
        print(row)
    
    # Сортируем каждую строку
    sorted_matrix = []
    for i in range(n):
        sorted_row = sorted(matrix[i])
        sorted_matrix.append(sorted_row)
    
    print("\nМатрица после сортировки строк:")
    for row in sorted_matrix:
        print(row)
    return sorted_matrix


# Вариант 6, задание 1 Найти в каждой строке наибольший элемент и в каждом столбце наименьший
def find_max_in_rows_min_in_columns():
    
    n = int(input("Введите размер квадратной матрицы n: "))
    matrix = []
    print("Введите элементы матрицы:")
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input(f"Элемент [{i}][{j}]: ")))
        matrix.append(row)
    
    print("\nМатрица:")
    for row in matrix:
        print(row)
    
    row_maxs = []
    print("\nНаибольшие элементы в каждой строке:")
    for i in range(n):
        max_in_row = max(matrix[i])
        row_maxs.append(max_in_row)
        print(f"Строка {i}: {max_in_row}")
    
    col_mins = []
    print("\nНаименьшие элементы в каждом столбце:")
    for j in range(n):
        min_in_col = min(matrix[i][j] for i in range(n))
        col_mins.append(min_in_col)
        print(f"Столбец {j}: {min_in_col}")
    return row_maxs, col_mins


# Вариант 7, задание 1 Восстановить симметричную матрицу из верхнего треугольника
def restore_symmetric_matrix_from_triangle():
    
    n = int(input("Введите порядок матрицы n: "))
    
    # Количество элементов в верхнем треугольнике (включая диагональ)
    triangle_size = n * (n + 1) // 2
    
    print(f"Введите {triangle_size} элементов верхнего треугольника (по строкам):")
    triangle = []
    for i in range(triangle_size):
        triangle.append(int(input(f"Элемент {i+1}: ")))
    
    # Восстанавливаем матрицу
    matrix = [[0] * n for _ in range(n)]
    
    idx = 0
    for i in range(n):
        for j in range(i, n):
            matrix[i][j] = triangle[idx]
            matrix[j][i] = triangle[idx]  # Симметричный элемент
            idx += 1
    
    print("\nВосстановленная симметричная матрица:")
    for row in matrix:
        print(row)
    return matrix


# Вариант 8, задание 1 Разделить элементы k-й строки на диагональный элемент этой строки
def divide_row_by_diagonal_element():
    
    n = int(input("Введите порядок матрицы n: "))
    k = int(input(f"Введите номер строки k (0..{n-1}): "))
    
    matrix = []
    print("Введите элементы матрицы:")
    for i in range(n):
        row = []
        for j in range(n):
            row.append(float(input(f"Элемент [{i}][{j}]: ")))
        matrix.append(row)
    
    print("\nИсходная матрица:")
    for row in matrix:
        print(row)
    
    diagonal_element = matrix[k][k]
    
    if diagonal_element != 0:
        original_row = matrix[k].copy()
        for j in range(n):
            matrix[k][j] = matrix[k][j] / diagonal_element
        print(f"\nМатрица после деления строки {k} на диагональный элемент {diagonal_element}:")
        for row in matrix:
            print([f"{x:.2f}" for x in row])
        success = True
    else:
        print(f"\nОшибка: диагональный элемент в строке {k} равен 0, деление невозможно")
        success = False
    
    return matrix if success else None, success, diagonal_element


# Вариант 9, задание 1 Найти число элементов, кратных k, и наибольший из этих элементов
def find_multiples_and_max_multiple():
    
    n = int(input("Введите размер квадратной матрицы n: "))
    k = int(input("Введите число k (делитель): "))
    
    matrix = []
    print("Введите элементы матрицы:")
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input(f"Элемент [{i}][{j}]: ")))
        matrix.append(row)
    
    print("\nМатрица:")
    for row in matrix:
        print(row)
    
    multiples = []
    count = 0
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] % k == 0:
                count += 1
                multiples.append(matrix[i][j])
    
    if count > 0:
        max_multiple = max(multiples)
        print(f"\nКоличество элементов, кратных {k}: {count}")
        print(f"Наибольший из элементов, кратных {k}: {max_multiple}")
        print(f"Все элементы, кратные {k}: {multiples}")
    else:
        print(f"\nНет элементов, кратных {k}")
        max_multiple = None
    
    return count, max_multiple, multiples


# Вариант 10, задание 1 Найти максимальный среди элементов упорядоченных строк
def find_max_in_sorted_rows():
    
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    
    matrix = []
    print("Введите элементы матрицы:")
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Элемент [{i}][{j}]: ")))
        matrix.append(row)
    
    print("\nМатрица:")
    for row in matrix:
        print(row)
    
    max_in_sorted_rows = []
    sorted_row_indices = []
    
    for i in range(rows):
        # Проверяем, упорядочена ли строка по возрастанию
        is_ascending = all(matrix[i][j] <= matrix[i][j+1] for j in range(cols-1))
        
        # Проверяем, упорядочена ли строка по убыванию
        is_descending = all(matrix[i][j] >= matrix[i][j+1] for j in range(cols-1))
        
        if is_ascending or is_descending:
            max_in_sorted_rows.append(max(matrix[i]))
            sorted_row_indices.append(i)
            print(f"Строка {i} упорядочена")
    
    if max_in_sorted_rows:
        result = max(max_in_sorted_rows)
        print(f"\nМаксимальный элемент среди упорядоченных строк: {result}")
    else:
        print("\nНет упорядоченных строк")
        result = None
    
    return result, sorted_row_indices, max_in_sorted_rows


# Вариант 11, задание 1 Найти сумму элементов строки с наименьшим элементом
def sum_of_row_with_min_element():
    
    n = int(input("Введите порядок матрицы n: "))
    
    matrix = []
    print("Введите элементы матрицы:")
    for i in range(n):
        row = []
        for j in range(n):
            row.append(float(input(f"Элемент [{i}][{j}]: ")))
        matrix.append(row)
    
    print("\nМатрица:")
    for row in matrix:
        print(row)
    
    # Находим минимальный элемент и его позицию
    min_value = matrix[0][0]
    min_row = 0
    min_col = 0
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_row = i
                min_col = j
    
    # Сумма элементов строки с минимальным элементом
    row_sum = sum(matrix[min_row])
    
    print(f"\nМинимальный элемент: {min_value} на позиции [{min_row}][{min_col}]")
    print(f"Строка с минимальным элементом: строка {min_row}")
    print(f"Сумма элементов этой строки: {row_sum}")
    print(f"Элементы строки: {matrix[min_row]}")
    return min_value, min_row, min_col, row_sum


# Вариант 12, задание 1 Найти такие k, что k-я строка совпадает с k-м столбцом
def find_matching_row_column_indices():
    
    n = int(input("Введите размер квадратной матрицы n: "))
    
    matrix = []
    print("Введите элементы матрицы:")
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input(f"Элемент [{i}][{j}]: ")))
        matrix.append(row)
    
    print("\nМатрица:")
    for row in matrix:
        print(row)
    
    matching_indices = []
    
    for k in range(n):
        row = matrix[k]
        column = [matrix[i][k] for i in range(n)]
        
        if row == column:
            matching_indices.append(k)
    
    if matching_indices:
        print(f"\nСтрока и столбец совпадают для k = {matching_indices}")
    else:
        print("\nНет таких k, при которых строка совпадает со столбцом")
    return matching_indices


# Вариант 13, задание 1 Определить наименьший элемент каждой четной строки матрицы
def find_min_in_even_rows():
    
    M = int(input("Введите количество строк M: "))
    N = int(input("Введите количество столбцов N: "))
    
    A = []
    print("Введите элементы матрицы A:")
    for i in range(M):
        row = []
        for j in range(N):
            row.append(int(input(f"A[{i}][{j}]: ")))
        A.append(row)
    
    print("\nМатрица A:")
    for row in A:
        print(row)
    
    min_elements = []
    print("\nНаименьшие элементы четных строк:")
    for i in range(0, M, 2):  # Индексация с 0, поэтому четные строки имеют четные индексы
        min_in_row = min(A[i])
        min_elements.append((i, min_in_row))
        print(f"Строка {i}: наименьший элемент = {min_in_row}")
    return min_elements


# Вариант 14, задание 1 Переставить строку с максимальным элементом на главной диагонали со строкой m
def swap_row_with_max_diagonal():
    
    n = int(input("Введите размер квадратной матрицы n: "))
    
    matrix = []
    print("Введите элементы матрицы:")
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input(f"Элемент [{i}][{j}]: ")))
        matrix.append(row)
    
    print("\nИсходная матрица:")
    for row in matrix:
        print(row)
    
    # Находим строку с максимальным элементом на главной диагонали
    max_diag = matrix[0][0]
    max_row = 0
    
    for i in range(n):
        if matrix[i][i] > max_diag:
            max_diag = matrix[i][i]
            max_row = i
    
    print(f"\nМаксимальный элемент на главной диагонали: {max_diag} в строке {max_row}")
    
    m = int(input(f"\nВведите номер строки m для обмена (0..{n-1}): "))
    
    if 0 <= m < n and m != max_row:
        # Меняем строки местами
        matrix[max_row], matrix[m] = matrix[m], matrix[max_row]
        
        print(f"\nМатрица после обмена строк {max_row} и {m}:")
        for row in matrix:
            print(row)
        swapped = True
    else:
        print("\nНеверный номер строки или строки совпадают, обмен не выполнен")
        swapped = False
    
    return matrix, swapped, max_diag, max_row, m


# Вариант 15, задание 1 Определить номера строк, содержащих элемент c, и умножить эти строки на d
def multiply_rows_containing_value():
    
    M = int(input("Введите количество строк M: "))
    N = int(input("Введите количество столбцов N: "))
    
    R = []
    print("Введите элементы матрицы R:")
    for i in range(M):
        row = []
        for j in range(N):
            row.append(int(input(f"R[{i}][{j}]: ")))
        R.append(row)
    
    print("\nМатрица R:")
    for row in R:
        print(row)
    
    c = int(input("\nВведите число c: "))
    d = int(input("Введите число d: "))
    
    rows_with_c = []
    
    # Находим строки, содержащие элемент c
    for i in range(M):
        if c in R[i]:
            rows_with_c.append(i)
    
    if rows_with_c:
        print(f"\nСтроки, содержащие элемент {c}: {rows_with_c}")
        
        # Сохраняем оригинальные значения для отображения
        original_rows = [R[i].copy() for i in rows_with_c]
        
        # Умножаем эти строки на d
        for i in rows_with_c:
            for j in range(N):
                R[i][j] *= d
        
        print(f"\nМатрица после умножения строк на {d}:")
        for row in R:
            print(row)
    else:
        print(f"\nВ матрице нет элемента {c}")
    
    return R, rows_with_c, c, d, original_rows if rows_with_c else None


calculate_sum_and_count_positive_above_diagonal()
check_magic_square()
check_symmetric_matrix()
find_rows_max_min_sum()
sort_matrix_rows_ascending()
find_max_in_rows_min_in_columns()
restore_symmetric_matrix_from_triangle()
divide_row_by_diagonal_element()
find_multiples_and_max_multiple()
find_max_in_sorted_rows()
sum_of_row_with_min_element()
find_matching_row_column_indices()
find_min_in_even_rows()
swap_row_with_max_diagonal()
multiply_rows_containing_value()