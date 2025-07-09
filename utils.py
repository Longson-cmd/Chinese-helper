captured_coords = None

def handle_coords(x1, y1, x2, y2):
    global captured_coords
    captured_coords = (x1, y1, x2, y2)
    print(f"Coordinates saved: ({x1}, {y1}), ({x2}, {y2})")

def get_saved_coords():
    global captured_coords
    return captured_coords