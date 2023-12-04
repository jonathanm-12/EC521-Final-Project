import tkinter as tk
from tkinter import ttk
import random

# Function to simulate scanning and generate fake results
def scan():
    username = username_entry.get()
    ml_test = ml_var.get()
    entropy_test = entropy_var.get()
    regex_test = regex_var.get()

    # Simulating fake repositories
    fake_repositories = ["Repo1", "Repo2", "Repo3"]

    # Generating fake scan results for each repository
    results = [f"Scanning GitHub repositories of {username}..."]
    for repo in fake_repositories:
        results.append(f"\nResults for {repo}:")
        if ml_test:
            results.append(f"  ML Test: {random.randint(0, 100)} API Keys detected")
        if entropy_test:
            results.append(f"  Entropy Test: {random.randint(0, 100)} API Keys detected")
        if regex_test:
            results.append(f"  Regex Test: {random.randint(0, 100)} API Keys detected")

    # Displaying the results
    result_text = "\n".join(results) if results else "No tests selected"
    result_label.config(text=result_text)
    print(result_text)

# Create the main window
root = tk.Tk()
root.title("GitHub Scanning Tool")

# Create a frame for the input fields
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# GitHub username entry
username_label = ttk.Label(frame, text="GitHub Username:")
username_label.grid(row=0, column=0, sticky=tk.W)
username_entry = ttk.Entry(frame, width=30)
username_entry.grid(row=0, column=1)

# Variables for the checkbuttons
ml_var = tk.BooleanVar()
entropy_var = tk.BooleanVar()
regex_var = tk.BooleanVar()

# Test options (ML, Entropy, Regex)
ml_check = ttk.Checkbutton(frame, text="Machine Learning (ML) Test", variable=ml_var)
ml_check.grid(row=1, column=0, columnspan=2, sticky=tk.W)
entropy_check = ttk.Checkbutton(frame, text="Entropy Test", variable=entropy_var)
entropy_check.grid(row=2, column=0, columnspan=2, sticky=tk.W)
regex_check = ttk.Checkbutton(frame, text="Regex Test", variable=regex_var)
regex_check.grid(row=3, column=0, columnspan=2, sticky=tk.W)

# Scan button
scan_button = ttk.Button(frame, text="Scan", command=scan)
scan_button.grid(row=4, column=0, columnspan=2)

# Label for displaying results
result_label = ttk.Label(frame, text="")
result_label.grid(row=5, column=0, columnspan=2)

# Start the GUI
root.mainloop()
