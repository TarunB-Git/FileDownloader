import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import csv
from tkinter import messagebox
from renamer import create_rename_csv

downloads = 0

def download_files(url_entry, folder_entry, extension_entry, abort_var):
    global downloads
    url = url_entry.get()
    folder_location = folder_entry.get()  # Get the folder location from the input field
    file_extension = extension_entry.get()  # Get the file extension from the text field
    
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
            # Ensure that the file URL has a valid extension
            if '.' in file_url:
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
        # Scrape files with the specific extension
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

    # Write the filenames to 'filenames.csv'
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
        print("Renaming will proceed.")  # Debugging
        create_rename_csv(folder_location)
    else:
        messagebox.showinfo("Action Aborted", "File renaming aborted.")

