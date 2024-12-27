from pynput.keyboard import Key, Controller
from tkinter import Tk, messagebox
import pygetwindow as gw
from time import sleep
import psutil
import yt_dlp
from pathlib import Path

# FUNCTIONS
def check_browser_open(browser_name):
    for proc in psutil.process_iter(['name']):
        if browser_name.lower() in proc.info['name'].lower():
            return True
    return False

def get_url(browser_name):
    win = gw.getWindowsWithTitle(browser_name)[0]
    win.activate()
    sleep(1)

    keyboard = Controller()
    with keyboard.pressed(Key.ctrl):
        keyboard.press('l')
        keyboard.release('l')
        keyboard.press('c')
        keyboard.release('c')

    url = Tk().clipboard_get()
    return url

def show_message(title, message):
    root = Tk()
    root.withdraw()
    messagebox.showinfo(title, message)
    root.destroy()

def create_download_folder():
    current_dir = Path.cwd()
    download_folder = current_dir / "download"
    download_folder.mkdir(exist_ok=True)
    return download_folder

# MAIN
def main():
    url = ""
    
    if check_browser_open("firefox"):
        url = get_url("Mozilla Firefox")

    if check_browser_open("chrome"):
        url = get_url("Google Chrome")
    print("url: " + url)
    
    download_folder = create_download_folder()
    
    ydl_opts = {
    'format': 'best',
    'outtmpl': str(download_folder / '%(title)s.%(ext)s'),
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        show_message("Download completato", "Il download è stato completato con successo!")
    except Exception as e:
        show_message("Errore durante il download", f"Errore riportato: {e}")
        print(f"Errore durante il download: {e}")

if __name__ == "__main__":
    main()