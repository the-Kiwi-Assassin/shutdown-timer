import os
import sys
import customtkinter
from tkinter.filedialog import askopenfilename
from datetime import datetime

class SettingsWindow(customtkinter.CTkToplevel):
    def __init__(self, set_theme_callback, *number, **word):
        super().__init__(*number, **word)
        self.title("Settings")
        self.geometry("200x150")
        self.resizable(False, False)
        self.set_theme_button = customtkinter.CTkButton(self, text="Set Theme", command=set_theme_callback)
        self.set_theme_button.grid(row=1, column=0, padx=29, pady=29)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Timing Task")
        self.iconbitmap("image_2024-12-20_001846172.ico")
        self.resizable(False, False)
        self.geometry("620x260")
        customtkinter.set_appearance_mode("system")

        self.label_var0 = customtkinter.StringVar(self, 'Timing Task')
        self.label_var1 = customtkinter.StringVar(self, 'time hh:mm:ss')
        self.label_var2 = customtkinter.StringVar(self, 'time in seconds')
        self.entry_var1 = customtkinter.StringVar(self, "0")
        self.entry_var2 = customtkinter.StringVar(self, "0")
        self.entry_var3 = customtkinter.StringVar(self, "0")
        self.entry_var4 = customtkinter.StringVar(self)
        self.entry_var_program = customtkinter.StringVar(self, "notepad.exe")

        self.countdown_time = 0
        self.selected_function = "Shutdown"
        self.is_canceled = False

        self.setup_widgets()
        self.bind("<Escape>", self.button_cancel2)
        self.bind("<Return>", self.button_confirm2)

        self.settings_window = None

    def setup_widgets(self):
        label0 = customtkinter.CTkLabel(self, textvariable=self.label_var0)
        label1 = customtkinter.CTkLabel(self, textvariable=self.label_var1)
        entry1 = customtkinter.CTkEntry(self, textvariable=self.entry_var1)
        entry2 = customtkinter.CTkEntry(self, textvariable=self.entry_var2)
        entry3 = customtkinter.CTkEntry(self, textvariable=self.entry_var3)
        label2 = customtkinter.CTkLabel(self, textvariable=self.label_var2)
        entry4 = customtkinter.CTkEntry(self, textvariable=self.entry_var4)
        entry_program = customtkinter.CTkEntry(self, textvariable=self.entry_var_program)
        label_program = customtkinter.CTkLabel(self, text="Program Name")

        optionmenu_var1 = customtkinter.StringVar(value="hours")
        optionmenu1 = customtkinter.CTkOptionMenu(
            self,
            values=["1hour", "2hours", "4hours", "6hours", "8hours"],
            command=self.optionmenu1_callback,
            variable=optionmenu_var1,
            width=139,
            corner_radius=20
        )

        optionmenu_var2 = customtkinter.StringVar(value="Minutes")
        optionmenu2 = customtkinter.CTkOptionMenu(self, values=["15minutes", "30minutes", "45minutes"],
                                                 command=self.optionmenu2_callback,
                                                 variable=optionmenu_var2,
                                                 width=139,
                                                 corner_radius=20)

        optionmenu_var3 = customtkinter.StringVar(value="Function")
        optionmenu3 = customtkinter.CTkOptionMenu(
            self,
            values=["Shutdown", "restart", "log off", "kill task"],
            command=self.optionmenu3_callback,
            variable=optionmenu_var3,
            width=139,
            corner_radius=20
        )

        slider = customtkinter.CTkSlider(self, from_=0, to=59, command=self.slider_event, number_of_steps=59,
                                         width=141,
                                         border_width=3)

        confirm = customtkinter.CTkButton(self, text="OK", command=self.button_confirm,
                                         border_width=3)

        cancel = customtkinter.CTkButton(self, text='cancel', command=self.button_cancel,
                                         border_width=3)

        set_theme_button = customtkinter.CTkButton(
            self,
            text="Settings",
            command=self.open_settings_window,
            border_width=3
        )

        # Grid placement
        label0.grid(row=0, column=2)
        label1.grid(row=1, column=0, padx=20)
        entry1.grid(row=1, column=1)
        entry2.grid(row=1, column=2)
        entry3.grid(row=1, column=3)
        label2.grid(row=2, column=0, padx=20)
        entry4.grid(row=2, column=1)
        label_program.grid(row=3, column=0, padx=20)
        entry_program.grid(row=3, column=1)
        optionmenu1.grid(row=4, column=1)
        optionmenu2.grid(row=4, column=2)
        slider.grid(row=4, column=3)
        optionmenu3.grid(row=4, column=0, padx=20)
        confirm.grid(row=5, column=1)
        cancel.grid(row=5, column=2)
        set_theme_button.grid(row=5, column=3)

    # --- Logic methods (copied and adapted from your code) ---
    def countdown(self):
        if self.countdown_time > 0 and not self.is_canceled:
            self.countdown_time -= 1
            self.entry_var4.set(str(self.countdown_time))
            self.after(1000, self.countdown)
        elif self.countdown_time == 0 and not self.is_canceled:
            self.entry_var4.set(f"{self.selected_function}!")
            if self.selected_function == "Shutdown":
                os.system("shutdown -s -t 0")
            elif self.selected_function == "restart":
                os.system("shutdown -r -t 0")
            elif self.selected_function == "log off":
                os.system("shutdown -l")
            elif self.selected_function == "kill task":
                program_name = self.entry_var_program.get()
                os.system(f"taskkill /IM {program_name} /T /F")

    def button_confirm(self):
        try:
            hour = int(self.entry_var1.get())
            minute = int(self.entry_var2.get())
            second = int(self.entry_var3.get())
            hh = hour * 60 * 60
            mm = minute * 60
            ss = second
            self.countdown_time = hh + mm + ss
            self.entry_var4.set(str(self.countdown_time))
            self.is_canceled = False
            self.countdown()
        except ValueError:
            self.entry_var4.set("Invalid input")

    def button_confirm2(self, event):
        try:
            self.button_confirm()
        except ValueError:
            self.entry_var4.set("Invalid input")

    def button_cancel(self):
        self.is_canceled = True
        self.entry_var4.set("Canceled!")

    def button_cancel2(self, event):
        try:
            self.button_cancel()
        except ValueError:
            self.entry_var4.set("canceled!")

    def optionmenu1_callback(self, choice):
        if choice == "1hour":
            self.entry_var1.set("1")
        elif choice == "2hours":
            self.entry_var1.set("2")
        elif choice == "4hours":
            self.entry_var1.set("4")
        elif choice == "6hours":
            self.entry_var1.set("6")
        elif choice == "8hours":
            self.entry_var1.set("8")

    def optionmenu2_callback(self, choice):
        if choice == "15minutes":
            self.entry_var2.set("15")
        elif choice == "30minutes":
            self.entry_var2.set("30")
        elif choice == "45minutes":
            self.entry_var2.set("45")

    def optionmenu3_callback(self, choice):
        self.selected_function = choice

    def slider_event(self, value):
        self.entry_var3.set(int(value))

    def open_settings_window(self):
        if self.settings_window is None or not self.settings_window.winfo_exists():
            self.settings_window = SettingsWindow(self.set_theme)
        else:
            self.settings_window.focus()

    def set_theme(self):
        filename = askopenfilename(filetypes=[("JSON files", "*.json")])
        if filename:
            customtkinter.set_default_color_theme(filename)
            self.destroy()
            app = App()
            app.mainloop()

def create_file():
    with open("log.txt", "a+"):
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()
    create_file()