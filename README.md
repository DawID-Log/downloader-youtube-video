# **YouTube Video Downloader**

This script allows you to download YouTube videos effortlessly. Key features include:

- **Automatic URL Detection**:  
  The script automatically fetches the URL of the currently open YouTube video in your browser (supported browsers: Firefox, Chrome).

- **Direct Download to `download` Folder**:  
  All downloaded videos are saved in a folder named `download`, which is automatically created in the current directory.

- **Completion Notification**:  
  When the download is finished, a popup window notifies you of the successful operation.

## **How to Use**

1. Open a YouTube video in Firefox or Chrome.  
2. Run the script: it will automatically detect the video URL and start the download.  
3. The downloaded videos will be saved in the `download` folder in the same directory as the script.

---

### **Command to Create the Executable**

To create an executable for the program, follow these steps:

1. **Install PyInstaller**:  
   Ensure that `pyinstaller` is installed. If not, install it using:

   ```bash
   pip install pyinstaller
   ```

2. **Generate the Executable**:  
   Run the following command in your terminal or command prompt:

   ```bash
   pyinstaller --onefile --noconsole main.py
   ```

   - `--onefile`: Combines all dependencies into a single executable.  
   - `--noconsole`: Hides the console window (optional, useful for GUI-only applications).  

3. **Locate the Executable**:  
   After running the command, the executable will be located in the `dist` folder, which is created in the same directory as your script.

---

### **Download the ZIP File**

You can also download the pre-packaged ZIP file containing the executable and all necessary dependencies. Once downloaded, extract the ZIP file and run the executable directly from your system, without the need for setting up Python or running the script manually.
