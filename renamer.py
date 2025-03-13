# renamer.py
import os
import csv
from tkinter import messagebox

def create_rename_csv(folder_location):
    try:
        filenames_csv_path = os.path.join(folder_location, 'filenames.csv')
        
        # Check if filenames.csv exists
        if not os.path.exists(filenames_csv_path):
            print(f"Error: {filenames_csv_path} does not exist.")
            messagebox.showerror("Error", "'filenames.csv' was not found.")
            return
        
        with open(filenames_csv_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            rename_file_path = os.path.join(folder_location, 'rename.csv')
            
            # Open rename.csv for writing
            with open(rename_file_path, 'w', newline='') as renamefile:
                writer = csv.writer(renamefile)
                
                # Write a new rename.csv with old names and new names
                for row in reader:
                    original_filename = row[1]  # Current filename from filenames.csv
                    new_filename = original_filename  
                    writer.writerow([new_filename, original_filename])
                    print(f"Written to rename.csv: {new_filename} -> {original_filename}")
        
        # Confirm that rename.csv was created successfully
        if os.path.exists(rename_file_path):
            print(f"rename.csv created successfully in {folder_location}")
            messagebox.showinfo("Rename CSV Created", f"'rename.csv' has been created in {folder_location}. You can now modify it for renaming.")
        else:
            print("Error: rename.csv was not created.")
            messagebox.showerror("Error", "An error occurred while creating rename.csv.")
    
    except Exception as e:
        print(f"Error creating rename.csv: {e}")
        messagebox.showerror("Error", "An error occurred while creating the rename.csv file.")
def rename_files(folder_location):
    try:
        rename_file_path = os.path.join(folder_location, 'rename.csv')
        if not os.path.exists(rename_file_path):
            messagebox.showerror("Error", "rename.csv not found. Please create it first.")
            return
        
        with open(rename_file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            skipped_files = []  
            for row in reader:
                original_filename = row[0]
                new_filename = row[1]
                original_path = os.path.join(folder_location, original_filename)
                new_path = os.path.join(folder_location, new_filename)
                try:
                    os.rename(original_path, new_path)
                    print(f"Renamed {original_filename} to {new_filename}")
                except Exception as e:
                    print(f"Error renaming {original_filename} to {new_filename}: {e}")
                    skipped_files.append((original_filename, new_filename))
        
        # Log skipped files
        if skipped_files:
            with open(os.path.join(folder_location, 'skipped_files2.log'), 'w') as logfile:
                logfile.write("Skipped files due to errors:\n")
                for original, new in skipped_files:
                    logfile.write(f"{original} -> {new}\n")
            messagebox.showinfo("Renaming Skipped Files", "Some files were skipped due to errors. Check 'skipped_files2.log' for details.")
        
        messagebox.showinfo("Files Renamed", "Files have been renamed successfully.")
    except Exception as e:
        print(f"Error processing rename file: {e}")
        messagebox.showerror("Error", "An error occurred while processing the rename file.")
