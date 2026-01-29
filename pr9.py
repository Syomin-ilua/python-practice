# Функция для чтения матрицы из файла
# Возвращает матрицу (список списков) и её размеры
def read_matrix_from_file(file_name):
    with open(file_name, 'r') as file:
        n, m = map(int, file.readline().strip().split())
        
        matrix = []
        for _ in range(n):
            row = list(map(int, file.readline().strip().split()))
            matrix.append(row)
    
    return matrix, n, m

# Функция для записи матрицы в файл
def write_matrix_to_file(file_name, matrix, n, m):
    with open(file_name, 'w') as file:
        file.write(f"{n} {m}\n")
        
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

def main():
    fio = input("Введите ФИО: ")
    group = input("Введите номер группы: ")
    
    input_file = f"{fio}_{group}_vvod.txt"
    output_file = f"{fio}_{group}_vivod.txt"
    
    try:
        matrix, n, m = read_matrix_from_file(input_file)
        
        result_matrix = [[matrix[j][i] for j in range(n)] for i in range(m)]
        
        write_matrix_to_file(output_file, result_matrix, m, n)
        
        print(f"Результаты успешно записаны в файл {output_file}")
        
    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден!")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

main()
