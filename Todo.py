
import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Initialize Tkinter
root = tk.Tk()
root.title("To-Do List")

# Task Entry
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Add Task Button
add_button = tk.Button(root, text="Add Task", bg='orange',command=add_task)
add_button.pack()

# Task List
task_listbox = tk.Listbox(root, width=50)
task_listbox.pack(pady=10)

# Delete Task Button
delete_button = tk.Button(root, text="Delete Task",bg='orange', command=delete_task)
delete_button.pack()

# Run the Tkinter event loop
root.mainloop()
