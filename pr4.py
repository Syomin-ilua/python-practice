# Числа от A до B включительно
A1 = int(input("Введите A: "))
B1 = int(input("Введите B: "))
print("Результат:")
for i in range(A1, B1 + 1):
    print(i, end=" ")
print("\n")

# Числа от A до B в порядке возрастания/убывания
A2 = int(input("Введите A: "))
B2 = int(input("Введите B: "))
step = 1 if A2 < B2 else -1
print("Результат:")
for i in range(A2, B2 + step, step):
    print(i, end=" ")
print("\n")

# Задача 3: Нечётные числа от A до B в порядке убывания (A > B)
A3 = int(input("Введите A (больше B): "))
B3 = int(input("Введите B (меньше A): "))
start = A3 if A3 % 2 != 0 else A3 - 1
print("Результат:")
for i in range(start, B3 - 1, -2):
    print(i, end=" ")
print("\n")

# Задача 4: Сумма N чисел
n4 = int(input("Введите количество чисел N: "))
total4 = 0
for _ in range(n4):
    total4 += int(input("Введите число: "))
print(f"Сумма: {total4}\n")

# Задача 5: Сумма кубов 1³+2³+...+n³
n5 = int(input("Введите n: "))
total5 = 0
for i in range(1, n5 + 1):
    total5 += i ** 3
print(f"Сумма кубов: {total5}\n")

# Задача 6: Факториал n!
n6 = int(input("Введите n: "))
factorial6 = 1
for i in range(2, n6 + 1):
    factorial6 *= i
print(f"Факториал {n6}! = {factorial6}\n")

# Задача 7: Сумма факториалов 1!+2!+...+n! (один цикл)
n7 = int(input("Введите n: "))
total7 = 0
current_fact = 1
for i in range(1, n7 + 1):
    current_fact *= i
    total7 += current_fact
print(f"Сумма факториалов: {total7}\n")

# Задача 8: Лесенка из n ступенек (n ≤ 9)
n8 = int(input("Введите n (1-9): "))
print("Лесенка:")
for i in range(1, n8 + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
print()

# Задача 9: Сумма N первых чисел Фибоначчи
N9 = int(input("Введите N: "))
a9, b9 = 0, 1
total9 = 0
for _ in range(N9):
    total9 += a9
    a9, b9 = b9, a9 + b9
print(f"Сумма первых {N9} чисел Фибоначчи: {total9}\n")

# Задача 10: Сумма N чисел Фибоначчи, начиная с K-го
N10 = int(input("Введите N (количество чисел): "))
K10 = int(input("Введите K (начальный номер): "))
a10, b10 = 0, 1
total10 = 0
count10 = 0

while count10 < N10 + K10 - 1:
    if count10 >= K10 - 1:
        total10 += a10
    a10, b10 = b10, a10 + b10
    count10 += 1

print(f"Сумма {N10} чисел Фибоначчи с {K10}-го номера: {total10}")