import tkinter as tk  # Import the tkinter library and give it an alias 'tk'
from tkinter import messagebox  # Import the messagebox module from tkinter for showing popup messages


def add_menu(root):
    def show_help():  # Define a function to show help information
        messagebox.showinfo(
                "Help",
                "Here’s how to use the app:\n\n"
                "    1. Press Shift + z to capture text areas."
                "(if the background don't turn gray, click to the 'feather' icon on Windows taskbar.)\n"
                "    2. Click 'Use saved coords' to capture text from previous area."
                "(designed for subtitle videos).\n"
                "    3. Use 'Open Edit Window' to modify the text.\n"
                "    4. Click important word directly before saving.\n\n"
                "Note: Each text is saved in 30 days."
        )
        # Display an informational message box with help instructions

    def show_about():  # Define a function to show about information
        messagebox.showinfo("About", 
                            "Support learning languages app v1.0.\n\n"
                            "Created by Steve Nguyen.\n\n"
                            "© 2025 No copyright.")
        # Display an informational message box with app version and credits

    # Create a menu bar
    menu_bar = tk.Menu(root)  # Create a Menu widget and attach it to the root window

    # Help menu
    help_menu = tk.Menu(menu_bar, tearoff=0)  # Create a submenu for Help with no tear-off option
    help_menu.add_command(label="How to Use", command=show_help)  # Add a menu item that calls show_help when clicked
    help_menu.add_separator()  # Add a separator line between menu items
    help_menu.add_command(label="About", command=show_about)  # Add a menu item that calls show_about when clicked

    # Add the Help menu to the menu bar
    menu_bar.add_cascade(label="Help", menu=help_menu)  # Add the Help submenu to the main menu bar under the label "Help"

    # Configure the window to use the menu bar
    root.config(menu=menu_bar)  # Set the window's menu bar to the one we created










# import tkinter as tk  # Import the tkinter library and give it an alias 'tk'
# from tkinter import messagebox  # Import the messagebox module from tkinter for showing popup messages

# def show_help():  # Define a function to show help information
#     messagebox.showinfo("Help", "Here’s how to use the app:\n\n1. Open the app.\n2. Click 'Next' to view items.\n3. Use other controls as needed.")
#     # Display an informational message box with help instructions

# def show_about():  # Define a function to show about information
#     messagebox.showinfo("About", "My App v1.0\nCreated by Your Name\n© 2025 All rights reserved.")
#     # Display an informational message box with app version and credits

# root = tk.Tk()  # Create the main application window
# root.title("My App")  # Set the title of the application window

# # Create a menu bar
# menu_bar = tk.Menu(root)  # Create a Menu widget and attach it to the root window

# # Help menu
# help_menu = tk.Menu(menu_bar, tearoff=0)  # Create a submenu for Help with no tear-off option
# help_menu.add_command(label="How to Use", command=show_help)  # Add a menu item that calls show_help when clicked
# help_menu.add_separator()  # Add a separator line between menu items
# help_menu.add_command(label="About", command=show_about)  # Add a menu item that calls show_about when clicked

# # Add the Help menu to the menu bar
# menu_bar.add_cascade(label="Help", menu=help_menu)  # Add the Help submenu to the main menu bar under the label "Help"

# # Configure the window to use the menu bar
# root.config(menu=menu_bar)  # Set the window's menu bar to the one we created

# root.mainloop()  # Start the Tkinter event loop (keep the window open and responsive)


# # tk.Menu(root) creates a Menu object linked to the root window. But nothing is shown yet.

# # root.config(menu=menu_bar) assigns that menu as the visible top-level menu of the window.
# # Without this line, the menu bar will not appear in the GUI, even though you've created it.