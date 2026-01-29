# Практическая работа №6        

# Найти максимальный элемент и вывести массив в обратном порядке (Вариант 1)
def find_max_and_reverse_array():
    
    N = int(input("Введите количество элементов массива: "))
    arr = []
    for i in range(N):
        arr.append(int(input(f"Введите элемент {i+1}: ")))
    
    max_element = max(arr)
    print(f"Максимальный элемент: {max_element}")
    print("Массив в обратном порядке:", arr[::-1])

# Найти минимальный элемент и его индекс (Вариант 2)
def find_min_element_and_index():
    
    N = int(input("Введите количество элементов массива: "))
    arr = []
    for i in range(N):
        arr.append(int(input(f"Введите элемент {i+1}: ")))
    
    min_element = min(arr)
    min_index = arr.index(min_element)
    print(f"Минимальный элемент: {min_element}")
    print(f"Индекс минимального элемента: {min_index}")

# Вычислить сумму элементов с нечетными индексами (Вариант 3)
def sum_odd_index_elements():
    
    n = int(input("Введите количество элементов массива D: "))
    D = []
    for i in range(n):
        D.append(float(input(f"Введите элемент D[{i}]: ")))
    
    sum_odd = 0
    for i in range(1, n, 2):
        sum_odd += D[i]
    
    print(f"Массив D: {D}")
    print(f"Сумма элементов с нечетными индексами: {sum_odd}")

# Найти максимальный элемент и его порядковый номер (Вариант 4)
def find_max_element_and_position():
    
    N = int(input("Введите количество элементов массива: "))
    arr = []
    for i in range(N):
        arr.append(int(input(f"Введите элемент {i+1}: ")))
    
    max_element = max(arr)
    max_index = arr.index(max_element)
    print(f"Максимальный элемент: {max_element}")
    print(f"Порядковый номер (индекс): {max_index}")

# Найти пары отрицательных чисел, стоящих рядом (Вариант 5)
def find_adjacent_negative_pairs():
    
    arr = []
    for i in range(10):
        arr.append(int(input(f"Введите элемент {i+1}: ")))
    
    print("Пары отрицательных чисел, стоящих рядом:")
    found = False
    for i in range(9):
        if arr[i] < 0 and arr[i+1] < 0:
            print(f"({arr[i]}, {arr[i+1]}) на позициях {i} и {i+1}")
            found = True
    
    if not found:
        print("Нет пар отрицательных чисел, стоящих рядом")

# Подсчитать количество элементов меньше и больше максимального (Вариант 6)
def count_elements_relative_to_max():

    arr = []
    for i in range(10):
        arr.append(int(input(f"Введите элемент {i+1}: ")))
    
    max_element = max(arr)
    less_count = 0
    greater_count = 0
    
    for num in arr:
        if num < max_element:
            less_count += 1
        elif num > max_element:
            greater_count += 1
    
    print(f"Максимальный элемент: {max_element}")
    print(f"Количество элементов меньше максимального: {less_count}")
    print(f"Количество элементов больше максимального: {greater_count}")

# Вычислить сумму элементов с четными индексами и произведение с нечетными (Вариант 7)
def sum_even_index_product_odd_index():
    
    N = int(input("Введите количество элементов массива: "))
    arr = []
    for i in range(N):
        arr.append(int(input(f"Введите элемент {i+1}: ")))
    
    sum_even = 0
    product_odd = 1
    has_odd = False
    
    for i in range(N):
        if i % 2 == 0:
            sum_even += arr[i]
        else:
            product_odd *= arr[i]
            has_odd = True
    
    print(f"Массив: {arr}")
    print(f"Сумма элементов с четными индексами: {sum_even}")
    if has_odd:
        print(f"Произведение элементов с нечетными индексами: {product_odd}")
    else:
        print("Нет элементов с нечетными индексами")

# Вычислить сумму и произведение всех элементов списка (Вариант 8)
def calculate_sum_and_product():
    
    N = int(input("Введите количество элементов списка: "))
    lst = []
    for i in range(N):
        lst.append(float(input(f"Введите элемент {i+1}: ")))
    
    sum_elements = sum(lst)
    product = 1
    for num in lst:
        product *= num
    
    print(f"Список: {lst}")
    print(f"Сумма элементов: {sum_elements}")
    print(f"Произведение элементов: {product}")

