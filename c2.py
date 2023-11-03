import tkinter as tk
import random

def select_action():
    a = color_var.get()
    b = number_var.get()
    random_number = random.randint(0, 1)

    result_label.config(text="")  # Clear previous result

    if a == "Blue":
        if b == "4" and random_number == 1:
            result_label.config(text="choosen Dare")
        elif b == "4" and random_number == 0:
            result_label.config(text="choosen Truth")
        elif b == "8":
            result_label.config(text="Random Result: " + str(random_number))
    elif a == "Red":
        if b == "4" and random_number == 1:
            result_label.config(text="do 50 pushups")
        elif b == "4" and random_number == 0:
            result_label.config(text="do 50 situps")
        elif b == "8":
            result_label.config(text="Random Result: " + str(random_number))
    elif a == "1":
        exit

window = tk.Tk()
window.title("Dare or Truth")


color_label = tk.Label(window, text="Choose a color:")
color_label.pack()

color_var = tk.StringVar()
color_var.set("Blue") 
color_menu = tk.OptionMenu(window, color_var, "Blue", "Red")
color_menu.pack()

number_label = tk.Label(window, text="Choose a number:")
number_label.pack()

number_var = tk.StringVar()
number_var.set("4") 
number_menu = tk.OptionMenu(window, number_var, "4", "8")
number_menu.pack()

result_label = tk.Label(window, text="", fg="blue")
result_label.pack()

action_button = tk.Button(window, text="Get Result", command=select_action)
action_button.pack()

window.mainloop()
