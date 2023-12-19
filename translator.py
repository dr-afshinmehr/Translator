import os
import tkinter as tk
from tkinter import ttk
from googletrans import Translator as Tr
from tkinter.messagebox import showinfo

def translator(event):
    try:
        text_src = str(text_src_input.get(1.0, tk.END + "-1c"))
        text_dest.tag_config("Right", justify="right")
        text_dest.delete(1.0, "end-1c")
        translator = Tr()
        if (drawer_list.get() == "Persian"):
            translated_text = translator.translate(text_src, src='auto', dest='fa')
            text_dest.insert(1.0, chars=translated_text.text)
            text_dest.tag_add("Right", 1.0, "end")
        elif (drawer_list.get()== "Chinese"):
            translated_text = translator.translate(text_src, src='auto', dest='zh-tw')
            text_dest.insert(1.0, chars=translated_text.text)
            text_dest.tag_add("Right", 1.0, "end")
        elif (drawer_list.get()== "Jpan"):
            translated_text = translator.translate(text_src, src='auto', dest='ja')
            text_dest.insert(1.0, chars=translated_text.text)
            text_dest.tag_add("Right", 1.0, "end")
        elif (drawer_list.get() == "Italy"):
            translated_text = translator.translate(text_src, src='auto', dest='it')
            text_dest.insert(1.0, chars=translated_text.text)
        elif (drawer_list.get() == "German"):
            translated_text = translator.translate(text_src, src='auto', dest='de')
            text_dest.insert(1.0, chars=translated_text.text)
        elif (drawer_list.get() == "French"):
            translated_text = translator.translate(text_src, src='auto', dest='fr')
            text_dest.insert(1.0, chars=translated_text.text)
        elif (drawer_list.get() == "English"):
            translated_text = translator.translate(text_src, src='auto', dest='en')
            text_dest.insert(1.0, chars=translated_text.text)
        elif (drawer_list.get() == "Arabic"):
            translated_text = translator.translate(text_src, src='auto', dest='ar')
            text_dest.insert(1.0, chars=translated_text.text)
            text_dest.tag_add("Right", 1.0, "end")
    except Exception as Error:
        tk.Message("A.I.A Trnslator", text="Please Select your Language")

# Create Window
main_root = tk.Tk()
main_root.geometry('800x400')
main_root.title('A.I.A Translator')
main_root.iconbitmap(default=r"img\Translate_icon.ico")
main_root.resizable(False, False)

# Artificiaal Intelligence Age Logo
logo = tk.PhotoImage(file=r"img\logo.png")
logo_label = tk.Label(main_root, image=logo)
logo_label.place(x=640, y=10)

# Combo List
# Select Destination Language
langs_val = tk.StringVar()
# Combo
label1 = tk.Label(main_root, text="Select Your Language: ", font=("Arial", 12), fg="Black")
label1.place(x=10, y=25)
drawer_list = ttk.Combobox(main_root, textvariable=langs_val, width=25, cursor="hand2")
drawer_list.place(x=175, y=29)
drawer_list ['state'] = 'readonly'
# List of Languages
lang_list = ["English", "Persian", "Arabic", "French", "Chinese", "Jpan", "German", "Italy"]
lang_list.sort()
# Insert list in Combo
drawer_list ['values'] = tuple(lang_list)
drawer_list.bind('<<ComboboxSelected>>', translator)

# Background 1 for Surce Text
bg_one = tk.PhotoImage(file=r"img\bg.png")
bg_one_lbl = tk.Label(main_root, image=bg_one)
bg_one_lbl.place(x=440, y=80)

# Text Area for src text
text_src_input = tk.Text(main_root, font=("Arial", 12), fg="gray", border=False, bg="#F7F7F7")
text_src_input.place(x=448, y=88, width=337, height=285)

# Translate Button
tr_btn = tk.PhotoImage(file=r"img\go.png")
tr_btn_lbl = tk.Button(main_root, image=tr_btn, cursor="hand2", border=False)
tr_btn_lbl.place(x=375, y=150)
tr_btn_lbl.bind("<Button-1>", translator)

# Switch Language BTN
switch_btn = tk.PhotoImage(file=r"img\switch.png")
switch_btn_lbl = tk.Button(main_root, image=switch_btn, border=False, cursor="hand2")
switch_btn_lbl.place(x=375, y=220)

# Background 2 for Surce Text
bg_two = tk.PhotoImage(file=r"img\bg.png")
bg_two_lbl = tk.Label(main_root, image=bg_one)
bg_two_lbl.place(x=10, y=80)

# Text Area for Destination text
text_dest = tk.Text(main_root, font=("Arial", 12), fg="black", border=False, bg="#F7F7F7")
text_dest.place(x=18, y=88, width=337, height=285)
main_root.mainloop()