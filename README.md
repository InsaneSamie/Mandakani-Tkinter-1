# Mandakani-Tkinter-1
## Overview

Mandakani is a GUI-based application developed using Python's `tkinter` library. This application is designed to provide a comprehensive interface with various features accessible through a menu-driven approach. Additionally, it demonstrates the ability to integrate custom images and handle console messages within the GUI.

https://github.com/InsaneSamie/Mandakani-Tkinter-1/assets/101932418/ff43b0c7-0827-4de6-b2c1-acae64c8277a

## Features

1. **Main Menu**: The application features a robust menu system with several sub-menus including File, Edit, View, Generate, Export, and Help. Each menu item is linked to a function that can be customized for specific actions.

2. **Profile Icon**: A profile icon is placed in the top-right corner of the application window, which is added using the PIL (Python Imaging Library) to handle image resizing and formatting.

3. **Console Output**: The application includes a console output area where messages can be added dynamically from different parts of the GUI.

4. **Split Pane Layout**: The main window is divided into two sections (left and right boxes), each containing buttons to interact with the console.

5. **Web Browser Integration**: There is a separate script (1.py) that demonstrates how to open a web browser from the application to display an HTML file.

## File Structure

- **2.py**: The main application script which sets up the GUI, menus, profile icon, console, and interactive buttons.
- **1.py**: A script that opens a specific HTML file in the default web browser.
- **Images**: Directory containing the profile icon image.

## Dependencies

- Python 3.x
- `tkinter`
- `Pillow` (PIL)

## Setup Instructions

1. **Install Python**: Ensure Python 3.x is installed on your system.
2. **Install Dependencies**: Install the required libraries using pip:
   ```bash
   pip install tkinter Pillow
   ```
3. **Place Images**: Ensure the profile icon image is placed at the specified path:
   ```
   c:/Users/winne/Desktop/DID INTERN/CDAC/Project 2/Code/Python tkinter/Login/logo.png
   ```
4. **Run the Application**:
   - To run the main application, execute:
     ```bash
     python 2.py
     ```
   - To open the web browser with the HTML file, execute:
     ```bash
     python 1.py
     ```

## Code Explanation

### 2.py (Main Application)

- **Imports and Setup**:
  ```python
  from tkinter import *
  import tkinter as tk
  from tkinter import ttk, PhotoImage
  from PIL import Image, ImageTk
  ```
  These lines import the necessary libraries for GUI creation and image handling.

- **Window Configuration**:
  ```python
  root = Tk()
  root.geometry("800x600")
  root.title("Mandakani")
  ```
  This initializes the main application window with specified dimensions and title.

- **Menu Functions**: Functions like `myfunc1`, `myfunc2`, etc., are placeholders for menu actions, currently configured to print messages to the console.

- **Console Function**:
  ```python
  def add_to_console(message):
      console_text.insert(tk.END, message + "\n")
      console_text.see(tk.END)
  ```
  This function adds messages to the console text widget.

- **Profile Icon**: The profile icon image is loaded, resized, and displayed in the top-right corner of the application window.

- **Menu Setup**:
  ```python
  mainmenu = Menu(root)
  ```
  Various menus and sub-menus are created and added to the main menu.

- **Layout**: The window is divided into frames and sub-frames to organize the layout, with buttons added to demonstrate console interactions.

### 1.py (Web Browser Integration)

- **Imports and Setup**:
  ```python
  import webbrowser
  from tkinter import *
  ```
  This script uses the `webbrowser` module to open an HTML file.

- **Window Configuration**:
  ```python
  root = Tk()
  root.title("WebBrowsers")
  root.geometry("800x600")
  ```
  Initializes a simple window setup.

- **Open Web Browser**:
  ```python
  webbrowser.open("file:///C:/Users/winne/Desktop/DID%20INTERN/CDAC/Project%202/Code/Python%20tkinter/Login/Login%20Page.html")
  ```
  Opens the specified HTML file in the default web browser.

## Usage

1. **Navigate Menus**: Use the menu options to trigger various commands (currently print messages to the console).
2. **Interact with Console**: Use buttons in the left and right boxes to add messages to the console.
3. **Profile Icon**: Click on the profile icon (though currently it has no action).
4. **Web Browser**: Run `1.py` to open a local HTML file in the default web browser.

## Conclusion

This application serves as a template for creating sophisticated GUI applications with Python `tkinter`. It demonstrates key functionalities such as menu handling, image integration, and dynamic console output, providing a foundation for further development and customization.