# Найти минимальный по модулю элемент и вывести массив в обратном порядке (Вариант 9)
def find_min_abs_and_reverse():
    
    N = int(input("Введите количество элементов массива: "))
    arr = []
    for i in range(N):
        arr.append(float(input(f"Введите элемент {i+1}: ")))
    
    min_abs = min(abs(num) for num in arr)
    print(f"Минимальный по модулю элемент: {min_abs}")
    print("Массив в обратном порядке:", arr[::-1])

# Найти повторяющиеся элементы в списке (Вариант 10)
def find_duplicate_elements():
    
    N = int(input("Введите количество элементов списка: "))
    lst = []
    for i in range(N):
        lst.append(input(f"Введите элемент {i+1}: "))
    
    duplicates = []
    seen = set()
    
    for item in lst:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)
    
    if duplicates:
        print("Повторяющиеся элементы:", duplicates)
    else:
        print("Повторяющиеся элементы отсутствуют")

# Найти наибольший четный элемент в списке (Вариант 11)
def find_max_even_element():
    
    N = int(input("Введите количество элементов списка: "))
    lst = []
    for i in range(N):
        lst.append(int(input(f"Введите элемент {i+1}: ")))
    
    even_numbers = [num for num in lst if num % 2 == 0]
    
    if even_numbers:
        max_even = max(even_numbers)
        print(f"Наибольший четный элемент: {max_even}")
    else:
        print("В списке нет четных чисел")

# Найти наименьший нечетный элемент в списке (Вариант 12)
def find_min_odd_element():
    
    N = int(input("Введите количество элементов списка: "))
    lst = []
    for i in range(N):
        lst.append(int(input(f"Введите элемент {i+1}: ")))
    
    odd_numbers = [num for num in lst if num % 2 != 0]
    
    if odd_numbers:
        min_odd = min(odd_numbers)
        print(f"Наименьший нечетный элемент: {min_odd}")
    else:
        print("В списке нет нечетных чисел")

# Найти одинаковые элементы и их индексы (Вариант 13)
def find_duplicate_values_and_indices():
    
    N = int(input("Введите количество элементов массива: "))
    arr = []
    for i in range(N):
        arr.append(int(input(f"Введите элемент {i+1}: ")))
    
    duplicates = {}
    for i in range(N):
        for j in range(i + 1, N):
            if arr[i] == arr[j]:
                if arr[i] not in duplicates:
                    duplicates[arr[i]] = []
                if i not in duplicates[arr[i]]:
                    duplicates[arr[i]].append(i)
                if j not in duplicates[arr[i]]:
                    duplicates[arr[i]].append(j)
    
    if duplicates:
        print("Одинаковые элементы и их индексы:")
        for value, indices in duplicates.items():
            print(f"Элемент {value}: индексы {sorted(indices)}")
    else:
        print("Одинаковых элементов нет")

# Поменять местами максимальный и минимальный элементы (Вариант 14)
def swap_max_min_elements():
    
    N = int(input("Введите количество элементов массива: "))
    arr = []
    for i in range(N):
        arr.append(float(input(f"Введите элемент {i+1}: ")))
    
    max_index = arr.index(max(arr))
    min_index = arr.index(min(arr))
    
    print(f"Исходный массив: {arr}")
    print(f"Максимальный элемент: {arr[max_index]} (индекс {max_index})")
    print(f"Минимальный элемент: {arr[min_index]} (индекс {min_index})")
    
    arr[max_index], arr[min_index] = arr[min_index], arr[max_index]
    print(f"Массив после замены: {arr}")

# Найти повторяющиеся строки в списке (Вариант 15)
def find_repeating_strings():
    N = int(input("Введите количество элементов списка: "))
    lst = []
    for i in range(N):
        lst.append(input(f"Введите элемент {i+1}: "))
    
    duplicates = []
    seen = set()
    
    for item in lst:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)
    
    if duplicates:
        print("Повторяющиеся элементы:", duplicates)
    else:
        print("Повторяющиеся элементы отсутствуют")

 
find_max_and_reverse_array()      
find_min_element_and_index()      
sum_odd_index_elements()          
find_max_element_and_position()   
find_adjacent_negative_pairs()    
count_elements_relative_to_max()  
sum_even_index_product_odd_index() 
calculate_sum_and_product()       
find_min_abs_and_reverse()        
find_duplicate_elements()         
find_max_even_element()           
find_min_odd_element()            
find_duplicate_values_and_indices() 
swap_max_min_elements()           
find_repeating_strings()