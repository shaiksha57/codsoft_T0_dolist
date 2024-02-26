# from tkinter import *
# from tkinter import ttk

# class todo:
#     def __init__(self,root):
#         self.root = root 
#         self.root.title("To-do-list")
#         self.root.geometry('650x410+300+150')

#         self.label = Label(self.root,text='To-Do-List-App',font='ariel, 25',width=10,bd=5,bg='orange',fg='black')
#         self.label.pack(side='top',fill=BOTH)

#         self.label2 = Label(self.root,text='Add Task',font='ariel,18',width=10,bd=5,bg='orange',fg='black')
#         self.label2.place(x=40,y=54)


#         self.label3=Label(self.root,text='Tasks',font='ariel,18',width=10,bd=5,bg='orange',fg='black')
#         self.label3.place(x=320,y=54)

#         self.main_text=Listbox(self.root,height=9,bd=5,width=23,font='ariel,20')
#         self.main_text.place(x=300,y=100)

#         self.text=Text(self.root,bd=5,height=2,width=30,font='ariel,10')
#         self.text.place(x=10,y=100)

#         def add():
#             content = self.text.get(1.0,END)
#             self.main_text.insert(END,content)
#             with open('data.txt','a') as file:
#                 file.write(content)
#                 file.seek(0)
#                 file.close()
#             self.text.delete(1.0,END)
#         def delete():
#             delete_ = self.main_text.curselection()
#             look = self.main_text.get(delete_)
#             with open('data.txt','r+') as f:
#                 new_f = f.readlines()
#                 f.seek(0)
#                 for line in new_f:
#                     item = str(look)
#                     if item not in line:
#                         f.write(line)
#                 f.truncate()
#             self.main_text.delete(delete_)


    
# def main():
#     root = Tk()
#     ui=todo(root)
#     root.mainloop()

# if __name__=="__main__":
#     main()


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
