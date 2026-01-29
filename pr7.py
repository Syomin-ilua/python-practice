import math

# ВАРИАНТ 1, ЗАДАНИЕ 2: Сумма и среднее арифметическое элементов массивов
def process_array_statistics():
    
    arrays = []
    for i in range(3):
        n = int(input(f"Введите количество элементов в массиве {i+1} (не более 15): "))
        if n > 15:
            n = 15
            print(f"Количество элементов ограничено до 15")
        
        arr = []
        for j in range(n):
            arr.append(int(input(f"Массив {i+1}, элемент {j+1}: ")))
        arrays.append(arr)
    
    for i, arr in enumerate(arrays, 1):
        print(f"\nМассив {i}: {arr}")
        if arr:
            sum_arr = sum(arr)
            avg = sum_arr / len(arr)
            print(f"Сумма элементов: {sum_arr}")
            print(f"Среднее арифметическое: {avg:.2f}")
        else:
            print("Массив пуст")


# ВАРИАНТ 2, ЗАДАНИЕ 2: Вычисление площадей прямоугольников
def calculate_rectangle_areas():
    
    rectangles = []
    for i in range(3):
        print(f"\nПрямоугольник {i+1}:")
        a = float(input("Введите длину: "))
        b = float(input("Введите ширину: "))
        rectangles.append((a, b))
    
    print("\nПлощади прямоугольников:")
    for i, (a, b) in enumerate(rectangles, 1):
        area = a * b
        print(f"Прямоугольник {i} (стороны {a} и {b}): площадь = {area:.2f}")


# ВАРИАНТ 3, ЗАДАНИЕ 2: Сортировка букв в словах строки
def sort_letters_in_words():
    
    text = input("Введите строку: ")
    words = text.split()
    sorted_words = []
    
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        sorted_words.append(sorted_word)
    
    result = ' '.join(sorted_words)
    
    print(f"Исходная строка: {text}")
    print(f"Строка с отсортированными буквами: {result}")


# ВАРИАНТ 4, ЗАДАНИЕ 2: Точки внутри окружности
def check_points_in_circle():
    
    a = float(input("Введите координату a центра окружности: "))
    b = float(input("Введите координату b центра окружности: "))
    R = float(input("Введите радиус R окружности: "))
    
    points = []
    for name in ['P', 'F', 'L']:
        print(f"\nТочка {name}:")
        x = float(input(f"Введите координату {name}1: "))
        y = float(input(f"Введите координату {name}2: "))
        points.append((name, x, y))
    
    inside_points = []
    for name, x, y in points:
        distance = math.sqrt((x - a)**2 + (y - b)**2)
        if distance <= R:
            inside_points.append(name)
    
    print(f"\nУравнение окружности: (x-{a})² + (y-{b})² = {R}²")
    print(f"Всего точек внутри окружности: {len(inside_points)}")
    if inside_points:
        print(f"Точки внутри окружности: {', '.join(inside_points)}")

# ВАРИАНТ 5, ЗАДАНИЕ 2: Нахождение делителей числа
def find_number_divisors():
    
    n = int(input("Введите натуральное число: "))
    divisors = []
    
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    
    divisors.sort()
    
    print(f"Делители числа {n}:")
    print(' '.join(map(str, divisors)))


# ВАРИАНТ 6, ЗАДАНИЕ 2: Площадь выпуклого четырехугольника
def compute_quadrilateral_area():
    a = float(input("Сторона a: "))
    b = float(input("Сторона b: "))
    c = float(input("Сторона c: "))
    d = float(input("Сторона d: "))
    diagonal = float(input("Диагональ: "))
    
    p1 = (a + b + diagonal) / 2
    area1 = math.sqrt(p1 * (p1 - a) * (p1 - b) * (p1 - diagonal))
    
    p2 = (c + d + diagonal) / 2
    area2 = math.sqrt(p2 * (p2 - c) * (p2 - d) * (p2 - diagonal))
    
    area = area1 + area2
    
    print(f"Площадь выпуклого четырехугольника: {area:.4f}")


# ВАРИАНТ 7, ЗАДАНИЕ 2: Восьмеричное представление числа
def convert_to_octal_format():
    print("\n" + "=" * 60)
    print("ВАРИАНТ 7, ЗАДАНИЕ 2: Восьмеричное представление числа")
    print("=" * 60)
    
    n = int(input("Введите неотрицательное целое число: "))
    if n < 0:
        print("Число должно быть неотрицательным!")
    else:
        octal_str = oct(n)[2:]
        octal_code = octal_str.zfill(10)
        print(f"10-значный восьмеричный код числа {n}: {octal_code}")


