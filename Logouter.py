import tkinter as tk
from win10toast import ToastNotifier
from tkinter import messagebox
import os

allowpath = None

def on_closing():
    pass
def countdown(count):
    # change text in label
    minutes['text'] = str(count//60) + " минут"
    seconds['text'] = str(count%60) + " секунд"
    if count < 60*5:
        seconds['fg'] = 'red'
        minutes['fg'] = 'red'
    if count <= 60:
        seconds['font'] = ('Helvetica', 40)
        minutes['font'] = ('Helvetica', 10)
    if count > 0:
        mainWindows.after(1000, countdown, count-1)
    elif count == 0:
        toaster.show_toast("ВРЕМЯ ВЫШЛО","ВРЕМЯ ВЫШЛО",icon_path='icon.ico',duration=5,threaded=True)
        if os.path.isfile(allowpath): os.remove(allowpath)
        os.system('shutdown /l')
    if (count == 5*60):
        toaster.show_toast("Время заканчивается","Осталось 5 минут",icon_path='icon.ico',duration=5,threaded=True)
    elif (count == 60):
        toaster.show_toast("Время заканчивается","Осталось 1 минута",icon_path='icon.ico',duration=5,threaded=True)
mainWindows = tk.Tk()
mainWindows.title("Timer")
mainWindows.config(width=400, height=200, bg='white')
toaster = ToastNotifier()

seconds = tk.Label(mainWindows, font=('Helvetica', 20), bg='white')
minutes = tk.Label(mainWindows, font=('Helvetica', 40), bg='white')
seconds.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
minutes.place(relx=0.5, rely=0.3, anchor=tk.CENTER)


if os.path.isfile('path.txt'):
    pathstr = open('path.txt')
    allowpath = pathstr.read()
    if os.path.isfile(allowpath):
        reader = open(allowpath, 'r')
        ptime = reader.read()
        reader.close()
        countdown(int(ptime))
    else:
        countdown(10)
        toaster.show_toast("Нет разрешения","Осталось 10 секунд",icon_path='icon.ico',duration=5,threaded=True)

mainWindows.protocol("WM_DELETE_WINDOW", on_closing)
mainWindows.mainloop()