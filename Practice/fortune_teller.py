from tkinter import * 
import os 
import time
import random

def click_my_button():
    my_fortune = random.choice(["Definitely", "No way", "Maybe"])
    enter_question.destroy()
    question.destroy()
    button.destroy()
    final_fortune = Label(vault, text=f"Answer: {my_fortune}.", font=("Brush Script MT", 30, "italic"), fg="SlateBlue")
    final_fortune.pack(pady=70)

vault = Tk()
vault.geometry("600x400")
fortune_teller = Label(vault, text="Fortune Teller", font=("Calibri", 40, "bold"))
fortune_teller.pack()
enter_question = Label(vault, text="Enter Your Question", font=("Calibri", 20, "bold"))
enter_question.pack()
question = Entry(vault)
question.pack()
button = Button(vault, text="Get My Fortune", fg="blue", command=click_my_button)
button.pack(pady=10)

vault.mainloop()