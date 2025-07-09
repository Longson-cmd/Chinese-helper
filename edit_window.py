import tkinter as tk

def open_edit_window(parent, label_text, show_text_func):
    child = tk.Toplevel(parent)
    child.title("Edit Chinese Text")

    tk.Label(child, text="Edit Chinese Text:").pack(pady=10)
    entry = tk.Entry(child, width=30)
    entry.pack(pady=10)
    entry.insert(0, label_text.get())

    def save_text():
        label_text.set(entry.get())
        child.destroy()
        show_text_func(label_text)

    tk.Button(child, text="Change", command=save_text).pack(pady=10)
    child.geometry("400x200+600+300")
    child.attributes("-topmost", True)