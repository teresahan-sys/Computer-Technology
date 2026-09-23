from tkinter import *
import os
import time

attempt_counter = 0 

def check_password():
    user_input = enter.get()
    global attempt_counter
    if user_input == "hello103~":
        system_locked.config(text="Access Granted", fg="green")
        vault.update()
        time.sleep(1.2)
        system_locked.destroy()
        enter_password.destroy()
        enter.destroy()
        verify.destroy()
        os.startfile(r"C:\~~HGHS Year 9\Science\Biology\Disease Student Outline.docx")
        vault.destroy()
    else: 
        system_locked.config(text="Access Denied", fg="red")
        attempt_counter = attempt_counter + 1
        if attempt_counter == 3:
            system_locked.config(text="ACCESS TERMINATED.", fg="red", font=("Calibri", 40, "bold"))
            vault.update()
            time.sleep(3)
            vault.destroy()
        else: 
            enter.delete(0, END)

vault = Tk()
vault.geometry("600x400")
system_locked = Label(vault, text="System Locked", font=("Calibri", 50, "bold"))
system_locked.pack()
enter_password = Label(vault, text="Enter Password:", font=("Calibri", 20, "bold"))
enter_password.pack()
enter = Entry(vault, show="*")
enter.pack(pady=5)
verify = Button(vault, text="Confirm", command=check_password)
verify.pack(pady=10)

vault.mainloop()