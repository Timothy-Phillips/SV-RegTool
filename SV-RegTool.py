# SV-RegTool
# This simple program allows users to select a single variable dataset (.csv)
# and have it and an adjustable regression model displayed. It will also allow
# users to query the model for predictions once the model is prepared.

import tkinter
from tkinter import filedialog

# Method for opening file explorer
def explorer():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("CSV Files",
                                                        "*.csv*"), ))
    # Change label contents
    if filename:
        explorer_label.configure(text="CSV File Selected:\n"+filename)
    else:
        explorer_label.configure(text="CSV File Selected:\nNone")

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

# Let the window wait for any events
window.mainloop()
