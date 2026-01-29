# Практическая работа №3

# Даны 3 числа, выбрать из них те, которые принадлежат интервалу
a = 0 
b = 2
c = 5
result = [x for x in (a, b, c) if 1 <= x <= 3]
print(result)  # [2]

# Сравнение двух чисел и вывод наибольшего
def max_of_two(a, b):
    return a if a > b else b

print(max_of_two(7,3))

# Проверка числа на четность и вывод результата
def is_even(num):
    return num % 2 == 0

print(is_even(4))

# Разделение числа на четные и нечетные цифры
def split_even_odd_digits(num):
    num_str = str(abs(num))
    evens = [int(d) for d in num_str if int(d) % 2 == 0]
    odds = [int(d) for d in num_str if int(d) % 2 != 0]
    return evens, odds

print(split_even_odd_digits(16785))

# Проверка числа на простоту
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(9))

# Вычисление среднего арифметического трех чисел
def average_of_three(a, b, c):
    return (a + b + c) / 3

print(average_of_three(3,6,7))

# Проверка числа на кратность 7.
def is_multiple_of_7(num):
    return num % 7 == 0

print(is_multiple_of_7(49))

# Определение, является ли год високосным
def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

print(is_leap_year(2014))

# Подсчет количества дней в месяце по его номеру.
def days_in_month(month, year=None):
    if month == 2:
        if year and is_leap_year(year):
            return 29
        return 28
    if month in [4, 6, 9, 11]:
        return 30
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    return "Неверный номер месяца"

print(days_in_month(2))

# Расчет площади треугольника по формуле Герона.
def triangle_area_heron(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5
    else:
        return "Треугольник не существует"

print(triangle_area_heron(2,6,9))    

# Проверка на равенство трех чисел.
def are_three_equal(a, b, c):
    return a == b == c

print(are_three_equal(3,6,3))

# Проверка возраста пользователя и вывод соответствующего сообщения
def age_message(age):
    if age < 18:
        return "Несовершеннолетний"
    elif 18 <= age <= 60:
        return "Взрослый"
    else:
        return "Пожилой"

print(age_message(26))   

# Определение, является ли введенное число положительным или отрицательным. 
def sign_check(num):
    if num > 0:
        return "Положительное"
    elif num < 0:
        return "Отрицательное"
    else:
        return "Ноль"

print(sign_check(-11))

# Проверка, является ли год високосным, и вывод количества дней в феврале.
def feb_days(year):
    return 29 if is_leap_year(year) else 28

print(feb_days(2014))

# Проверка, принадлежит ли точка квадрату с координатами (0,0),(0,5), (5,0), (5,5).
def in_square(x, y):
    return 0 <= x <= 5 and 0 <= y <= 5

print(in_square(1,4))

# Расчет суммы и разности двух чисел.
def sum_and_diff(a, b):
    return a + b, a - b

print(sum_and_diff(7,8))

# Проверка числа на кратность 3 и 5, вывод соответствующего сообщения
def multiple_3_5(num):
    if num % 3 == 0 and num % 5 == 0:
        return "Кратно 3 и 5"
    elif num % 3 == 0:
        return "Кратно 3"
    elif num % 5 == 0:
        return "Кратно 5"
    else:
        return "Не кратно 3 и 5"

print(multiple_3_5(15))

# Определение, является ли год вековым (делится на 100).
def is_century_year(year):
    return year % 100 == 0

print(is_century_year(2000))

# Определение, является ли введенное число целым или дробным.
def is_integer_or_float(num):
    # Если число передано как float, но равно целому
    if isinstance(num, float):
        return "Целое" if num.is_integer() else "Дробное"
    else:
        return "Целое"

print(is_integer_or_float(15))