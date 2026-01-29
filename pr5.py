# Практическая работа №5

# Данные для всех вариантов
texts = {
    1: "Электронные книги эффективны для экологического образования.",
    2: "JSON: {имя: 'Иван', возраст: 25, город: 'Москва'}",
    3: "Питон... Это язык программирования... Очень популярный...",
    4: "Карта, парта, арфа, шарф, бархат, карнавал.",
    5: "JavaScript и Python - Два Популярных Языка Программирования.",
    6: "Антибиотики атакуют анаэробные артерии акул.",
    7: "Программирование помогает программистам писать программы! Продуктивно!",
    8: "Эта строка заканчивается вопросительным знаком?",
    9: "Тест тест Тестирование теста тестовой системы.",
    10: "machine learning models need more data. but quality matters too!",
    11: "Ммм... молоко, мед, мандарины, мороженое! Ммм!",
    12: "Семья, друзья, мечты, планы, цели, успехи.",
    13: "Функция [с вложенным кодом] может содержать сложную логику.",
    14: "Анаконда атаковала, а ящерица убежала, удав удивился.",
    15: "Технологии трансформируют традиционные транспортные тренды."
}

# Найти количество слов, начинающихся с буквы 'е'
def count_words_starting_with_е():
    text = texts[1]
    print(f"Исходная строка: {text}")
    count = 0
    words = text.split()
    for word in words:
        if word.strip(".,!?:;").lower().startswith('е'):
            count += 1
    print(f"Количество слов, начинающихся с буквы 'е': {count}")

# Заменить все двоеточия (:) знаком процента (%)
def replace_colons_with_percent():
    print("=" * 60)
    text = texts[2]
    print(f"Исходная строка: {text}")
    old_char = ":"
    new_char = "%"
    new_text = text.replace(old_char, new_char)
    count = text.count(old_char)
    print(f"Новая строка: {new_text}")
    print(f"Количество замен: {count}")

# Удалить символ точку (.) и подсчитать количество удалений
def remove_dots_and_count():
    print("=" * 60)
    text = texts[3]
    print(f"Исходная строка: {text}")
    old_char = "."
    new_text = text.replace(old_char, "")
    count = text.count(old_char)
    print(f"Строка без точек: {new_text}")
    print(f"Количество удаленных символов: {count}")

# Заменить букву 'а' буквой 'о' и подсчитать статистику
def replace_а_with_о_and_stats():
    text = texts[4]
    print(f"Исходная строка: {text}")
    old_char = "а"
    new_char = "о"
    new_text = text.replace(old_char, new_char)
    count = text.count(old_char)
    total_symbols = len(text)
    print(f"Новая строка: {new_text}")
    print(f"Количество замен: {count}")
    print(f"Количество символов в строке: {total_symbols}")

# Заменить все заглавные буквы строчными
def convert_to_lowercase():
    text = texts[5]
    print(f"Исходная строка: {text}")
    new_text = text.lower()
    print(f"Новая строка: {new_text}")

# Удалить все буквы 'а' и подсчитать количество удалений
def remove_all_а_and_count():
    text = texts[6]
    print(f"Исходная строка: {text}")
    char_to_remove = "а"
    new_text = text.replace(char_to_remove, "")
    count = text.count(char_to_remove)
    print(f"Строка без букв 'а': {new_text}")
    print(f"Количество удаленных символов: {count}")

# Заменить звездочками все буквы 'п' в первой половине строки
def replace_p_with_stars_in_first_half():
    text = texts[7]
    print(f"Исходная строка: {text}")
    n = len(text)
    half = n // 2
    chars = list(text)
    for i in range(half):
        if chars[i].lower() == 'п':
            chars[i] = '*'
    new_text = ''.join(chars)
    print(f"Преобразованная строка: {new_text}")

# Подсчитать, сколько слов в строке, заканчивающейся точкой
def count_words_in_sentence():
    text = texts[8]
    print(f"Исходная строка: {text}")
    words = text.rstrip('.').split()
    count = len(words)
    print(f"Количество слов в строке: {count}")

# Определить, сколько раз в тексте встречается заданное слово
def count_word_occurrences():
    text = texts[9]
    target_word = "слово"
    print(f"Исходная строка: {text}")
    print(f"Искомое слово: '{target_word}'")
    words = [word.strip(".,!?:;").lower() for word in text.split()]
    count = words.count(target_word.lower())
    print(f"Слово '{target_word}' встречается {count} раз(а)")

# Преобразовать строку так, чтобы каждое слово начиналось с заглавной буквы
def capitalize_all_words():
    print("=" * 60)
    text = texts[10]
    print(f"Исходная строка: {text}")
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    new_text = ' '.join(capitalized_words)
    print(f"Преобразованная строка: {new_text}")

# Найти самую длинную последовательность 'н' и заменить восклицательные знаки на точки
def find_longest_n_sequence_and_replace_exclamation():
    text = texts[11]
    print(f"Исходная строка: {text}")
    
    # Подсчет самой длинной последовательности 'н'
    max_count = 0
    current_count = 0
    for char in text:
        if char.lower() == 'н':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    
    # Замена восклицательных знаков на точки
    new_text = text.replace('!', '.')
    
    print(f"Самая длинная последовательность 'н': {max_count}")
    print(f"Преобразованная строка: {new_text}")

# Вывести все слова, оканчивающиеся на букву 'я'
def find_words_ending_with_ya():
    text = texts[12]
    print(f"Исходная строка: {text}")
    words = text.split()
    result_words = []
    for word in words:
        cleaned_word = word.strip(".,!?:;")
        if cleaned_word.lower().endswith('я'):
            result_words.append(cleaned_word)
    print(f"Слова, оканчивающиеся на 'я': {', '.join(result_words)}")

# Вывести все символы, расположенные внутри скобок
def extract_text_between_parentheses():
    text = texts[13]
    print(f"Исходная строка: {text}")
    start = text.find('(')
    end = text.find(')')
    if start != -1 and end != -1 and start < end:
        inner_text = text[start + 1:end]
        print(f"Символы внутри скобок: {inner_text}")
    else:
        print("Скобки не найдены или расположены некорректно")

# Вывести слова, начинающиеся на 'а' и оканчивающиеся на 'я'
def find_words_starting_with_а_or_ending_with_ya():
    text = texts[14]
    print(f"Исходная строка: {text}")
    words = text.split()
    result_words = []
    for word in words:
        cleaned_word = word.strip(".,!?:;").lower()
        if cleaned_word.startswith('а') or cleaned_word.endswith('я'):
            result_words.append(word.strip(".,!?:;"))
    print(f"Слова, начинающиеся на 'а' или оканчивающиеся на 'я': {', '.join(result_words)}")

# Подсчитать количество букв 'т' в строке
def count_letter_t():
    text = texts[15]
    print(f"Исходная строка: {text}")
    char_to_count = 'т'
    count = text.lower().count(char_to_count)
    print(f"Количество букв '{char_to_count}' в строке: {count}")
    
count_words_starting_with_е()
replace_colons_with_percent()
remove_dots_and_count()
replace_а_with_о_and_stats()
convert_to_lowercase()
remove_all_а_and_count()
replace_p_with_stars_in_first_half()
count_words_in_sentence()
count_word_occurrences()
capitalize_all_words()
find_longest_n_sequence_and_replace_exclamation()
find_words_ending_with_ya()
extract_text_between_parentheses()
find_words_starting_with_а_or_ending_with_ya()
count_letter_t()
