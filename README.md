File Downloader and Renamer

This tkinter-based gui application allows users to download files from a provided URL. 
The file types are based on the user's selection, and the files are saved to a userdefined directory. The application also allows users to rename downloaded files based on an existing CSV file and logs any errors encountered during the process.

 Features :

  Downloads files of any type/extension from links found on a given URL. Extension is pre-defined by the user, but can be set to download from all links on a web-page.

 Users can choose a custom directory to save downloaded files.
 
 After the download, the app logs filenames in a CSV file for reference. Downloaded files are renamed based on a CSV file mapping of original and desired filenames. If any files are skipped due to errors, they are logged into separate `log` files.

 Requirements

 Python 3.x
 Python packages:
   `requests`
   `beautifulsoup4`
   `tkinter`
   `csv`

 Installation : 

1. Clone this repository:
   ```bash
   git clone https://github.com/Tarunb-Git/FileDownloader
   ```

2. Install the required dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```

3. Run the application:
   ```bash
   python file_downloader.py
   ```

 Process : 

 1. Enter URL:
    In the "Enter URL" field, input the URL from which you want to download files. The program will scan the page for links that match the file type you choose.

 2. Choose File Type:
    Select the file type you want to download (e.g., `.png`, `.pdf`, `.mp3`, `.mp4`, `.docx`). This allows you to filter the links on the page and download only the desired file type.

 3. Select Download Location:
    You can either set a default folder location or use the "Choose Location" button to browse and select your desired folder where the files will be saved.

 4. Download Files:
    Once you have set the URL and selected the necessary options, click the "Download Files" button to start the process. The program will download the files and save them in the selected location.

 5. Renaming Files:
    If the "Don't Rename pngs?" checkbox is unchecked, the program will attempt to rename downloaded files according to the CSV mapping.
    If any files cannot be renamed, they will be logged in a `skipped_files.log` file.

 6. Renaming CSV:
    After downloading and renaming files, the program will create a `rename.csv` file which logs all the changes, with the new filename and original filename.

 7. Error Handling:
    If any files cannot be downloaded, or if there are any errors, they will be logged in separate `.log` files (`skipped_files1.log`, `skipped_files2.log`, etc.) for troubleshooting.

 8. Abort Renaming:
    If you check the "Don't Rename pngs?" checkbox, the renaming operation will be skipped, and the program will only download the files.


 File Extensions: The program is designed to handle any file type (e.g., `.png`, `.pdf`, `.mp3`, `.mp4`, `.docx`), as long as the URL links point to files with the selected extension.
 
 CSV Format: The CSV file used for renaming should have the following structure:
  ```
  new_filename,original_filename
  new_file.png,image.png
  new_document.pdf,old_document.pdf
  ```

 Contributing :

Contributions are welcome! If you have any improvements or bug fixes, feel free to submit a pull request.

 License :

This project is licensed under the MIT License  see the [LICENSE] file for details.