# ВАРИАНТ 8, ЗАДАНИЕ 2: Обмен первого и последнего элементов массива
def swap_array_endpoints():
    
    m = int(input("Введите длину массива A: "))
    A = []
    for i in range(m):
        A.append(float(input(f"Введите элемент A[{i}]: ")))
    
    print(f"\nИсходный массив: {A}")
    
    if len(A) > 1:
        A[0], A[-1] = A[-1], A[0]
    
    print(f"Массив после замены первого и последнего элементов: {A}")


# Вариант 9, Задание 2: Произведение и среднее арифметическое элементов массивов
def compute_product_and_average():
    
    arrays = []
    for i in range(3):
        n = int(input(f"\nВведите количество элементов в массиве {i+1}: "))
        arr = []
        for j in range(n):
            arr.append(int(input(f"Массив {i+1}, элемент {j+1}: ")))
        arrays.append(arr)
    
    for i, arr in enumerate(arrays, 1):
        print(f"\nМассив {i}: {arr}")
        if arr:
            product = 1
            for num in arr:
                product *= num
            avg = sum(arr) / len(arr)
            print(f"Произведение элементов: {product}")
            print(f"Среднее арифметическое: {avg:.2f}")
        else:
            print("Массив пуст")


# ВАРИАНТ 10, ЗАДАНИЕ 2: Обратный порядок слов в строке
def reverse_words_in_string():
    
    text = input("Введите строку: ")
    words = text.split()
    reversed_words = words[::-1]
    result = ' '.join(reversed_words)
    
    print(f"Исходная строка: {text}")
    print(f"Строка с обратным порядком слов: {result}")

# ВАРИАНТ 11, ЗАДАНИЕ 2: Обмен максимальными элементами матриц
def swap_matrix_max_elements():
    
    rows_A = int(input("Введите количество строк матрицы A: "))
    cols_A = int(input("Введите количество столбцов матрицы A: "))
    
    A = []
    print("\nВведите элементы матрицы A:")
    for i in range(rows_A):
        row = []
        for j in range(cols_A):
            row.append(int(input(f"A[{i}][{j}]: ")))
        A.append(row)
    
    rows_B = int(input("\nВведите количество строк матрицы B: "))
    cols_B = int(input("Введите количество столбцов матрицы B: "))
    
    B = []
    print("\nВведите элементы матрицы B:")
    for i in range(rows_B):
        row = []
        for j in range(cols_B):
            row.append(int(input(f"B[{i}][{j}]: ")))
        B.append(row)
    
    max_A = A[0][0]
    max_pos_A = (0, 0)
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] > max_A:
                max_A = A[i][j]
                max_pos_A = (i, j)
    
    max_B = B[0][0]
    max_pos_B = (0, 0)
    for i in range(len(B)):
        for j in range(len(B[i])):
            if B[i][j] > max_B:
                max_B = B[i][j]
                max_pos_B = (i, j)
    
    print(f"\nМатрица A: максимальный элемент = {max_A} на позиции {max_pos_A}")
    print(f"Матрица B: максимальный элемент = {max_B} на позиции {max_pos_B}")
    
    if rows_A == rows_B and cols_A == cols_B:
        A[max_pos_A[0]][max_pos_A[1]], B[max_pos_B[0]][max_pos_B[1]] = max_B, max_A
        print("\nМатрицы после обмена максимальными элементами:")
        print(f"Матрица A: {A}")
        print(f"Матрица B: {B}")
    else:
        print("\nМатрицы разного размера, обмен невозможен")


# ВАРИАНТ 12, ЗАДАНИЕ 2: Медианы треугольника и треугольника из медиан
def calculate_triangle_medians():
    
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    c = float(input("Введите длину стороны c: "))
    
    ma = 0.5 * math.sqrt(2*b**2 + 2*c**2 - a**2)
    mb = 0.5 * math.sqrt(2*a**2 + 2*c**2 - b**2)
    mc = 0.5 * math.sqrt(2*a**2 + 2*b**2 - c**2)
    
    print(f"\nМедианы исходного треугольника:")
    print(f"Медиана к стороне a: {ma:.4f}")
    print(f"Медиана к стороне b: {mb:.4f}")
    print(f"Медиана к стороне c: {mc:.4f}")
    
    ma2 = 0.5 * math.sqrt(2*mb**2 + 2*mc**2 - ma**2)
    mb2 = 0.5 * math.sqrt(2*ma**2 + 2*mc**2 - mb**2)
    mc2 = 0.5 * math.sqrt(2*ma**2 + 2*mb**2 - mc**2)
    
    print(f"\nМедианы треугольника из медиан:")
    print(f"Медиана к стороне ma: {ma2:.4f}")
    print(f"Медиана к стороне mb: {mb2:.4f}")
    print(f"Медиана к стороне mc: {mc2:.4f}")


