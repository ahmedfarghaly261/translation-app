# Main GUI application

import tkinter as tk
from tkinter import ttk
from models.translation_model import Translator

translator = Translator(src_lang="ar", tgt_lang="en")

def translate():
    text = input_text.get("1.0", tk.END).strip()
    if selected_direction.get() == "Arabic to English":
        translator.set_languages("ar", "en")
    else:
        translator.set_languages("en", "ar")
    output = translator.translate(text)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, output)

def launch_gui():
    global input_text, output_text, selected_direction

    window = tk.Tk()
    window.title("Arabic-English Translator")
    window.geometry("600x400")

    selected_direction = tk.StringVar()
    selected_direction.set("Arabic to English")

    ttk.Label(window, text="Select Translation Direction:").pack(pady=5)
    ttk.OptionMenu(window, selected_direction, "Arabic to English", "Arabic to English", "English to Arabic").pack()

    ttk.Label(window, text="Input Text:").pack(pady=5)
    input_text = tk.Text(window, height=5, width=60)
    input_text.pack()

    ttk.Button(window, text="Translate", command=translate).pack(pady=10)

    ttk.Label(window, text="Translated Text:").pack(pady=5)
    output_text = tk.Text(window, height=5, width=60)
    output_text.pack()

    window.mainloop()