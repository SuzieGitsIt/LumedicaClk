# File:     TkinterGUI_2023-03-14
# Version:  0.0.01
# Author:   Susan Haynes
# Comments/Notes: 
#   (0,0) coordinates are the top left corner of the screen for 1920x1080
#   (0,0) coordinates are the bottom right corner of the screen for 1919x1079
# Online References: 
#   https://pypi.org/project/PyAutoGUI/
#   https://pyautogui.readthedocs.io/en/latest/mouse.html
# Revision History: N/A 
# To check tkinter is installed, use this in command promt.
# python -m tkinter 


import tkinter as tk                                # Tkinter's Tk class
import tkinter.ttk as ttk                           # Tkinter's Tkk class
from PIL import ImageTk, Image  

GUI = tk.Tk()

GUI.geometry("450x250")                             # Set the geometry of Tkinter frame
GUI.configure(bg = 'green')

entry = tk.Entry(                                   # Create an Entry widget to accept User Input
    GUI, 
    bg = "blue",
    fg = "yellow",
    width= 25,
    font=("Helvetica 12 italic")
)
entry.focus_set()
entry.pack(pady=20)

def display_text():
   global entry
   string = entry.get()
   lbl_input.configure(text = string)

btn_lemon = tk.Button(                                 # Create a Button to validate Entry Widget
    GUI, 
    text="Click Me! Drink to Shrink. Eat to Grow.",
    bg = "blue",
    fg = "yellow",
    width= 35,
    height = 10,
    font=("Helvetica 12 italic"),
    command = display_text
).pack(pady=5)

lbl_input = tk.Label(                               # I nitialize a Label to display the User Input
    GUI, 
    text = "", 
    bg = "green",                                   # set the background color, hex works too "#FFFFFF"
    fg = "yellow",                                  # set the text color, hex works too "#FFFFFF"
    font=("Helvetica 22 bold")
)
lbl_input.pack(pady=5)

lbl_mustard = tk.Label(
    text="MUSTARD?!?! Don't let's be silly!",       # set the output text
    bg = "green",                                   # set the background color, hex works too "#FFFFFF"
    fg = "yellow",                                  # set the text color, hex works too "#FFFFFF"
    width = 50,                                     # set the width of text box, measured in text units '0'. 50 = 50 zeros wide
    height= 10,                                     # set the height of text box, measured in text units '0' 10 = 10 zeros high
    font=("Helvetica 12 bold")
) 
lbl_mustard.pack(pady=5)

image1 = Image.open("\\RXS-FS-02\userdocs\shaynes\My Documents\R&D - Software\Python\TkinterGUI_2023-03-14image_name\mustard01.png")
test = ImageTk.PhotoImage(image1)

lbl_photo = tkinter.Label(image = test)
lbl_photo.image = test
lbl_photo.place(x=250, y=125)

'''
lbl_initals = tk.Label(text="Enter Operator Initials: ", bg = "black", fg = "white", width = 40, height = 5)
ent_initials = tk.Entry(bg = "black", fg = "white", width = 40)

lbl_initials.pack()                                     # We want the text output first, so we put the pack first.
ent_initials.pack()                                  # We want the user entry of intitials second, so we put the pack second.
ent_initials.get()                                   # This doesnt seem to be getting anything.
'''
'''
frm_a = tk.Frame()
frm_b = tk.Frame()

lbl_a = tk.Label(master=frame_a, text="I'm in Frame A")
lbl_a.pack()

lbl_b = tk.Label(master=frame_a, text="I'm in Frame B")
lbl_b.pack()

frm_a.pack()
frm_b.pack()
'''

GUI.mainloop()                                # Must be at the end of the program in order for the application to run b/c windows is constantly updating