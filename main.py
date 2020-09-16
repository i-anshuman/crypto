import tkinter as tk
from tkinter import StringVar
from lib.crypto import Crypto

def change_btn_text():
    btn.configure(text=operation.get().title())

def convert():
    c = Crypto()
    input = txt.get("1.0", tk.END)
    res.delete("1.0", tk.END)
    if (operation.get() == "encrypt"):
        cipher = c.encrypt(input[0:len(input)-1])
        res.insert("1.0", cipher)
    elif (operation.get() == "decrypt"):
        plaintext = c.decrypt(input)
        res.insert("1.0", plaintext)

def clear():
    txt.delete("1.0", tk.END)
    res.delete("1.0", tk.END)

window = tk.Tk()
window.title("Crypto")
frm_radio = tk.Frame(master=window)
frm_input = tk.Frame(master=window)
frm_btn = tk.Frame(master=window)
frm_radio.pack()
frm_input.pack()
frm_btn.pack()
operation = StringVar(window, "encrypt")

radio_encrypt = tk.Radiobutton(
    master=frm_radio,
    text="Encrypt",
    value="encrypt",
    variable=operation,
    command=change_btn_text
)
radio_decrypt = tk.Radiobutton(
    master=frm_radio,
    text="Decrypt",
    value="decrypt",
    variable=operation,
    command=change_btn_text
)
radio_encrypt.bind()
radio_encrypt.pack(side="left")
radio_decrypt.pack(side="left")
txt = tk.Text(master=frm_input, width=50)
res = tk.Text(master=frm_input, width=50)
txt.pack(side="left")
res.pack(side="right")
btn = tk.Button(
    master=frm_btn,
    width=25,
    text=operation.get().title(),
    command=convert
)
clr = tk.Button(
    master=frm_btn,
    width=25,
    text="Clear",
    command=clear
)
btn.pack(side="left")
clr.pack(side="right")
window.mainloop()
