# 📦 Imports and Setup ================================================
import tkinter as tk
import json
import random
from show import show_text_review
import os

# 📁 File Path Configuration ==========================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "new_words.json")

# 🔁 Main Function: Review Words ======================================
def review_words(parent, input_lang):
    
    # 🖼️ Create Review Window ========================================
    child = tk.Toplevel(parent)
    child.title("Review words")

    # 🎛️ Language Selection UI =======================================
    navbar = tk.Frame(child)
    navbar.pack(pady=10, padx=10, anchor='w')
    options = ["None", "English", "Vietnamese", "Chinese"]
    lang = tk.StringVar()
    lang.set(options[2])  # Default value
    tk.Label(navbar, text="Translation: ", fg="blue").grid(row=0, column=0, sticky="w")
    option_menu = tk.OptionMenu(navbar, lang, *options)
    option_menu.grid(row=0, column=1, sticky="w")
    option_menu.config(bg=child.cget("bg"), highlightthickness=0, bd=0, fg="red")

    # 💾 Save Function ================================================
    def save(data, data_2, input_lang):
        with open(JSON_PATH, 'w', encoding="utf-8") as file:
            json.dump({
                "Chinese": data if input_lang == "Chinese" else data_2,
                "English": data_2 if input_lang == "Chinese" else data
            }, file, ensure_ascii=False, indent=4)

    # 📖 Load Review Data =============================================
    with open(JSON_PATH, "r", encoding="utf-8") as file:
        content = json.load(file)
        data = content[input_lang]
        other_lang = "Chinese" if input_lang == "English" else "English"
        data_2 = content[other_lang]
        number_words = len(data) + len(data_2)

    # 🧾 Display Area Setup ===========================================
    text_container = tk.Frame(child)
    text_container.pack(pady=(10, 10))
    rand_int = 0
    label_text = tk.StringVar(value="")
    tran = True
    pro = True

    if len(data) < 1:
        tk.Label(text_container, text="There is no data saved", fg="red", font=("Arial", 20)).pack()
    else:
        rand_int = random.randint(0, len(data) - 1)
        label_text.set(data[rand_int]["text"])
        selected = data[rand_int]["selected"]
        print("There first time rand_int is :", rand_int)
        print("text is showed the first time", data[rand_int]["text"])
        show_text_review(text_container, label_text, lang.get(), selected, input_lang, pro, tran)

    # 🔄 Next Item Handler ============================================
    def next_item():
        nonlocal rand_int, tran, pro
        if len(data) < 1:
            next_button.config(state="disabled")  
        else:
            rand_int = random.randint(0, len(data) - 1)
            label_text.set(data[rand_int]["text"])
            selected = data[rand_int]["selected"]
            print("text is being showed :", data[rand_int]["text"])
            show_text_review(text_container, label_text, lang.get(), selected, input_lang, pro, tran)

    # ❌ Remove Item Handler ==========================================
    def remove():
        nonlocal rand_int, tran, pro
        if len(data) < 1:
            remove_button.config(state="disabled")
        elif len(data) == 1:
            del data[rand_int]
            save(data, data_2, input_lang)
            show_text_review(text_container, tk.StringVar(value=""), lang.get(), selected=[], input_lang=input_lang, pro=False, tran=False)
            tk.Label(text_container, text="There is no data saved", font=("Arial", 20), fg="red").pack()
        else:
            del data[rand_int]
            save(data, data_2, input_lang)
            next_item()

    # 🔘 Buttons: Next, Remove ========================================
    button_container = tk.Frame(child)
    button_container.pack(pady=(5, 5))

    next_button = tk.Button(button_container, text="Next", width=12, command=next_item)
    next_button.grid(row=0, column=0, padx=10, pady=10)

    remove_button = tk.Button(button_container, text="Remove", width=12, command=remove)
    remove_button.grid(row=0, column=1, padx=10, pady=10)

    # 🗣️ Toggle Pronunciation ========================================
    def Pronuciation():
        nonlocal pro, tran
        if len(data) < 1:
            pro_button.config(state="disabled")
        else:
            pro = not pro
            show_text_review(text_container, label_text, lang.get(), selected, input_lang, pro, tran)

    # 🌐 Toggle Translation ===========================================
    def Translation():
        nonlocal pro, tran
        if len(data) < 1:
            tran_Button.config(state="disabled")
        else:
            tran = not tran
            show_text_review(text_container, label_text, lang.get(), selected, input_lang, pro, tran)

    tran_Button = tk.Button(button_container, text="Translation", width=12, command=Translation)
    tran_Button.grid(row=1, column=0, padx=10)

    pro_button = tk.Button(button_container, text="Pronuciation", width=12, command=Pronuciation)
    pro_button.grid(row=1, column=1, padx=10)

    # 🔢 Word Count Display ===========================================
    tk.Label(child, text=f"Left: {number_words} w", fg="blue").pack(side="left", padx=3, pady=3)

    # 🖼️ Final Window Settings ========================================
    child.geometry("750x300+400+200")
    child.attributes("-topmost", True)
