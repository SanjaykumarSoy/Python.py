import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

def get_birthday_message():
    # Initialize the root window
    root = tk.Tk()
    root.title("Birthday Wishes")
    root.geometry("800x600")

    # Get user inputs using simpledialog
    name = simpledialog.askstring("Input", "Enter the person's name:", parent=root)
    age = simpledialog.askstring("Input", "Enter the person's age:", parent=root)
    sender_name = simpledialog.askstring("Input", "Enter your name:", parent=root)

    if not name or not age or not sender_name:  # Exit if name or age is not provided
        messagebox.showwarning("Input Error", "Please provide all fields.")
        root.destroy()
        return

    # Biblical birthday message
    message = (f"Happy Birthday to you, {name}! May the Lord bless you and keep you; may His face shine upon you and be gracious to you; may the Lord lift up His countenance upon you and give you peace. (Numbers 6:24-26) Wishing you a day filled with joy, love, and celebration. Love, {sender_name}")

    # Create a new message box with the birthday message
    new_root = tk.Toplevel(root)
    new_root.title("Birthday Wishes")
    new_root.geometry("800x600")

    # Create a canvas to draw the animation
    canvas = tk.Canvas(new_root, width=800, height=600)
    canvas.pack(fill="both", expand=True)

    # Create a pastel background
    canvas.create_rectangle(0, 0, 800, 600, fill="#C9E4CA")

    # Create the birthday message text with an italic font and darker color
    try:
        font_name = "Arial Italic"
        words = canvas.create_text(400, 300, text=message, font=(font_name, 24), fill="#333333", width=600)
    except tk.TclError:  # Fallback if the font isn't available
        words = canvas.create_text(400, 300, text=message, font=("Arial", 24, "italic"), fill="#333333", width=600)

    # Update the canvas to display the text
    new_root.update_idletasks()

    # Run the tkinter main loop
    new_root.mainloop()

get_birthday_message()
