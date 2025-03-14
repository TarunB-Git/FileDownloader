# File Downloader and Renamer

This tkinter-based gui application allows users to mass download files from a provided URL. 
The file types are based on the user's selection, and the files are saved to a userdefined directory. 
The application also allows users to rename downloaded files based on an existing CSV file and logs any errors encountered during the process.

 Features :

 Downloads files of any type/extension from links found on a given URL. Extension is pre-defined by the user, but can be set to download from all links on a web-page.

 Users can choose a custom directory to save downloaded files.
 
 After the download, the app logs filenames in two CSV files for reference. Downloaded files are renamed based on a CSV file mapping of original and desired filenames. If any files are skipped due to errors, they are logged into separate `log` files.

# Requirements

 Python 3.x
 Python packages:
   `requests`
   `beautifulsoup4`
   `tkinter`
   `csv`

# Installation : 

1. Clone this repository:
   ```bash
   git clone https://github.com/Tarunb-Git/FileDownloader
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

# Process : 
 
 ![Screenshot from 2025-03-14 15-39-34](https://github.com/user-attachments/assets/ebe28138-0b57-46b7-a731-b7cb1d099603)

 1. Enter URL:
    In the "Enter URL" field, input the URL from which you want to download files. The program will scan the page for links that match the file type you choose.

 2. Choose File Type:
    Select the file type you want to download (e.g., `.png`, `.pdf`, `.mp3`, `.mp4`, `.docx`). This allows you to filter the links on the page and download only the desired file type.

 3. Select Download Location:
    You can either set a default folder location or use the "Choose Location" button to browse and select your desired folder where the files will be saved.

 4. Download Files:
    Once you have set the URL and selected the necessary options, click the "Download Files" button to start the process. The program will download the files and save them in the selected location.

![Screenshot from 2025-03-14 15-40-46](https://github.com/user-attachments/assets/9d47807d-d62f-4d58-89d4-1f2f4e89c8ee) ![Screenshot from 2025-03-14 15-42-56](https://github.com/user-attachments/assets/7c4047f0-20fb-4b78-9b4a-16097c1facde)

![Screenshot from 2025-03-14 15-44-06](https://github.com/user-attachments/assets/1e011b95-e797-4ac4-8499-0714c4cdaacf)

 5. Renaming Files:
    If the "Don't Rename pngs?" checkbox is unchecked, the program will attempt to rename downloaded files according to the CSV mapping.
    If any files cannot be renamed, they will be logged in a `skipped_files.log` file.

 6. Renaming CSV:
    After downloading and renaming files, the program will create a `filenames.csv` file which logs all the changes, with the new filename and original filename, and a `rename.csv` file that can be edited to mass rename files.

![Screenshot from 2025-03-14 15-43-05](https://github.com/user-attachments/assets/64649161-0b7e-41eb-9390-cedd9b21195a) ![Screenshot from 2025-03-14 15-45-24](https://github.com/user-attachments/assets/0c22221c-3007-428b-84db-e0ee3c446284)

![Screenshot from 2025-03-14 15-46-10](https://github.com/user-attachments/assets/508d428e-4423-4039-93f2-79d37ec67aef)

 7. Error Handling:
    If any files cannot be downloaded, or if there are any errors, they will be logged in separate `.log` files (`skipped_files1.log`, `skipped_files2.log`, etc.) for troubleshooting.

![Screenshot from 2025-03-14 15-46-03](https://github.com/user-attachments/assets/a36e4e4d-f644-450c-9de9-4c595ce1eaf5)

 9. Abort Renaming:
    If you check the "Don't Rename Files?" checkbox, the renaming operation will be skipped, and the program will only download the files.
    

 File Extensions: The program is designed to handle any file type (e.g., `.png`, `.pdf`, `.mp3`, `.mp4`, `.docx`), as long as the URL links point to files with the selected extension.
 
 CSV Format: The CSV file used for auto-renaming (`filenames.csv`) has the following structure, and the same format must be used for mass-renaming (`rename.csv`):
  ```
  original_filename,new_filename
  image.png, new_file.png
  old_document.pdf,new_document.pdf
  ```

# Contributing :

Contributions are welcome! If you have any improvements or bug fixes, feel free to submit a pull request.

# License :

This project is licensed under the MIT License, see the [LICENSE] file for details.
