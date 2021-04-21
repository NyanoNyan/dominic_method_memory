import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import pandas as pd
import mode_select
import timer
import time

class WindowSetUp:
    def __init__(self, window, isRand):
        self.window = window
        self.isRand = False
        self.mode = "r"
        self.count_order = 0
        self.window.title("Dominic Method Memory Tester")
        self.window.rowconfigure([0, 1, 2, 3, 4], minsize= 100, weight=1)
        self.window.columnconfigure([0, 1, 2, 3, 4], minsize= 150, weight=1)

        self.frame = tk.Frame(self.window)
        self.lower_range = tk.Entry(self.window, justify="center")
        self.upper_range = tk.Entry(self.window, justify="center")

        self.frame.grid(row=0, column=0, sticky="nsew")

        # For settings
        self.label_lower = tk.Label(text="Please enter a lower range:")
        self.label_upper = tk.Label(text="Please enter the upper range +1:")
        self.button_save_settings = tk.Button(text="Save settings", command=self.save_settings)
        self.lower_range.insert(0, "0")
        self.upper_range.insert(0, "21")
        self.main_menu_btn = tk.Button(text="Main Menu", command= self.main_screen, width=30)

        # For mode select
        self.mode_select = mode_select.ModeSelect(self.mode, self.lower_range.get(), self.upper_range.get())
        # For game to start
        self.label_number_game = tk.Label()
        self.person_value = tk.Label()
        self.action_value = tk.Label()

        self.next_button = tk.Button(text="Next", command= lambda: self.start_game(self.mode))

        self.data_values = pd.DataFrame()


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
        self.btn_rand_mode = tk.Button(text="Random Mode", command= lambda: self.start_game("r"), width=30)
        self.btn_order_mode = tk.Button(text="Ordered Mode", command= lambda: self.start_game("n"), width=30)
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
        self.label_number_game.grid_forget()
        self.action_value.grid_forget()
        self.person_value.grid_forget()
        self.next_button.grid_forget()

        # Reset count for game for normal mode
        self.count_order = 0
        # Add in form style to gather lower and upper values

        self.label_lower.grid(row=1, column=1, sticky="nswe")
        self.label_upper.grid(row=2, column=1, sticky="nswe")
        self.main_menu_btn.grid(row=4, column=2, sticky="nsew")

        self.lower_range.grid(row=1, column=2, sticky="nsew", padx=1, pady=1)
        self.upper_range.grid(row=2, column=2, sticky="nsew", padx=1, pady=1)
        self.button_save_settings.grid(row=3, column=2, sticky="nsew")

        self.mode_select = mode_select.ModeSelect(self.mode, self.lower_range.get(), self.upper_range.get())
    

        # print(self.lower_range.get())

    def save_settings(self):
        self.lower_range.get()
        self.upper_range.get()

    def start_game(self, event):

        if (self.data_values.empty):
            messagebox.showinfo(title="No data loaded", message="Please open your data file")
        else: 
            self.btn_rand_mode.grid_forget()
            self.btn_order_mode.grid_forget()
            self.screen_label.grid_forget()

            ## Change mode setting in ModeSelect Class
            self.mode = event
            self.mode_select.change_mode(self.mode)

            ## Show the number
            self.index_value = self.mode_select.give_values()
            self.label_number_game["text"] = str(self.index_value)
            self.label_number_game.grid(row=1, column=2, sticky="nsew")

                
            self.person_value.grid_forget()
            self.action_value.grid_forget()
            ## Show value and next button after 2 seconds
            self.window.after(2000, self.show_next_button)

    def show_next_button(self):

        if (self.mode == "r"):
            person_value = self.data_values.iloc[self.index_value+1, 3]
            action_value = self.data_values.iloc[self.index_value+1, 4]  
        else:
            self.item_count = int(self.mode_select.show_item_list()[0]) + 1
    
            person_value = self.data_values.iloc[self.count_order + self.item_count, 3]
            action_value = self.data_values.iloc[self.count_order + self.item_count, 4]  
            self.count_order += 1

        self.person_value["text"] = person_value
        self.action_value["text"] = action_value

        self.person_value.grid(row=2, column=2, sticky="nsew")
        self.action_value.grid(row=3, column=2, sticky="nsew")
        self.next_button.grid(row=4, column=2, sticky="nsew")


    def show_memory_data(self):
        return self.data_values

    def hide_settings_widgets(self):
        self.label_lower.grid_forget()
        self.label_upper.grid_forget()
        self.lower_range.grid_forget()
        self.upper_range.grid_forget()
        self.main_menu_btn.grid_forget()
        self.button_save_settings.grid_forget()

        self.label_number_game.grid_forget()
        self.action_value.grid_forget()
        self.person_value.grid_forget()
        self.next_button.grid_forget()
    
    def show_range_values(self):
        return self.lower_range.get(), self.upper_range.get()


def main():

    window=  tk.Tk()
    app = WindowSetUp(window, False)
    app.main_screen()
    window.resizable(False,False)
    window.mainloop()

if __name__ == "__main__":
    main()
