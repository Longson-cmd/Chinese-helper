# main.py
import tkinter as tk
from menu import add_menu  # Import the function from your file

def main():
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("500x400")

    add_menu(root)  # Add the menu to this window

    tk.Label(root, text="Main Window Content", font=("Arial", 16)).pack(pady=50)

    root.mainloop()

if __name__ == "__main__":
    main()

# import tkinter as tk
# from tkinter import font

# root = tk.Tk()

# # List all available font families
# available_fonts = list(font.families())
# available_fonts.sort()

# # Print or search for a specific font
# print("Charis SIL" in available_fonts)  # True if available
# print(available_fonts)  # See the full list
