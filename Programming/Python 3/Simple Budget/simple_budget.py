import tkinter as tk
import pickle
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime

# Function to save budget data to a file
def save_budget_data(data, filename):
    try:
        with open(filename, "wb") as file:
            pickle.dump(data, file)
            messagebox.showinfo("File Saved", "Budget data saved successfully.")
    except IOError:
        messagebox.showerror("Save Error", "An error occurred while saving the file.")

# Function to load budget data from a file
def load_budget_data(filename):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}
    except IOError:
        messagebox.showerror("Load Error", "An error occurred while loading the file.")

# Function to handle calculate button click event
def calculate_budget():
    income = income_entry.get()
    expenses = expenses_entry.get()
    try:
        income = float(income)
        expenses = float(expenses)
        savings = income - expenses
        savings_label.configure(text="Savings: $%.2f" % savings)

        # Save the budget data
        budget_data = {"income": income, "expenses": expenses, "savings": savings}
        save_budget_data(budget_data, current_file)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter numeric values for income and expenses.")

# Function to handle save button click event
def save_file():
    filename = filedialog.asksaveasfilename(defaultextension=".pkl")
    if filename:
        save_budget_data({}, filename)

# Function to handle open button click event
def open_file():
    global current_file
    filename = filedialog.askopenfilename(filetypes=[("Pickle files", "*.pkl")])
    if filename:
        current_file = filename
        budget_data = load_budget_data(filename)
        income_entry.delete(0, tk.END)
        expenses_entry.delete(0, tk.END)
        income_entry.insert(0, str(budget_data.get("income", "")))
        expenses_entry.insert(0, str(budget_data.get("expenses", "")))
        savings_label.configure(text="Savings: $%.2f" % budget_data.get("savings", 0.0))

root = tk.Tk()
root.title("Simple Budget")

# Add some styling
root.configure(bg="#f2f2f2")
root.geometry("300x200")

title_label = tk.Label(root, text="Simple Budget", font=("Arial", 16, "bold"), fg="#333333", bg="#f2f2f2")
title_label.pack(pady=10)

month_year = datetime.now().strftime("%B %Y")
month_year_label = tk.Label(root, text=month_year, font=("Arial", 12, "bold"), fg="#000000", bg="#f2f2f2")
month_year_label.place(x=10, y=10)

income_frame = tk.Frame(root, bg="#f2f2f2")
income_frame.pack()

income_label = tk.Label(income_frame, text="Income:", font=("Arial", 12), fg="#333333", bg="#f2f2f2")
income_label.pack(side="left", padx=5)

income_entry = tk.Entry(income_frame, font=("Arial", 12))
income_entry.pack(side="left")

expenses_frame = tk.Frame(root, bg="#f2f2f2")
expenses_frame.pack()

expenses_label = tk.Label(expenses_frame, text="Expenses:", font=("Arial", 12), fg="#333333", bg="#f2f2f2")
expenses_label.pack(side="left", padx=5)

expenses_entry = tk.Entry(expenses_frame, font=("Arial", 12))
expenses_entry.pack(side="left")

calculate_button = tk.Button(root, text="Calculate", font=("Arial", 12, "bold"), fg="#ffffff", bg="#4287f5", command=calculate_budget)
calculate_button.pack(pady=10)

savings_label = tk.Label(root, text="Savings:", font=("Arial", 12, "bold"), fg="#333333", bg="#f2f2f2")
savings_label.pack()

save_button = tk.Button(root, text="Save", font=("Arial", 12), fg="#ffffff", bg="#4287f5", command=save_file)
save_button.pack(side="left", padx=10)

open_button = tk.Button(root, text="Open", font=("Arial", 12), fg="#ffffff", bg="#4287f5", command=open_file)
open_button.pack(side="left")

# Set the initial current file to an empty string
current_file = ""

root.mainloop()
