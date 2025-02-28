import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk



# Function to create the GUI with background image



def create_gui_with_background():
    # Create main window

    root = tk.Tk()
    root.title("User/Admin Options")


    # Load background image
    background_image = Image.open("bgg.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    # Create canvas to display background image
    canvas = tk.Canvas(root, width=background_image.width, height=background_image.height)
    canvas.pack(fill="both", expand=True)

    # Place the background image on the canvas
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # Calculate the center coordinates of the canvas
    canvas_center_x = background_image.width // 2
    canvas_center_y = background_image.height // 2

    # Create welcome labels
    welcome_label = tk.Label(root, text="Welcome!", font=("Helvetica", 24), bg="white")
    welcome_label_window = canvas.create_window(canvas_center_x, canvas_center_y - 150, anchor="center", window=welcome_label)

    def user_option():
        root.destroy()
        import loginpage

    def admin_option():
        root.destroy()
        import adminlogin


    # Create buttons for user and admin options at the center of the canvas
    user_button = tk.Button(root, text="User Login", command=user_option, font=("Helvetica", 14))
    user_button_window = canvas.create_window(canvas_center_x, canvas_center_y - 50, anchor="center", window=user_button)

    admin_button = tk.Button(root, text="Admin Login", command=admin_option, font=("Helvetica", 14))
    admin_button_window = canvas.create_window(canvas_center_x, canvas_center_y + 50, anchor="center", window=admin_button)

    # Run the main event loop
    root.mainloop()


# Call the function to create GUI with background image
create_gui_with_background()