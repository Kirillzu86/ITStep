import tkinter as tk
from tkinter import messagebox
import requests
import os

class DataFetcherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Запрос данных")

        # Создание интерфейса
        tk.Label(root, text="Введите ID:").pack(pady=5)
        self.entry_id = tk.Entry(root)
        self.entry_id.pack(pady=5)

        self.btn_fetch = tk.Button(root, text="Запросить", command=self.fetch_data)
        self.btn_fetch.pack(pady=5)

        self.text_output = tk.Text(root, height=10, width=50)
        self.text_output.pack(pady=10)

    def fetch_data(self):
        id_value = self.entry_id.get()
        if not id_value.isdigit():
            messagebox.showerror("Ошибка", "Введите числовой ID!")
            return

        try:
            response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id_value}")
            if response.status_code == 200:
                data = response.json()
                self.display_data(data)
                self.save_data(data)
            else:
                messagebox.showerror("Ошибка", "Данные не найдены!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось выполнить запрос: {e}")

    def display_data(self, data):
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, str(data))

    def save_data(self, data):
        folder = "saved_data"
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, f"post_{data['id']}.json")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(str(data))
        messagebox.showinfo("Успех", f"Данные сохранены в {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataFetcherApp(root)
    root.mainloop()
