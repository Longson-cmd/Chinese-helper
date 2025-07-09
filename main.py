import tkinter as tk
import keyboard
from screen_capture import capture_screen_region
from edit_window import open_edit_window
from utils import handle_coords, get_saved_coords
import pyautogui
import numpy as np
from paddleocr import PaddleOCR
from show import show_text
from save_words import save
from review import review_words
import os
import json
import time
import traceback
from menu import add_menu

import paddlex.utils.deps
paddlex.utils.deps.require_extra = lambda *args, **kwargs: None

# ========================================
# 📁 Initialization: File Paths and JSON Setup
# ========================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "new_words.json")

if not os.path.exists(JSON_PATH):
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump({
            "Chinese": [], "English": []
        }, f, ensure_ascii=False, indent=4)


# ========================================
# 🖼️ Initialize Main Window and UI Options
# ========================================
window = tk.Tk()
add_menu(window) 
navbar = tk.Frame(window)
navbar.pack(fill="x", pady=10, padx=10)

# ---------- Translation Language Option ----------
options = ["None", "English", "Vietnamese", "Chinese"]
lang = tk.StringVar()
lang.set(options[2])  # Default to Vietnamese
tk.Label(navbar, text="Translation: ", fg="blue").pack(side="left")
option_translation = tk.OptionMenu(navbar, lang, *options)
option_translation.pack(side="left")
option_translation.config(bg=window.cget("bg"), highlightthickness=0, bd=0, fg="red")

# ---------- Input Language Option ----------
input_lang = tk.StringVar()
input_options = ["English", "Chinese"]
input_lang.set(input_options[1])  # Default to Chinese
option_language = tk.OptionMenu(navbar, input_lang, *input_options)
option_language.pack(side="right")
tk.Label(navbar, text="Language: ", fg="blue").pack(side="right")
option_language.config(bg=window.cget("bg"), highlightthickness=0, bd=0, fg="red")

# ---------- Window Title and Default Text ----------
window.title("Languages Helper")
label_text = tk.StringVar(value="今天是星期一，我感觉充满能量")

# ---------- Text Display Frame ----------
text_container = tk.Frame(window)
text_container.pack(pady=(5, 5))

hightlight = show_text(text_container, label_text, lang.get(), input_lang.get())

def update_hightlight_and_show(text_var):
    global hightlight 
    hightlight = show_text(text_container, text_var, lang.get(), input_lang.get())


# ========================================
# 🔍 OCR Model Initialization
# ========================================
ocr = PaddleOCR(
    text_detection_model_name="PP-OCRv5_mobile_det",
    text_recognition_model_name="PP-OCRv5_mobile_rec",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
    cpu_threads=8,
    lang="ch" if input_lang.get() == "Chinese" else "en"
)

def predict_text(img_np):
    result = ocr.predict(img_np)
    all_texts = ''
    for res in result:
        text = " ".join(res["rec_texts"])
        if input_lang.get() == "Chinese":
            all_texts += text
        else:
            all_texts += " " + text
    return all_texts


# ========================================
# 🚀 Main UI Setup and Event Bindings
# ========================================
def main():
    # ---------- Button Area ----------
    button_container = tk.Frame(window)
    button_container.pack(pady=(5, 5))

    tk.Button(button_container, text="Open Edit Window", command=lambda: open_edit_window(window, label_text, lambda label_text: update_hightlight_and_show(label_text))).grid(row=0, column=0, padx=10, pady=(5, 5))
    tk.Button(button_container, text="Use Saved Coords", command=lambda: use_saved_coords()).grid(row=0, column=1, padx=10, pady=(5, 5))
    tk.Button(button_container, text="Save", command=lambda: save(label_text.get(), hightlight, input_lang.get())).grid(row=0, column=2, padx=10, pady=(5, 5))
    tk.Button(button_container, text="Review", command=lambda: review_words(window, input_lang.get())).grid(row=0, column=3, padx=10, pady=(5, 5))

    # ---------- Keyboard Hotkeys ----------
    keyboard.add_hotkey('shift+z', lambda: window.after(0, lambda: capture_screen_region(window, label_text, lambda label_text: update_hightlight_and_show(label_text), handle_coords, predict_text)))
    keyboard.add_hotkey('esc', lambda: window.after(0, window.destroy))

    # ---------- Execution Time Display ----------
    time_container = tk.Frame(window)
    time_container.pack(pady=(5, 5), anchor="w", padx=3)
    time_label = None
    time_ocr = None

    def show_time():
        nonlocal time_label, time_ocr
        if time_label: time_label.destroy()
        time_label = tk.Label(time_container, text=f"Executed: {time_ocr}", fg="blue")
        time_label.grid(row=0, column=0, sticky="w")

    # ---------- Use Saved Coords Function ----------
    def use_saved_coords():
        nonlocal time_ocr
        coords = get_saved_coords()
        if coords:
            start_time = time.time()
            x1, y1, x2, y2 = coords
            img = pyautogui.screenshot(region=(int(x1), int(y1), int(x2 - x1), int(y2 - y1)))
            img_np = np.array(img.convert("RGB"))
            all_texts = predict_text(img_np)
            label_text.set(all_texts)
            update_hightlight_and_show(label_text)
            time_ocr = f"{time.time() - start_time:.2f}s"
            show_time()
            print(f"✅ OCR completed in {time_ocr}")
        else:
            print("No coordinates saved.")

    # ---------- Final Window Settings ----------
    window.geometry("700x250+500+200")
    window.attributes("-topmost", True)
    window.mainloop()


# ========================================
# 🧪 Run Main Safely with Error Logging
# ========================================
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        with open("error_log.txt", "w", encoding="utf-8") as f:
            f.write(traceback.format_exc())




# pyinstaller main.py `
#   --hidden-import=paddle.fluid.proto.framework_pb2 `
#   --hidden-import=layoutparser  `
#   --hidden-import=pdf2image  `
#   --hidden-import=paddleocr `
#   --collect-all paddle `
#   --collect-all paddleocr `
#   --collect-all cv2 `
#   --collect-all paddlex `
#   --collect-all pypdfium2 `
#   --collect-all shapely `
#   --collect-all pyclipper `
#   --add-data "C:\Users\PC\anaconda3\envs\paddle\Lib\site-packages\paddlex\.version;paddlex"


# pyinstaller --onefile --noconsole main.py `
# pyinstaller --onedir --noconsole main.py `
#   --hidden-import=paddle.fluid.proto.framework_pb2 `
#   --hidden-import=layoutparser  `
#   --hidden-import=pdf2image  `
#   --hidden-import=paddleocr `
#   --collect-all paddle `
#   --collect-all paddleocr `
#   --collect-all cv2 `
#   --collect-all paddlex `
#   --collect-all pypdfium2 `
#   --collect-all shapely `
#   --collect-all pyclipper `
#   --add-data "C:\Users\PC\anaconda3\envs\paddle\Lib\site-packages\paddlex\.version;paddlex"


