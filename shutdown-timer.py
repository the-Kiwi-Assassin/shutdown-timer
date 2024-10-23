import os
from tkinter import *
import tkinter as tk

root=Tk()
root.title=('title')


label_var0=tk.StringVar(root,'SHUT DOWN TIMER')
label_var1=tk.StringVar(root,'time hh:mm:ss')
label_var2=tk.StringVar(root,'time in seconds')
entry_var1=tk.StringVar(root)
entry_var2=tk.StringVar(root)
entry_var3=tk.StringVar(root)
entry_var4=tk.StringVar(root)



# Globale Variable für den Countdown-Wert
countdown_time = 0

def countdown():
    global countdown_time, is_canceled
    if countdown_time > 0 and not is_canceled:
        countdown_time -= 1
        entry_var4.set(str(countdown_time))
        root.after(1000, countdown)  # Countdown läuft alle 1000 ms (1 Sekunde)
    elif countdown_time == 0 and not is_canceled:
        entry_var4.set("Shutdown!")
        os.system(f"shutdown -s -t 0")  # Hier wird der Shutdown-Befehl ausgeführt

def button_confirm():
    global countdown_time, is_canceled
    try:
        hour = int(entry_var1.get())
        minute = int(entry_var2.get())
        second = int(entry_var3.get())

        # In Sekunden umrechnen
        hh = hour * 60 * 60
        mm = minute * 60
        ss = second

        # Gesamtzeit in Sekunden
        countdown_time = hh + mm + ss

        # Den vierten Eintrag mit der Gesamtzeit in Sekunden aktualisieren
        entry_var4.set(str(countdown_time))

        # Reset is_canceled auf False, falls Countdown neu gestartet wird
        is_canceled = False

        # Countdown starten
        countdown()

    except ValueError:
        entry_var4.set("Invalid input")

def button_cancel():
    global is_canceled
    is_canceled = True  # Countdown stoppen
    entry_var4.set("Canceled!")



label0=Label(root, textvariable=label_var0)
label1=Label(root, textvariable=label_var1)
entry1=Entry(root, textvariable=entry_var1)
entry2=Entry(root, textvariable=entry_var2)
entry3=Entry(root, textvariable=entry_var3)
label2=Label(root, textvariable=label_var2)
entry4=Entry(root, textvariable=entry_var4)
button_confirm=Button(root,text="OK",command=button_confirm)
button_cancel=Button(root,text='cancel',command=button_cancel)



label0.grid(row=0,column=2)
label1.grid(row=1,column=0)
entry1.grid(row=1,column=1)
entry2.grid(row=1,column=2)
entry3.grid(row=1,column=3)
label2.grid(row=2,column=0)
entry4.grid(row=2,column=1)
button_confirm.grid(row=3,column=1)
button_cancel.grid(row=3,column=2)

root.mainloop()

