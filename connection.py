import urllib.request
from urllib.error import URLError
from tkinter import *
import tkinter as tk

def check():
    web = url.get().strip()

    # Auto-prepend "https://" if missing
    if not web.startswith("http://") and not web.startswith("https://"):
        web = "https://" + web

    try:
        status_code = urllib.request.urlopen(web).getcode()
        website_is_up = (status_code == 200)
        if website_is_up:
            result_label.config(text="✅ Website Available", fg="green")
        else:
            result_label.config(text="❌ Website Not Available", fg="red")
    except URLError:
        result_label.config(text="❌ Invalid URL or No Internet", fg="red")
    except ValueError:
        result_label.config(text="❌ URL Format Error", fg="red")

# GUI Setup
window = Tk()
window.geometry("700x350")
window.title("PythonGeeks")

Label(window, text="Website Connectivity Checker", font=('Calibri', 15)).pack(pady=20)

url = tk.StringVar()

Entry(window, textvariable=url).place(x=200, y=80, height=30, width=280)

Button(window, text="Check", command=check).place(x=320, y=160)

result_label = Label(window, text="", font=('Calibri', 15))
result_label.place(x=230, y=220)

window.mainloop()