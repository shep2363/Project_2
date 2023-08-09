import os
import tkinter as tk
from tkinter import filedialog

def process_files():
    root_dir = entry.get()

    if not os.path.isdir(root_dir):
        status_label.config(text="Invalid directory. Please enter a valid directory path.")
        return

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".nc"):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, "r") as file:
                    text = file.readlines()

                if len(text) >= 5:
                    text[2], text[4] = text[4], text[2]

                    with open(file_path, "w") as file:
                        file.writelines(text)
                else:
                    print(f"File {file_path} does not have at least 5 lines of text and cannot be processed.")
    status_label.config(text="Processing complete!")

def browse_directory():
    root_dir = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, root_dir)

# Create the main application window
app = tk.Tk()
app.title("NC Files Processor")

# Create a label, entry field, and buttons
label = tk.Label(app, text="Enter the root directory containing the nc files:")
entry = tk.Entry(app, width=50)
browse_button = tk.Button(app, text="Browse", command=browse_directory)
process_button = tk.Button(app, text="Process Files", command=process_files)
status_label = tk.Label(app, text="")

# Arrange the widgets using the grid layout
label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
entry.grid(row=1, column=0, padx=10)
browse_button.grid(row=1, column=1, padx=10)
process_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
status_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the main event loop
app.mainloop()
