import tkinter as tk
from pypinyin import pinyin, Style
from deep_translator import GoogleTranslator
import requests
import eng_to_ipa as ipa
selected_chars = [] 
def on_click(i, e):
    global selected_chars

    if i in selected_chars:
        selected_chars.remove(i)
        e.widget.config(bg="SystemButtonFace")

    else:
        selected_chars.append(i)
        e.widget.config(bg="lightblue")
    print(selected_chars)

frame = None
translate_frame = None


def show_text(text_container, text_var, lang, input_lang):
    global frame, translate_frame, selected_chars
    selected_chars = [] 
    if frame: frame.destroy()
    frame = tk.Frame(text_container)
    frame.pack(pady=(5, 5))


    if input_lang == "Chinese":
        for i, char in enumerate(text_var.get()):
            pinyin_char = pinyin(char, style=Style.TONE)[0][0]
            lb_py = tk.Label(frame, text = pinyin_char, font=("Arial", 10), fg="blue")
            lb_py.grid(row=0, column=i, padx=2, pady=5)
            lb_char = tk.Label(frame, text=char, font=("SimSun", 14, "bold"),  fg="red")
            lb_char.grid(row=1, column=i, padx=2)
            lb_char.bind("<Button-1>", lambda e, idx=i: on_click(idx, e))
    else:
        list_chars = text_var.get().split()
        for i, char in enumerate(list_chars):
            ipa_char = ipa.convert(char)
            lb_ipa = tk.Label(frame, text=ipa_char, font=("Arial", 10, "italic"), fg="blue")
            lb_ipa.grid(row=0, column=i, padx=2, pady=5)
            lb_char = tk.Label(frame, text=char, font=("Arial", 12, "bold"),  fg="red")
            lb_char.grid(row=1, column=i, padx=2)
            lb_char.bind("<Button-1>", lambda e, idx=i: on_click(idx, e))


    if translate_frame: translate_frame.destroy()
    translate_frame = tk.Frame(text_container)
    translate_frame.pack(pady=(5,5))
    if text_var.get() == "今天是星期一，我感觉充满能量" or lang == "None":
        tk.Label(translate_frame, text = "", font=("Arial", 12)).pack(pady=(0,5))
    else:
        try:
            if input_lang == "Chinese":
                source = "zh-CN"
            else:
                source = "en"

            if lang == "English":
                target = "en"
            elif lang == "Chinese":
                target = "zh-CN"
            else:
                target = "vi"

            if source == target:
                tk.Label(translate_frame, text = "", font=("Arial", 12)).pack(pady=(0,5))
            else:
                translator = GoogleTranslator(source=source, target=target)
                translator_result = translator.translate(text_var.get())
                tk.Label(translate_frame, text = translator_result, font=("Arial", 12)).pack(pady=(0,5))


        except requests.exceptions.RequestException as e:
            print("An error occurred:", e)
            tk.Label(translate_frame, text = "", font=("Arial", 12)).pack(pady=(0,5))

    return selected_chars



def show_text_review(text_container, text_var, lang, selected, input_lang, pro, tran):
    global frame, translate_frame

    if frame: frame.destroy()
    frame = tk.Frame(text_container)
    frame.pack(pady=(5, 5))

    if input_lang == "Chinese":
        for i, char in enumerate(text_var.get()):
            if pro == False:
                pinyin_char = ""
            else:
                pinyin_char = pinyin(char, style=Style.TONE)[0][0]
            lb_py = tk.Label(frame, text = pinyin_char, font=("Arial", 10), fg="blue")
            lb_py.grid(row=0, column=i, padx=2, pady=5)
            lb_char = tk.Label(frame, text=char, font=("SimSun", 14, "bold"),  fg="red")
            if i in selected:
                lb_char.config(bg="lightblue")
            lb_char.grid(row=1, column=i, padx=2)
           
    else:
        list_chars = text_var.get().split()
        for i, char in enumerate(list_chars):
            if pro == False:
                ipa_char = ''
            else:
                ipa_char = ipa.convert(char)
            lb_ipa = tk.Label(frame, text=ipa_char, font=("Arial", 10, "italic"), fg="blue")
            lb_ipa.grid(row=0, column=i, padx=2, pady=5)
            lb_char = tk.Label(frame, text=char, font=("Arial", 12, "bold"),  fg="red")
            if i in selected:
                lb_char.config(bg="lightblue")
            lb_char.grid(row=1, column=i, padx=2)



    if translate_frame: translate_frame.destroy()
    translate_frame = tk.Frame(text_container)
    translate_frame.pack(pady=(5, 5))

    if text_var.get() == "今天是星期一，我感觉充满能量" or lang == "None" or tran==False:
        tk.Label(translate_frame, text = "", font=("Arial", 12)).pack(pady=(0,5))
    else:
        try:
            if input_lang == "Chinese":
                source = "zh-CN"
            else:
                source = "en"


            if lang == "English":
                target = "en"
            elif lang == "Chinese":
                target = "zh-CN"
            else:
                target = "vi"

            if source == target:
                tk.Label(translate_frame, text = "", font=("Arial", 12)).pack(pady=(0,5))
            else:
                translator = GoogleTranslator(source=source, target=target)
                translator_result = translator.translate(text_var.get())
                tk.Label(translate_frame, text = translator_result, font=("Arial", 12)).pack(pady=(0,5))

        except requests.exceptions.RequestException as e:
            print("An error occurred:", e)
            tk.Label(translate_frame, text = "", font=("Arial", 12)).pack(pady=(0,5))
