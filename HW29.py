import tkinter as tk
from tkinter import messagebox
import requests
import os

def fetch_data():
    id_value = entry_id.get()
    if not id_value.isdigit():
        messagebox.showerror("Ошибка", "Введите числовой ID!")
        return
    
    try:
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id_value}")
        if response.status_code == 200:
            data = response.json()
            text_output.delete("1.0", tk.END)
            text_output.insert(tk.END, str(data))
            save_data(data)
        else:
            messagebox.showerror("Ошибка", "Данные не найдены!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось выполнить запрос: {e}")

def save_data(data):
    folder = "saved_data"
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, f"post_{data['id']}.json")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(str(data))
    messagebox.showinfo("Успех", f"Данные сохранены в {file_path}")

# Интерфейс
root = tk.Tk()
root.title("Запрос данных")

tk.Label(root, text="Введите ID:").pack(pady=5)
entry_id = tk.Entry(root)
entry_id.pack(pady=5)

btn_fetch = tk.Button(root, text="Запросить", command=fetch_data)
btn_fetch.pack(pady=5)

text_output = tk.Text(root, height=10, width=50)
text_output.pack(pady=10)

root.mainloop()
