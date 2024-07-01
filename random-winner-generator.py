import tkinter as tk
import random


def my_pick_winner():
    my_students_list = my_students_entry.get("1.0", tk.END).splitlines()
    my_students_list = [my_student for my_student in my_students_list if my_student]
    if my_students_list:
        my_winner = random.choice(my_students_list)
        my_winner_label.config(text=f"Congratulations, {my_winner}!")
    else:
        my_winner_label.config(text="Please enter at least one student name.")


my_window = tk.Tk()
my_window.title("Random Winner Generator")

my_instructions_label = tk.Label(my_window, text="Enter student names (one per line):")
my_instructions_label.pack()

my_students_entry = tk.Text(my_window, height=10, width=30)
my_students_entry.pack()

my_pick_button = tk.Button(my_window, text="Pick a Winner", command=my_pick_winner)
my_pick_button.pack()


my_winner_label = tk.Label(my_window, text="")
my_winner_label.pack()

my_window.mainloop()
