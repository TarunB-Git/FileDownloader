# Main file
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from downloader import download_files
from renamer import rename_files, create_rename_csv

def set_default_location():
    default_location = "/home"
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, default_location)

def choose_location():
    folder_selected = filedialog.askdirectory(initialdir="/home")
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_selected)

root = tk.Tk()
root.title("File Downloader")

# URL Entry
url_label = tk.Label(root, text="Enter URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.insert(0, "https://")  # Set default value to https://
url_entry.pack()

# Folder Entry
folder_label = tk.Label(root, text="Download Location:")
folder_label.pack()
folder_entry = tk.Entry(root, width=50)
folder_entry.pack()

# Default Location Button
default_button = tk.Button(root, text="Set Default Location", command=set_default_location)
default_button.pack()

# Choose Location Button
choose_button = tk.Button(root, text="Choose Location", command=choose_location)
choose_button.pack()

# Checkbox for Rename Option
abort_var = tk.IntVar()
rename_checkbox = tk.Checkbutton(root, text="Don't Rename Files?", variable=abort_var)
rename_checkbox.pack()

# File Extension Text Entry
extension_label = tk.Label(root, text="File Extension (e.g., .png, .pdf):")
extension_label.pack()

extension_entry = tk.Entry(root, width=20)
extension_entry.pack()

# Default Extensions Dropdown
dropdown_label = tk.Label(root, text="Select Extension (Optional):")
dropdown_label.pack()

file_type_options = ['.pdf', '.png', '.mp3', '.mp4', '.docx', 'All Files']
file_type_var = tk.StringVar(value=file_type_options[0])  # Default to .pdf

def update_extension_field(*args):
    extension_entry.delete(0, tk.END)  # Clear the text field
    extension_entry.insert(0, file_type_var.get())  # Insert the selected value from the dropdown

file_type_menu = tk.OptionMenu(root, file_type_var, *file_type_options, command=update_extension_field)
file_type_menu.pack()

# Download Button
download_button = tk.Button(root, text="Download Files", command=lambda: download_files(url_entry, folder_entry, extension_entry, abort_var))
download_button.pack()

# Rename Button
rename_button = tk.Button(root, text="Rename Files", command=lambda: rename_files(folder_entry.get()))
rename_button.pack()

root.mainloop()

