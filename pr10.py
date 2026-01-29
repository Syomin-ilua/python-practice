import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Сёмин Илья Александрович")
        
        # Устанавливаем минимальный размер окна
        self.root.minsize(500, 300)
        
        # Создаем меню
        self.create_menu()
        
        # Создаем Notebook (вкладки)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Создаем вкладки
        self.create_tab1()
        self.create_tab2()
        self.create_tab3()
        
        # Текущий текст для третьей вкладки
        self.current_text = ""
    
    def create_menu(self):
        # Создание меню
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Меню "Файл"
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Загрузить текст", command=self.load_text_from_file)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.root.quit)
        
        # Меню "Помощь"
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Помощь", menu=help_menu)
        help_menu.add_command(label="О программе", command=self.show_about)
    
    def create_tab1(self):
        """Создание первой вкладки - калькулятор"""
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Калькулятор")
        
        # Поля для ввода чисел
        tk.Label(self.tab1, text="Число 1:").grid(row=0, column=0, padx=10, pady=10)
        self.num1_entry = tk.Entry(self.tab1, width=15)
        self.num1_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Выпадающий список операций
        self.operation_var = tk.StringVar()
        self.operation_var.set("+")  # значение по умолчанию
        operations = ["+", "-", "*", "/"]
        operation_menu = tk.OptionMenu(self.tab1, self.operation_var, *operations)
        operation_menu.grid(row=0, column=2, padx=10, pady=10)
        
        tk.Label(self.tab1, text="Число 2:").grid(row=0, column=3, padx=10, pady=10)
        self.num2_entry = tk.Entry(self.tab1, width=15)
        self.num2_entry.grid(row=0, column=4, padx=10, pady=10)
        
        # Кнопка вычисления
        calc_button = tk.Button(self.tab1, text="Вычислить", command=self.calculate)
        calc_button.grid(row=1, column=0, columnspan=5, pady=20)
        
        # Поле для вывода результата
        tk.Label(self.tab1, text="Результат:").grid(row=2, column=0, padx=10, pady=10)
        self.result_label = tk.Label(self.tab1, text="", font=("Arial", 12))
        self.result_label.grid(row=2, column=1, columnspan=4, padx=10, pady=10)
    
    def calculate(self):
        """Выполнение вычисления"""
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()
            
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    messagebox.showerror("Ошибка", "Деление на ноль!")
                    return
                result = num1 / num2
            else:
                result = "Неизвестная операция"
            
            self.result_label.config(text=f"{result}")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные числа!")
    
    def create_tab2(self):
        """Создание второй вкладки - чекбоксы"""
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Выбор варианта")
        
        # Переменные для чекбоксов
        self.check_var1 = tk.BooleanVar()
        self.check_var2 = tk.BooleanVar()
        self.check_var3 = tk.BooleanVar()
        
        # Создание чекбоксов
        self.check1 = tk.Checkbutton(self.tab2, text="Первый", variable=self.check_var1)
        self.check1.pack(pady=15)
        
        self.check2 = tk.Checkbutton(self.tab2, text="Второй", variable=self.check_var2)
        self.check2.pack(pady=15)
        
        self.check3 = tk.Checkbutton(self.tab2, text="Третий", variable=self.check_var3)
        self.check3.pack(pady=15)
        
        # Кнопка подтверждения выбора
        check_button = tk.Button(self.tab2, text="Показать выбранные варианты", 
                                command=self.show_selected)
        check_button.pack(pady=30)
    
    def show_selected(self):
        """Показать выбранные варианты"""
        selected = []
        
        if self.check_var1.get():
            selected.append("Первый")
        if self.check_var2.get():
            selected.append("Второй")
        if self.check_var3.get():
            selected.append("Третий")
        
        if selected:
            message = f"Вы выбрали: {', '.join(selected)}"
        else:
            message = "Вы ничего не выбрали"
        
        messagebox.showinfo("Ваш выбор", message)
    
    def create_tab3(self):
        """Создание третьей вкладки - работа с текстом"""
        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab3, text="Работа с текстом")
        
        # Текстовое поле
        self.text_widget = tk.Text(self.tab3, wrap='word', height=10)
        self.text_widget.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Добавляем Scrollbar
        scrollbar = tk.Scrollbar(self.text_widget)
        scrollbar.pack(side='right', fill='y')
        self.text_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text_widget.yview)
    
    def load_text_from_file(self):
        """Загрузка текста из файла"""
        file_path = filedialog.askopenfilename(
            title="Выберите текстовый файл",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    text = file.read()
                
                # Очищаем текстовое поле и вставляем загруженный текст
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(1.0, text)
                self.current_text = text
                
                messagebox.showinfo("Успех", f"Текст загружен из файла:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось загрузить файл:\n{str(e)}")
    
    def show_about(self):
        """Показать информацию о программе"""
        messagebox.showinfo("О программе", 
                           "Приложение с графическим интерфейсом\n"
                           "Автор: Сёмин Илья Александрович\n"
                           "Практическая работа 10")


root = tk.Tk()
app = MyApp(root)
root.mainloop()