from tkinter import Tk, Entry, Button, END, Spinbox, StringVar
import secrets

class PasswordGeneratorApp:
    LOWERCASE_CHARS = "abcdefghijklmnopqrstuvwxyz"
    UPPERCASE_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMS = "0123456789"
    SYMBOLS = "!#$%&_+-=?@^"

    def __init__(self, root):
        self.root = root
        self.root.title("Генератор паролей")
        self.root.geometry("400x150")

        self.password_var = StringVar()
        self.text_field = Entry(root, width=30, font=("Helvetica", 14), textvariable=self.password_var)
        self.text_field.pack(pady=10)

        self.length_spinbox = Spinbox(root, from_=8, to=24, font=("Helvetica", 12))
        self.length_spinbox.pack(pady=5)
        self.length_spinbox.bind("<KeyRelease>", self.validate)

        self.generate_button = Button(root, text="Сгенерировать", command=self.generate, font=("Helvetica", 12))
        self.generate_button.pack(pady=5)

        self.copy_button = Button(root, text="Копировать", command=self.copy_to_clipboard, font=("Helvetica", 12))
        self.copy_button.pack(pady=5)

    def validate(self, event):
        length = int(self.length_spinbox.get())
        if length < 8:
            self.length_spinbox.delete(0, "end")
            self.length_spinbox.insert(0, 8)
        elif length > 24:
            self.length_spinbox.delete(0, "end")
            self.length_spinbox.insert(0, 24)

    def generate_password(self, length, chars):
        return ''.join(secrets.choice(chars) for _ in range(length))

    def generate(self):
        length = int(self.length_spinbox.get())
        chars = self.LOWERCASE_CHARS + self.UPPERCASE_CHARS + self.NUMS + self.SYMBOLS
        password = self.generate_password(length, chars)
        self.password_var.set(password)

    def copy_to_clipboard(self):
        self.root.clipboard_append(self.password_var.get())

if __name__ == "__main__":
    app = PasswordGeneratorApp(Tk())
    app.root.mainloop()
