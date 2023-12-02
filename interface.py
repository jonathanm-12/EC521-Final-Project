import tkinter as tk
from tkinter import scrolledtext
from scan import fetch_github_data  # Importing the function

root = tk.Tk()
root.title("GitHub Repository Viewer")

output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
output_area.pack(pady=10)

fetch_button = tk.Button(root, text="Fetch GitHub Data", command=lambda: fetch_github_data(output_area))
fetch_button.pack()

root.mainloop()
