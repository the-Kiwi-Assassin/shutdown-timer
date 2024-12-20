import os
import customtkinter

root=customtkinter.CTk()
root.title("ShutDownTimer")
root.iconbitmap("image_2024-12-20_001846172.ico")
root.resizable(False,False)
root.geometry("550x160")
customtkinter.set_appearance_mode("system")


label_var0=customtkinter.StringVar(root,'SHUT DOWN TIMER')
label_var1=customtkinter.StringVar(root,'time hh:mm:ss')
label_var2=customtkinter.StringVar(root,'time in seconds')
entry_var1=customtkinter.StringVar(root,"0")
entry_var2=customtkinter.StringVar(root,"0")
entry_var3=customtkinter.StringVar(root,"0")
entry_var4=customtkinter.StringVar(root)



# Globale Variable fÃ¼r den Countdown-Wert
countdown_time = 0

def countdown():
    global countdown_time, is_canceled
    if countdown_time > 0 and not is_canceled:
        countdown_time -= 1
        entry_var4.set(str(countdown_time))
        root.after(1000, countdown)  # Countdown lÃ¤uft alle 1000 ms (1 Sekunde)
    elif countdown_time == 0 and not is_canceled:
        entry_var4.set("Shutdown!")
        os.system(f"shutdown -s -t 0")  # Hier wird der Shutdown-Befehl ausgefÃ¼hrt

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


def button_confirm2(event):
    global countdown_time, is_canceled
    try:
        button_confirm()

    except ValueError:
        entry_var4.set("Invalid input")


def button_cancel():
    global is_canceled
    is_canceled = True  # Countdown stoppen
    entry_var4.set("Canceled!")


def button_cancel2(event):
    global is_canceled
    try:
        button_cancel()
    except ValueError:
        entry_var4.set("canceled!")


def optionmenu1_callback(choice):
    if choice == "1hour" :
        entry_var1.set("1")
    elif choice == "2hours" :
        entry_var1.set("2")
    elif choice == "4hours" :
        entry_var1.set("4")
    elif choice == "6hours" :
        entry_var1.set("6")
    elif choice == "8hours" :
        entry_var1.set("8")

def optionmenu2_callback(choice):
    if choice == "15minutes" :
        entry_var2.set("15")
    elif choice == "30minutes" :
        entry_var2.set("30")
    elif choice == "45minutes" :
        entry_var2.set("45")

def slider_event(value):
    global entry_var3
    entry_var3.set(int(value))
    


label0=customtkinter.CTkLabel(root, textvariable=label_var0,
                              text_color="#00ff00")
label1=customtkinter.CTkLabel(root, textvariable=label_var1,
                              text_color="#00ff00")
entry1=customtkinter.CTkEntry(root, textvariable=entry_var1,
                              text_color="#00ff00")
entry2=customtkinter.CTkEntry(root, textvariable=entry_var2,
                              text_color="#00ff00")
entry3=customtkinter.CTkEntry(root, textvariable=entry_var3,
                              text_color="#00ff00")
label2=customtkinter.CTkLabel(root, textvariable=label_var2,
                              text_color="#00ff00")
entry4=customtkinter.CTkEntry(root, textvariable=entry_var4,
                              text_color="#00ff00")


optionmenu_var1 = customtkinter.StringVar(value="hours")
optionmenu1 = customtkinter.CTkOptionMenu(root,values=["1hour", "2hours", "4hours", "6hours", "8hours"],
                                         command=optionmenu1_callback,
                                         variable=optionmenu_var1,
                                         width=139,
                                         fg_color="#00ff00",
                                         button_color="#00ff00",
                                         button_hover_color="#009900",
                                         text_color="#000000",
                                         corner_radius=20,
                                         dropdown_fg_color="#000000",
                                         dropdown_text_color="#ffffff")

optionmenu_var2 = customtkinter.StringVar(value="Minutes")

optionmenu2 = customtkinter.CTkOptionMenu(root,values=["15minutes", "30minutes", "45minutes"],
                                         command=optionmenu2_callback,
                                         variable=optionmenu_var2,
                                         width=139,
                                         fg_color="#00ff00",
                                         button_color="#00ff00",
                                         button_hover_color="#009900",
                                         text_color="#000000",
                                         corner_radius=20,
                                         dropdown_fg_color="#000000",
                                         dropdown_text_color="#ffffff")

slider = customtkinter.CTkSlider(root, from_=0, to=59, command=slider_event, number_of_steps=59,
                                 width=141,
                                 border_width=3,
                                 border_color="#000000",
                                 progress_color="#00ff00",
                                 fg_color="#009900",
                                 button_color="#00cc00",
                                 button_hover_color="#008800")

confirm=customtkinter.CTkButton(root,text="OK",command=button_confirm,
                                 fg_color="#00ff00",
                                 hover_color="#009900",
                                 text_color="#000000",
                                 border_width=3,
                                 border_color="#000000")

cancel=customtkinter.CTkButton(root,text='cancel',command=button_cancel, 
                                 fg_color="#00ff00",
                                 hover_color="#009900",
                                 text_color="#000000",
                                 border_width=3,
                                 border_color="#000000")

root.bind("<Escape>", button_cancel2)
root.bind("<Return>",button_confirm2)



label0.grid(row=0,column=2)
label1.grid(row=1,column=0)
entry1.grid(row=1,column=1)
entry2.grid(row=1,column=2)
entry3.grid(row=1,column=3)
label2.grid(row=2,column=0)
entry4.grid(row=2,column=1)
optionmenu1.grid(row=3,column=1, pady=5)
optionmenu2.grid(row=3,column=2, pady=5)
slider.grid(row=3, column=3, pady=5)
confirm.grid(row=4,column=1)
cancel.grid(row=4,column=2)
root.mainloop()