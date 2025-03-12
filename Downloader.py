#!/usr/bin/python3
import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox, filedialog
import csv

downloads = 0

def set_default_location():
    default_location = "/home/tar_guest/Downloads"
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, default_location)

def choose_location():
    folder_selected = filedialog.askdirectory(initialdir="/home/tar_guest/Downloads")
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_selected)


def download_files():
    global downloads
    url = url_entry.get()
    folder_location = folder_entry.get()
    file_extension = extension_entry.get()  # Get the file extension from the text field
    folder_location = extension_entry.get() 

    if not os.path.exists(folder_location):
        os.mkdir(folder_location)
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    file_info = []
    
    count = 0
    skipped_files = []  # List to keep track of skipped files
    
    if file_extension == "All Files":
        # Scrape all files if the "All Files" option is selected
        for link in soup.find_all("a", href=True):
            file_url = link['href']
            filename = os.path.join(folder_location, file_url.split('/')[-1])
            file_info.append([link.text, filename])
            
            try:
                with open(filename, 'wb') as f:
                    f.write(requests.get(urljoin(url, file_url)).content)
                downloads += 1
                count += 1
            except Exception as e:
                print(f"Error downloading {filename}: {e}")
                skipped_files.append(filename)
    else:

        for link in soup.select(f"a[href$='{file_extension}']"):
            filename = os.path.join(folder_location, link['href'].split('/')[-1])
            file_info.append([link.text + file_extension, filename])
            
            try:
                with open(filename, 'wb') as f:
                    f.write(requests.get(urljoin(url, link['href'])).content)
                downloads += 1
                count += 1
            except Exception as e:
                print(f"Error downloading {filename}: {e}")
                skipped_files.append(filename)

    messagebox.showinfo("Download Complete", f"{file_extension} files downloaded successfully! Total downloads: {downloads} Downloaded Now: {count}")

    with open(os.path.join(folder_location, 'filenames.csv'), mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for info in file_info:
            writer.writerow(info)
    
    if skipped_files:
        with open(os.path.join(folder_location, 'skipped_files1.log'), 'w') as logfile:
                logfile.write("Skipped files due to errors:\n")
                for skipped_file in skipped_files:
                    logfile.write(f"{skipped_file}\n")
        messagebox.showinfo("Skipped Files", f"Some files were skipped due to errors. Check 'skipped_files1.log' for details.")
    
    if not abort_var.get():  # If the checkbox is not selected
        rename_files(folder_location)
    else:
        messagebox.showinfo("Action Aborted", "File renaming aborted.")

def rename_files(folder_location):
    try:
        rename_file_path = os.path.join(folder_location, 'filenames.csv')
        with open(rename_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            skipped_files = []  
            for row in reader:
                original_filename = row[1]
                new_filename = row[0]
                original_path = os.path.join(folder_location, original_filename)
                new_path = os.path.join(folder_location, new_filename)
                try:
                    os.rename(original_path, new_path)
                    print(f"Renamed {original_filename} to {new_filename}")
                except Exception as e:
                    print(f"Error renaming {original_filename} to {new_filename}: {e}")
                    skipped_files.append((original_filename, new_filename))
        
        rename_csv_path = os.path.join(folder_location, 'rename.csv')
        with open(rename_csv_path, 'w', newline='') as renamefile:
            writer = csv.writer(renamefile)
            # Re-read from filenames.csv to create rename.csv
            with open(rename_file_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                first_column = [row[0] for row in reader]  
                # Write the first column to both column 0 and column 1 of rename.csv
                for item in first_column:
                    writer.writerow([item, item])
        
        # Log skipped files
        if skipped_files:
            with open(os.path.join(folder_location, 'skipped_files2.log'), 'w') as logfile:
                logfile.write("Skipped files due to errors:\n")
                for original, new in skipped_files:
                    logfile.write(f"{original} -> {new}\n")
            messagebox.showinfo("Renaming Skipped Files", "Some files were skipped due to errors. Check 'skipped_files2.log' for details.")

    except Exception as e:
        print(f"Error processing rename file: {e}")
        messagebox.showerror("Error", "An error occurred while processing the rename file.")
        

root = tk.Tk()
root.title("File Downloader")

# URL Entry
url_label = tk.Label(root, text="Enter URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
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
download_button = tk.Button(root, text="Download Files", command=download_files)
download_button.pack()

root.mainloop()

