import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd

df = pd.DataFrame

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.csv"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    df = pd.read_csv(filepath)
    # data = pd.read_csv(filepath)
    txt_edit.insert(tk.END, df)
    # with open(filepath, "r") as input_file:
    #     text = input_file.read()
    #     txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def rand_test():
    txt_test.insert(tk.END, "hello")

window = tk.Tk()

window.title("Dominic Method Memory Tester")

window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure([1,2], minsize=500, weight=1)

txt_edit = tk.Text(window)
txt_edit.grid(row=0, column=1, sticky="nsew")
txt_test = tk.Text(window)
txt_test.grid(row=0, column=2, sticky="nsew")


fr_buttons = tk.Frame(window)
fr_buttons.grid(row=0, column=0, sticky="ns")

btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

btn_open_check = tk.Button(fr_buttons, text="Check", command=rand_test)
btn_open_check.grid(row=0, column=2, sticky="ew", padx=5, pady=5)



window.mainloop()