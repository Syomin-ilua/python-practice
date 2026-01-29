# Блок А Задание №3
def reverse_print(n):
    if n < 10:
        print(n)
    else:
        print(n % 10, end='')
        reverse_print(n // 10)

# Ввод числа
num = int(input("Введите натуральное число: "))
print("Число в обратном порядке: ", end='')
reverse_print(num)

#  Блок Б Задание 3
def print_odd_positions():
    num = int(input())
    if num == 0:
        return
    print(num)  # выводим первое число (оно всегда на нечётной позиции)
    
    next_num = int(input())
    if next_num == 0:
        return  # если следующее число 0, завершаем рекурсию
    
    print_odd_positions()

print_odd_positions()
