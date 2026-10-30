
import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get().strip()

    if task:
        tasks.append({"name": task, "completed": False})
        task_entry.delete(0, tk.END)
        display_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def display_tasks():
    task_list.delete(0, tk.END)

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        task_list.insert(
            tk.END, f"{i}. {task['name']} - {status}"
        )

def complete_task():
    selected = task_list.curselection()

    if selected:
        index = selected[0]
        tasks[index]["completed"] = True
        display_tasks()
    else:
        messagebox.showwarning("Warning", "Select a task first!")

def delete_task():
    selected = task_list.curselection()

    if selected:
        index = selected[0]
        tasks.pop(index)
        display_tasks()
    else:
        messagebox.showwarning("Warning", "Select a task first!")

# Create main window
root = tk.Tk()
root.title("My To-Do List")
root.geometry("500x550")
root.configure(bg="#eaf2f8")

# Heading
heading = tk.Label(
    root,
    text="MY TO-DO LIST",
    font=("Arial", 22, "bold"),
    bg="#eaf2f8",
    fg="#154360"
)
heading.pack(pady=20)

# Task entry
task_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=30
)
task_entry.pack(pady=10)

# Add button
tk.Button(
    root,
    text="Add Task",
    command=add_task,
    bg="#2874a6",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20
).pack(pady=5)

# Task list
task_list = tk.Listbox(
    root,
    font=("Arial", 12),
    width=45,
    height=12,
    selectmode=tk.SINGLE
)
task_list.pack(pady=15)

# Complete button
tk.Button(
    root,
    text="Complete Task",
    command=complete_task,
    bg="#239b56",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20
).pack(pady=5)

# Delete button
tk.Button(
    root,
    text="Delete Task",
    command=delete_task,
    bg="#c0392b",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20
).pack(pady=5)

# Run application
root.mainloop()
