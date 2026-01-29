import requests
import json
import tkinter as tk
from tkinter import messagebox


def get_github_data():
    username = entry.get().strip()
    if not username:
        messagebox.showwarning("Ошибка", "Введите имя пользователя GitHub!")
        return

    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url)
        if response.status_code != 200:
            messagebox.showerror("Ошибка", f"Не удалось получить данные.\nКод: {response.status_code}")
            return

        user_data = response.json()

        filtered_data = {
            "company": user_data.get("company"),
            "created_at": user_data.get("created_at"),
            "email": user_data.get("email"),
            "id": user_data.get("id"),
            "name": user_data.get("name"),
            "url": user_data.get("url")
        }

        with open("user_data.json", "w", encoding="utf-8") as file:
            json.dump(filtered_data, file, indent=4, ensure_ascii=False)

        messagebox.showinfo("Успех", f"Данные пользователя '{username}' сохранены в 'user_data.json'!")

    except requests.RequestException as e:
        messagebox.showerror("Ошибка сети", f"Не удалось подключиться к GitHub.\n{e}")


root = tk.Tk()
root.title("GitHub User Info")
root.geometry("400x200")

label = tk.Label(root, text="Введите имя пользователя GitHub:")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack()

button = tk.Button(root, text="Получить данные", command=get_github_data)
button.pack(pady=10)

root.mainloop()