# ВАРИАНТ 13, ЗАДАНИЕ 2: Угол между осью абсцисс и вектором
def find_min_angle_to_xaxis():
    
    points = []
    for name in ['X', 'Y', 'Z']:
        print(f"\nТочка {name}:")
        x = float(input(f"Введите координату {name}1: "))
        y = float(input(f"Введите координату {name}2: "))
        points.append((name, x, y))
    
    angles = []
    for name, x, y in points:
        if x == 0:
            angle = 90 if y > 0 else 270
        else:
            angle_rad = math.atan(abs(y/x))
            angle = math.degrees(angle_rad)
            
            if x > 0 and y >= 0:
                pass
            elif x < 0 and y >= 0:
                angle = 180 - angle
            elif x < 0 and y < 0:
                angle = 180 + angle
            else:
                angle = 360 - angle
        
        angles.append((name, x, y, angle))
    
    min_point = angles[0]
    for point in angles:
        if point[3] < min_point[3]:
            min_point = point
    
    print("\nУглы между осью абсцисс и точками:")
    for name, x, y, angle in angles:
        print(f"Точка {name}({x}, {y}): угол = {angle:.2f}°")
    
    print(f"\nТочка с минимальным углом:")
    print(f"Точка {min_point[0]}({min_point[1]}, {min_point[2]}) с углом {min_point[3]:.2f}°")


# ВАРИАНТ 14, ЗАДАНИЕ 2: Максимальное расстояние между точками на плоскости
def find_max_distance_2d():
    
    points = []
    for name in ['X', 'Y', 'Z', 'P']:
        print(f"\nТочка {name}:")
        x = float(input(f"Введите координату {name}1: "))
        y = float(input(f"Введите координату {name}2: "))
        points.append((name, x, y))
    
    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            name1, x1, y1 = points[i]
            name2, x2, y2 = points[j]
            dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            distances.append(((name1, name2), dist))
    
    max_dist = distances[0]
    for dist_pair in distances:
        if dist_pair[1] > max_dist[1]:
            max_dist = dist_pair
    
    print("\nВсе расстояния между точками:")
    for (p1, p2), dist in distances:
        print(f"Расстояние {p1}-{p2}: {dist:.4f}")
    
    print(f"\nМаксимальное расстояние:")
    print(f"Между точками {max_dist[0][0]} и {max_dist[0][1]}: {max_dist[1]:.4f}")


# ВАРИАНТ 15, ЗАДАНИЕ 2: Минимальное расстояние между точками в пространстве
def find_min_distance_3d():
    
    points = []
    for name in ['X', 'Y', 'Z', 'T']:
        print(f"\nТочка {name}:")
        x = float(input(f"Введите координату {name}1: "))
        y = float(input(f"Введите координату {name}2: "))
        z = float(input(f"Введите координату {name}3: "))
        points.append((name, x, y, z))
    
    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            name1, x1, y1, z1 = points[i]
            name2, x2, y2, z2 = points[j]
            dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
            distances.append(((name1, name2), dist))
    
    min_dist = distances[0]
    for dist_pair in distances:
        if dist_pair[1] < min_dist[1]:
            min_dist = dist_pair
    
    print("\nВсе расстояния между точками:")
    for (p1, p2), dist in distances:
        print(f"Расстояние {p1}-{p2}: {dist:.4f}")
    
    print(f"\nМинимальное расстояние:")
    print(f"Между точками {min_dist[0][0]} и {min_dist[0][1]}: {min_dist[1]:.4f}")


process_array_statistics()
calculate_rectangle_areas()
sort_letters_in_words()
check_points_in_circle()
find_number_divisors()
compute_quadrilateral_area()
convert_to_octal_format()
swap_array_endpoints()
compute_product_and_average()
reverse_words_in_string()
swap_matrix_max_elements()
calculate_triangle_medians()
find_min_angle_to_xaxis()
find_max_distance_2d()
find_min_distance_3d()