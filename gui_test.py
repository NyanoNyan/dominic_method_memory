import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd


class WindowSetUp:
    def __init__(self, window):
        self.window = window
        self.window.title("Dominic Method Memory Tester")
        self.window.rowconfigure([0, 1, 2, 3, 4], minsize= 100, weight=1)
        self.window.columnconfigure([0, 1, 2, 3], minsize= 100, weight=1)

        self.frame = tk.Frame(self.window)
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.data_values = tk.Text(self.window)
        # self.txt_edit = tk.Text(self.window)
        # self.txt_test = tk.Text(self.window)
        # self.txt_test.grid(row=0, column=2, sticky="nsew")

    def open_file(self):
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.csv"), ("All Files", "*.*")]
        )
        if not filepath:
            return

        df = pd.read_csv(filepath)
        # print(df)
        # data = pd.read_csv(filepath)
        self.data_values.insert(tk.END, df)
        # with open(filepath, "r") as input_file:
        #     text = input_file.read()
        #     txt_edit.insert(tk.END, text)
        self.window.title(f"Simple Text Editor - {filepath}")
    
    def rand_test(self):
        self.clear_test()
    
    def clear_test(self):
        self.btn_open.grid_forget()

    def main_screen(self):
        self.screen_label = tk.Label(text="Welcome to the Dominic Number Method Trainer")
        self.btn_open = tk.Button(self.frame, text="Open", command= self.open_file)
        self.btn_rand_mode = tk.Button(text="Random Mode", command= self.rand_test, width=30)
        self.btn_order_mode = tk.Button(text="Ordered Mode", command= self.rand_test, width=30)

        self.screen_label.grid(row=0, column=1, sticky="nsew")
        self.btn_open.grid(row=0, column=0, sticky="n", padx=5, pady=5)
        self.btn_rand_mode.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        self.btn_order_mode.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

    def memory_data(self):
        return self.data_values.get("1.0", tk.END)
        

def main():
    window=  tk.Tk()
    app = WindowSetUp(window)
    app.main_screen()
    window.mainloop()

if __name__ == "__main__":
    main()


# window = tk.Tk()


# window.title("Dominic Method Memory Tester")

# window.rowconfigure(0, minsize=500, weight=1)
# window.columnconfigure([1,2], minsize=100, weight=1)

# txt_edit = tk.Text(window)
# txt_test = tk.Text(window)
# txt_test.grid(row=0, column=2, sticky="nsew")


# fr_buttons = tk.Frame(window)
# fr_buttons.grid(row=0, column=0, sticky="ns")

# btn_open = tk.Button(fr_buttons, text="Open", command= open_file)
# btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

# btn_open_check = tk.Button(fr_buttons, text="Check", command=rand_test)
# btn_open_check.grid(row=0, column=2, sticky="ew", padx=5, pady=5)



# window.mainloop()