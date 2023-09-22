import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import threading
import sys
import os
basedir = os.path.dirname(__file__)
def update_progress():
    progress = 0
    while progress < 100:
        progress += 1
        loading_window.update_idletasks()
        progress_var.set(progress)
        if progress == 25:
            status_label.config(text="Wetter wird gecheckt...")
        elif progress == 50:
            status_label.config(text="Daten aus deinem Standort werden abgerufen...")
        elif progress == 75:
            status_label.config(text="NASA wird gehackt...")
        time.sleep(0.1)
    loading_window.destroy()
    show_message_window()
    input_entry.config(state=tk.NORMAL)
    button.config(state=tk.NORMAL)

def show_message_window():
    message_window = tk.Toplevel()
    message_window.title("Ergebnis")
    message_label = tk.Label(message_window, text="Schau einfach aus deinem Fenster", padx=10, pady=10)
    message_label.pack()

def open_loading_window():
    global loading_window, status_label
    if not input_entry.get():
        messagebox.showerror("Fehler", "Die Eingabe darf nicht leer sein.")
        return
    input_entry.config(state=tk.DISABLED)
    button.config(state=tk.DISABLED)

    loading_window = tk.Toplevel(main_window)
    loading_window.title("Laden")
    loading_window.geometry("300x100")

    status_label = tk.Label(loading_window, text="Startet...", padx=10, pady=10)
    status_label.pack()

    progress_bar = ttk.Progressbar(loading_window, orient="horizontal", length=200, mode="determinate", variable=progress_var)
    progress_bar.pack()

    progress_thread = threading.Thread(target=update_progress)
    progress_thread.start()

def clear_original_window():
    input_label.pack_forget()  # Verstecke das Label
    input_entry.pack_forget()  # Verstecke das Entry-Feld
    button.pack_forget()  # Verstecke den Button
    input_label.pack()  # Zeige das Label erneut an
    input_entry.pack()  # Zeige das Entry-Feld erneut an
    button.pack()  # Zeige den Button erneut an

main_window = tk.Tk()
main_window.title("Wetter Checker")
main_window.geometry("300x100")
main_window.iconbitmap(os.path.join(basedir, "icon.ico"))

input_label = tk.Label(main_window, text="Gib deinen Ort ein, um das Wetter zu checken:")
input_label.pack()

input_entry = tk.Entry(main_window)
input_entry.pack()

button = tk.Button(main_window, text="Jetzt checken", command=lambda: [open_loading_window(), clear_original_window()])
button.pack()

main_window_label = tk.Label(main_window, text="")
main_window_label.pack()

progress_var = tk.DoubleVar()
loading_window = None
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
iconPath = resource_path('icon.ico')
main_window.mainloop()
