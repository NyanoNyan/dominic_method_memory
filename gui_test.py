import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import pandas as pd


class WindowSetUp:
    def __init__(self, window):
        self.window = window
        self.window.title("Dominic Method Memory Tester")
        self.window.rowconfigure([0, 1, 2, 3, 4], minsize= 100, weight=1)
        self.window.columnconfigure([0, 1, 2, 3, 4], minsize= 100, weight=1)

        self.frame = tk.Frame(self.window)
        self.lower_range = tk.Entry(self.window, justify="center")
        self.upper_range = tk.Entry(self.window, justify="center")

        self.frame.grid(row=0, column=0, sticky="nsew")

        # For settings
        self.label_lower = tk.Label(text="Please enter a lower range:")
        self.label_upper = tk.Label(text="Please enter the upper range +1:")
        self.main_menu_btn = tk.Button(text="Main Menu", command= self.main_screen, width=30)

        self.data_values = pd.DataFrame()
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
        self.data_values = df
        self.window.title(f"Simple Text Editor - {filepath}")
    
    def rand_test(self):
        self.clear_test()
        print(self.show_memory_data().head())
    
    def clear_test(self):
        self.btn_open.grid_forget()
        print(self.show_memory_data().head())


    def main_screen(self):

        self.hide_settings_widgets()
        self.screen_label = tk.Label(text="Welcome to the Dominic Number Method Trainer")
        self.btn_open = tk.Button(self.frame, text="Open", command= self.open_file)
        self.btn_rand_mode = tk.Button(text="Random Mode", command= self.gather_number_range, width=30)
        self.btn_order_mode = tk.Button(text="Ordered Mode", command= self.rand_test, width=30)
        self.btn_settings = tk.Button(text="Settings", command= self.settings_menu, width=10)

        self.screen_label.grid(row=0, column=2, sticky="nsew")
        self.btn_open.grid(row=0, column=0, sticky="n", padx=5, pady=5)
        self.btn_rand_mode.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)
        self.btn_order_mode.grid(row=1, column=3, sticky="nsew", padx=5, pady=5)
        self.btn_settings.grid(row=0, column=4, sticky="nsew", padx=5, pady=5)

    def settings_menu(self):
        # Clear unnecessary buttons
        self.btn_rand_mode.grid_forget()
        self.btn_order_mode.grid_forget()
        self.screen_label.grid_forget()

        # Add in form style to gather lower and upper values


        self.label_lower.grid(row=1, column=1, sticky="nswe")
        self.label_upper.grid(row=2, column=1, sticky="nswe")
        self.main_menu_btn.grid(row=4, column=2, sticky="nsew")

        self.lower_range.grid(row=1, column=2, sticky="nsew", padx=1, pady=1)
        self.upper_range.grid(row=2, column=2, sticky="nsew", padx=1, pady=1)

    def gather_number_range(self):

        if (self.data_values.empty):
            messagebox.showinfo(title="No data loaded", message="Please open your data file")
        else: 
            self.btn_rand_mode.grid_forget()
            self.btn_order_mode.grid_forget()
            self.screen_label.grid_forget()

            label = tk.Label(text="Please select lower range")
            nxt_button = tk.Button(text="Next")

            label.grid(row=0, column=2, sticky="nsew")
            nxt_button.grid(row=3, column=2, sticky="nsew")
            self.lower_range.grid(row=1, column=2, sticky="nsew", padx=1, pady=1)

    def show_memory_data(self):
        return self.data_values

    def hide_settings_widgets(self):
        self.label_lower.grid_forget()
        self.label_upper.grid_forget()
        self.lower_range.grid_forget()
        self.upper_range.grid_forget()
        
        self.main_menu_btn.grid_forget()

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

# https://stackoverflow.com/questions/16115378/tkinter-example-code-for-multiple-windows-why-wont-buttons-load-correctly
# https://stackoverflow.com/questions/53256356/hide-a-button-in-tkinter