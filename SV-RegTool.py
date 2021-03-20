# SV-RegTool
# This python file is the primary controller for SV-RegTool

import Regression as reg
import tkinter
from tkinter import filedialog

file_found_flag = False

# Method for opening file explorer
def explorer():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("CSV Files",
                                                        "*.csv*"), ))
    # Change label contents
    if filename:
        explorer_label.configure(text="CSV File Selected:\n"+filename)
        file_found_flag = True
    else:
        explorer_label.configure(text="CSV File Selected:\nNone")
        file_found_flag = False

# Create window for UI
window = tkinter.Tk()
window.title('File Explorer')
window.geometry("700x500")
window.config(background = "darkcyan")

# Create UI Elements
padding_label = tkinter.Label(window, height = 1, background = "darkcyan")

explorer_label = tkinter.Label(window,
                            text = "Select a Single Variable Dataset (.csv file)",
                            width = 100, height = 4,
                            fg = "blue")

explorer_button = tkinter.Button(window,
                        text = "Browse Files", command = explorer)

# Layout UI Elements
padding_label.grid(column = 1, row = 1)
explorer_label.grid(column = 1, row = 2)
explorer_button.grid(column = 1, row = 3, pady = 10)
if file_found_flag:
    print("This is when the Data is processed and Displayed")

# Let the window wait for any events
window.mainloop()
