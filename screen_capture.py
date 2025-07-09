import tkinter as tk
import pyautogui
import numpy as np
import time


# Define a function to capture a screen region with multiple callbacks and processing steps
def capture_screen_region(window, label_text, show_text, handle_coords, predict_text):
    # Define an inner class to handle screen capturing logic
    class ScreenCapture:
        def __init__(self):
            # Initialize starting x and y coordinates as None
            self.start_x = self.start_y = None

            # Create a new top-level transparent fullscreen window over 'window'
            self.root = tk.Toplevel(window)
            self.root.attributes("-fullscreen", True)  # Make it fullscreen
            self.root.attributes("-alpha", 0.3)        # Set window transparency
            self.root.config(bg="gray")                # Set background color to gray

            # Create a canvas for drawing the selection rectangle
            self.canvas = tk.Canvas(self.root, cursor="cross")  # Use cross cursor
            self.canvas.pack(fill=tk.BOTH, expand=True)         # Expand to fill window

            # Initialize rectangle variable
            self.rect = None

            # Bind mouse events to functions
            self.canvas.bind("<ButtonPress-1>", self.on_press)     # Left mouse press
            self.canvas.bind("<B1-Motion>", self.on_drag)          # Mouse drag with button 1
            self.canvas.bind("<ButtonRelease-1>", self.on_release) # Left mouse release

            # Start the event loop for this top-level window
            self.root.mainloop()

        # Event handler when mouse button is pressed
        def on_press(self, event):
            self.start_time = time.time()  # Record start time for performance tracking
            self.start_x = self.canvas.canvasx(event.x)  # Record x coordinate on canvas
            self.start_y = self.canvas.canvasy(event.y)  # Record y coordinate on canvas
            # Create a rectangle starting and ending at the same point initially
            self.rect = self.canvas.create_rectangle(
                self.start_x, self.start_y,
                self.start_x, self.start_y,
                outline="red"  # Rectangle border color
            )

        # Event handler when mouse is dragged with button pressed
        def on_drag(self, event):
            cur_x = self.canvas.canvasx(event.x)  # Current x position
            cur_y = self.canvas.canvasy(event.y)  # Current y position
            # Update rectangle coordinates dynamically while dragging
            self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

        # Event handler when mouse button is released
        def on_release(self, event):
            end_x = self.canvas.canvasx(event.x)  # Record final x
            end_y = self.canvas.canvasy(event.y)  # Record final y

            self.root.destroy()  # Close the fullscreen capture window

            # Calculate top-left (x1,y1) and bottom-right (x2,y2) coordinates
            x1, y1 = min(self.start_x, end_x), min(self.start_y, end_y)
            x2, y2 = max(self.start_x, end_x), max(self.start_y, end_y)

            # Take screenshot of the selected region
            img = pyautogui.screenshot(region=(int(x1), int(y1), int(x2 - x1), int(y2 - y1)))

            # Convert screenshot to numpy array in RGB format
            img_np = np.array(img.convert("RGB"))

            # Perform text prediction using the passed predict_text function
            text = predict_text(img_np)

            # Update label_text and call show_text function in the main window thread
            window.after(0, lambda: (label_text.set(text), show_text(label_text)))

            # Call handle_coords function with captured coordinates
            handle_coords(x1, y1, x2, y2)

            # Print completion time
            print(f"✅ OCR completed in {time.time() - self.start_time:.2f}s")
    
    # Instantiate and run the ScreenCapture class
    ScreenCapture()