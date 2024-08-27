import tkinter as tk
from tkinter import messagebox

# Initialize the task list
tasks = []

# Functions for task management
def add_task():
    task = entry_task.get()
    if task:
        tasks.append({"task": task, "completed": False})
        entry_task.delete(0, tk.END)
        update_task_listbox()
        messagebox.showinfo("Success", "Task added successfully")
    else:
        messagebox.showwarning("input Error", "Please enter a task")

def mark_task_completed():
    selected_task_index = listbox_tasks.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        tasks[task_index]["completed"] = True
        update_task_listbox()
        messagebox.showinfo("Success", "Task marked as completed")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed")

def view_tasks():
    update_task_listbox()

def update_task_listbox():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        status = "✔️" if task["completed"] else "❌"
        listbox_tasks.insert(tk.END, f"{task['task']} {status}")

def quit_program():
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Task Manager")

frame = tk.Frame(root)
frame.pack(pady=10)

entry_task = tk.Entry(frame, width=40)
entry_task.grid(row=0, column=0, padx=5)

button_add_task = tk.Button(frame, text="Add Task", command=add_task)
button_add_task.grid(row=0, column=1, padx=5)

listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.pack(pady=10)

button_view_tasks = tk.Button(root, text="View Tasks", command=view_tasks)
button_view_tasks.pack(pady=5)

button_mark_completed = tk.Button(root, text="Mark Task as Completed", command=mark_task_completed)
button_mark_completed.pack(pady=5)

button_quit = tk.Button(root, text="Quit", command=quit_program)
button_quit.pack(pady=5)

# Start the GUI loop
root.mainloop()
