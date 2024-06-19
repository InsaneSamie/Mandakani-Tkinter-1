from tkinter import *
import tkinter as tk
from tkinter import ttk, PhotoImage
from PIL import Image, ImageTk

root = Tk()
root.geometry("800x600")
root.title("Mandakani")

def myfunc1():
    print("Hello! Sub-menu of File is successful created!")

def myfunc2():
    print("Hello! Sub-menu of Edit is successful created!")

def myfunc3():
    print("Hello! Sub-menu of View is successful created!")

def myfunc4():
    print("Hello! Sub-menu of Generate is successful created!")

def myfunc5():
    print("Hello! Sub-menu of Export is successful created!")

def myfunc6():
    print("Hello! Sub-menu of Help is successful created!")

def add_to_console(message):
    console_text.insert(tk.END, message + "\n")
    console_text.see(tk.END) 

# Load and resize the profile icon image using PIL
profile_image = Image.open("c:/Users/winne/Desktop/DID INTERN/CDAC/Project 2/Code/Python tkinter/Login/logo.png")
profile_image = profile_image.resize((40, 40),  Image.Resampling.LANCZOS)
profile_icon = ImageTk.PhotoImage(profile_image)


# Create the main menu
mainmenu = Menu(root)

m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New Text File", command=myfunc1)
m1.add_command(label="New File", command=myfunc1)
m1.add_command(label="New Window", command=myfunc1)
m1.add_separator()
m1.add_command(label="Open File", command=myfunc1)
m1.add_command(label="Open Folder", command=myfunc1)
m1.add_command(label="Open Workspace from File", command=myfunc1)
m1.add_command(label="Open Recent", command=myfunc1)
m1.add_separator()
m1.add_command(label="Add Folder to Workspace", command=myfunc1)
m1.add_command(label="Save Workspace As", command=myfunc1)
m1.add_command(label="Duplicate Workspace", command=myfunc1)
m1.add_separator()
m1.add_command(label="Save", command=myfunc1)
m1.add_command(label="Save As", command=myfunc1)
m1.add_command(label="Save All", command=myfunc1)
m1.add_command(label="Auto Save", command=myfunc1)
m1.add_command(label="Print", command=myfunc1)
m1.add_separator()
m1.add_command(label="Share", command=myfunc1)
m1.add_separator()
m1.add_command(label="Revert File", command=myfunc1)
m1.add_command(label="Close Folder", command=myfunc1)
m1.add_command(label="Close Window", command=myfunc1)
m1.add_command(label="Exit", command=quit)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Undo", command=myfunc2)
m2.add_command(label="Redo", command=myfunc2)
m2.add_separator()
m2.add_command(label="Cut", command=myfunc2)
m2.add_command(label="Copy", command=myfunc2)
m2.add_command(label="Paste", command=myfunc2)
m2.add_separator()
m2.add_command(label="Find", command=myfunc2)
m2.add_command(label="Replace", command=myfunc2)
m2.add_separator()
m2.add_command(label="Find in Files", command=myfunc2)
m2.add_command(label="Replace in Files", command=myfunc2)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Open View", command=myfunc3)
m3.add_separator()
m3.add_command(label="Appearance", command=myfunc3)
m3.add_command(label="Editor Layout", command=myfunc3)
m3.add_separator()
m3.add_command(label="Explorer", command=myfunc3)
m3.add_command(label="Search", command=myfunc3)
m3.add_command(label="Source Control", command=myfunc3)
m3.add_command(label="Run", command=myfunc3)
m3.add_command(label="Extensions", command=myfunc3)
m3.add_separator()
m3.add_command(label="Problems", command=myfunc3)
m3.add_command(label="Output", command=myfunc3)
m3.add_separator()
m3.add_command(label="Word Wrap", command=myfunc3)

m4 = Menu(mainmenu, tearoff=0)
m4.add_command(label="Generate File", command=myfunc4)

m5 = Menu(mainmenu, tearoff=0)
m5.add_command(label="Export File", command=myfunc5)

m6 = Menu(mainmenu, tearoff=0)
m6.add_command(label="Welcome", command=myfunc6)
m6.add_separator()
m6.add_command(label="Show All Commands", command=myfunc6)
m6.add_command(label="Documentation", command=myfunc6)
m6.add_command(label="Show Release Notes", command=myfunc6)
m6.add_separator()
m6.add_command(label="Keyboard Shortcut Reference", command=myfunc6)
m6.add_command(label="Video Tutorials", command=myfunc6)
m6.add_command(label="Tips and Tricks", command=myfunc6)
m6.add_separator()
m6.add_command(label="Join Us on YouTube", command=myfunc6)
m6.add_command(label="Search Feature Requests", command=myfunc6)
m6.add_command(label="Report Issue", command=myfunc6)
m6.add_separator()
m6.add_command(label="View License", command=myfunc6)
m6.add_command(label="Privacy Statement", command=myfunc6)
m6.add_separator()
m6.add_command(label="Check for Updates", command=myfunc6)
m6.add_separator()
m6.add_command(label="About", command=myfunc6)

root.config(menu=mainmenu)

mainmenu.add_cascade(label="File", menu=m1)
mainmenu.add_cascade(label="Edit", menu=m2)
mainmenu.add_cascade(label="View", menu=m3)
mainmenu.add_cascade(label="Generate",menu=m4)
mainmenu.add_cascade(label="Export",menu=m5)
mainmenu.add_cascade(label="Help", menu=m6)

# Create a frame for the top part of the window (to contain the two boxes)
top_frame = ttk.Frame(root, padding="10")
top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create two frames inside the top frame for the contained boxes
left_box = ttk.Frame(top_frame, height=400, borderwidth=2, relief="sunken", padding="10")
right_box = ttk.Frame(top_frame, height=400, borderwidth=2, relief="sunken", padding="10")

# Pack the contained boxes side by side with different padx values
left_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 5))
right_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a frame for the profile icon in the top right corner
profile_frame = ttk.Frame(root)
profile_frame.place(relx=1.0, rely=0.0, anchor='ne')  # Placing it at the top-right corner

# Add profile icon to the profile frame
profile_button = ttk.Button(profile_frame, image=profile_icon)
profile_button.pack(pady=10, padx=10)

# Create a text widget for the console output
console_frame = ttk.Frame(root, padding="10")
console_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

console_text = tk.Text(console_frame, height=2, wrap="word", borderwidth=2, relief="sunken")
console_text.pack(fill=tk.BOTH, expand=True)

# Add a button to each box to demonstrate adding messages to the console
btn_left = ttk.Button(left_box, text="Add to Console from Left Box", command=lambda: add_to_console("Message from Left Box"))
btn_right = ttk.Button(right_box, text="Add to Console from Right Box", command=lambda: add_to_console("Message from Right Box"))

btn_left.pack(pady=200)
btn_right.pack(pady=200)

root.mainloop()