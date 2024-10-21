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
    global countdown_time
    if countdown_time > 0:
        countdown_time -= 1
        entry_var4.set(str(countdown_time))
        root.after(1000, countdown)  # Countdown läuft alle 1000 ms (1 Sekunde)
    else:
        entry_var4.set("Shutdown!")
        # Hier könntest du den Shutdown-Befehl ausführen:
        # os.system(f"shutdown -s -t 0")

def button_confirm():
    global countdown_time
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

        # Countdown starten
        countdown()

        # Shutdown nach der Zeit (kann auch am Ende des Countdowns passieren)
        # os.system(f"shutdown -s -t {countdown_time}")
    except ValueError:
        entry_var4.set("Invalid input")




label0=Label(root, textvariable=label_var0)
label1=Label(root, textvariable=label_var1)
entry1=Entry(root, textvariable=entry_var1)
entry2=Entry(root, textvariable=entry_var2)
entry3=Entry(root, textvariable=entry_var3)
label2=Label(root, textvariable=label_var2)
entry4=Entry(root, textvariable=entry_var4)
button_confirm=Button(root,text="OK",command=button_confirm)



label0.grid(row=0,column=2)
label1.grid(row=1,column=0)
entry1.grid(row=1,column=1)
entry2.grid(row=1,column=2)
entry3.grid(row=1,column=3)
label2.grid(row=2,column=1)
entry4.grid(row=2,column=2)
button_confirm.grid(row=2,column=3)

root.mainloop()

