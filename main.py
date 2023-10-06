import tkinter as tk
from tkinter import Menu, messagebox, filedialog, colorchooser, simpledialog

root = tk.Tk()
root.title("Tkinter app template")


def new_file():
    pass


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            # Add your logic for opening a file here
            file_contents = file.read()
            print(file_contents)


def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            # Add your logic for opening a file here
            file_contents = "This is some example data that you can save."
            file.write(file_contents)


# Create a function to handle the "Exit" menu item
def exit_app():
    root.quit()


def cut():
    # Add your cut logic here
    pass


# Create a function to handle the "Copy" menu item
def copy():
    # Add your copy logic here
    pass


# Create a function to handle the "Paste" menu item
def paste():
    # Add your paste logic here
    pass


def show_info():
    messagebox.showinfo("Info", "This is an info message!")


def show_error():
    messagebox.showerror("Error", "This is an error message!")


def show_warning():
    messagebox.showwarning("Warning", "This is a warning message!")


def show_question():
    messagebox.askquestion("Question", "This is a question message!")


def show_cancel():
    messagebox.askokcancel("Cancel", "This is a cancel message!")


def show_yesno():
    messagebox.askyesno("YesNo", "This is a yesno message!")


def show_retrycancel():
    messagebox.askretrycancel("RetryCancel", "This is a retrycancel message!")


def float_dialog():
    result = simpledialog.askfloat("Input", "Enter a floating-point number:")
    if result is not None:
        print(f"Entered Float: {result}")


def choose_color():
    color = colorchooser.askcolor(title="Choose a Color")
    if color[1]:  # Check if a color was selected
        selected_color = color[1]
        print(f"Selected Color: {selected_color}")


def open_help_window():
    pass


# Function to open the "About" window
def open_about_window():
    about_window = tk.Toplevel(root)
    about_window.title("About This App")

    # Set the size of the "About" window
    about_window.geometry("500x500")

    about_text = ("Author: Ondřej Hasník\nVersion: 2023.10.06\n \nThis software is licensed under ondhas SOFTWARE\n"
                  "OpenSource License (OSOSL)")

    label = tk.Label(about_window, text=about_text, padx=20, pady=20)
    label.pack()

    # Calculate the center position of the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = about_window.winfo_reqwidth()
    window_height = about_window.winfo_reqheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Set the "About" window's position
    about_window.geometry(f"+{x}+{y}")


menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

edit_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

message_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Messageboxes", menu=message_menu)
message_menu.add_command(label="Info", command=show_info)
message_menu.add_command(label="Error", command=show_error)
message_menu.add_command(label="Warning", command=show_warning)
message_menu.add_command(label="Question", command=show_question)
message_menu.add_command(label="Cancel", command=show_cancel)
message_menu.add_command(label="YesNo", command=show_yesno)
message_menu.add_command(label="RetryCancel", command=show_retrycancel)

dialog_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Dialogs", menu=dialog_menu)
dialog_menu.add_command(label="Float", command=float_dialog)
dialog_menu.add_command(label="Colors", command=choose_color)

about_menu = Menu(menu_bar)
menu_bar.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="Help", command=open_help_window)
about_menu.add_command(label="About", command=open_about_window)

# Start the Tkinter main loop
root.mainloop()
