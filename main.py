import os
import subprocess
import tkinter as tk
from tkinter import filedialog, ttk

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
        for file in files:
            listbox.insert(tk.END, (os.path.basename(file), tk.Checkbutton(listbox, variable=tk.BooleanVar())))

def start_installation():
    files_to_install = []
    for i in range(listbox.size()):
        file_name, checkbox = listbox.item(i)
        if checkbox.get():
            files_to_install.append(file_name)
    if files_to_install:
        install_files(files_to_install)

# Create the main window
root = tk.Tk()
root.title("Multiple EXE Installer")
root.geometry("400x300")

# Create a label
label = ttk.Label(root, text="Select files to install:")
label.pack(pady=10)

# Create a listbox to display selected files
listbox = tk.Listbox(root, height=10)
listbox.pack(pady=10)

# Create a button to select files
select_button = ttk.Button(root, text="Select Files", command=select_files)
select_button.pack(pady=5)

# Create a button to start installation
install_button = ttk.Button(root, text="Install Selected Files", command=start_installation)
install_button.pack(pady=5)

# Start the GUI
root.mainloop()