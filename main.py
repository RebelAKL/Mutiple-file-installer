import os
import subprocess
import tkinter as tk
from tkinter import filedialog

def install_files(files):
    for file in files:
        try:
            subprocess.run(file, shell=True, check=True)
            print(f"Successfully installed: {file}")
        except subprocess.CalledProcessError as e:
            print(f"Error installing {file}: {e}")

def select_files():
    files = filedialog.askopenfilenames(filetypes=[("Executable files", "*.exe")])
    if files:
        install_files(files)

# Create the main window
root = tk.Tk()
root.title("Multiple EXE Installer")

# Create a button to select files
select_button = tk.Button(root, text="Select EXE Files", command=select_files)
select_button.pack(pady=20)

# Start the GUI
root.mainloop()