import math

# Практическая работа №2

# Пример №1

x = 14.26
y = -1.22
z = 3.5e-2  # 3.5 × 10^(-2)

numerator = 2 * math.cos(x - 2/3) # числитель
denominator = 0.5 + math.sin(y)**2 # знаменатель
fraction = numerator / denominator # большая дробь

z_numerator = z**2 # числитель дроби в скобках
z_denominator = 3 - z**2 / 5 # знаменатель дроби в скобках
z_expression = 1 + z_numerator / z_denominator # результат в скобках

s = fraction * z_expression # общий результат

print(f"Ответ(пример №1): s = {s:.6f}")

# Пример №4

x_2 = 0.4e4  # 4000
y_2 = -0.875
z_2 = -0.475e-3  # -0.000475

# Первая часть: |cos x - cos y|^(1 + 2*sin^2 y)
cos_x = math.cos(x_2)
cos_y = math.cos(y_2)
abs_diff_cos = abs(cos_x - cos_y)

sin_y = math.sin(y_2)
exponent = 1 + 2 * (sin_y ** 2)

part1 = abs_diff_cos ** exponent

# Вторая часть: 1 + z + z^2/2 + z^3/3 + z^4/4
part2 = 1 + z_2 + (z_2 ** 2) / 2 + (z_2 ** 3) / 3 + (z_2 ** 4) / 4

# Итоговое значение s
s_2 = part1 * part2

print(f"Ответ(пример №4): {s_2:.5f}")