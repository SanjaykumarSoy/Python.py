import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import qrcode

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

    # Create a QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(message)
    qr.make(fit=True)

    # Save the QR code as an image
    img = qr.make_image(fill='black', back_color='white')
    img.save('birthday_qr.png')

    # Display the QR code
    root.destroy()
    img.show()

get_birthday_message()
