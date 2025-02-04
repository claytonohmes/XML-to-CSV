import tkinter as tk
from tkinter import filedialog
from able_config_to_csv_alarm_list import able_config_to_csv_alarm_list

selected_file_path = None  # Variable to store the selected file path
user_input_text = None  # Variable to store the user's input

def select_file():
    """Opens a file selection dialog and returns the selected file path."""
    filepath = filedialog.askopenfilename(
        initialdir=".", 
        filetypes=[("All files", "*.*")]
    )
    
    if filepath:
        file_path_label.config(text="Selected file: " + filepath)
        global selected_file_path
        selected_file_path = filepath
    else:
        file_path_label.config(text="No file selected")

def ok_button_pressed():
    """Handles the OK button press event."""
    global user_input_text
    user_input_text = user_input.get()
    
    if selected_file_path:
        print("File path:", selected_file_path)
        print("User input:", user_input_text)
        able_config_to_csv_alarm_list(selected_file_path, user_input_text + ".csv")
    else:
        print("No file selected to use")
    
    
    root.destroy()  # Close the main window

if __name__ == '__main__':

    # Create main window
    root = tk.Tk()
    root.title("File Selector")

    # Create a button to trigger file selection
    select_button = tk.Button(root, text="Select an ABLE IDCConfig", command=select_file)
    select_button.pack()

    # Label to display the selected file path
    file_path_label = tk.Label(root, text="")
    file_path_label.pack()

    # Create a label for the user input
    user_input_label = tk.Label(root, text="Enter a name for the alarm file, .csv will be automatically added. Do not add it:")
    user_input_label.pack()

    # Create an entry widget for user input
    user_input = tk.Entry(root)
    user_input.pack()

    # Create an OK button
    ok_button = tk.Button(root, text="OK", command=ok_button_pressed)
    ok_button.pack()

    # Run the main loop
    root.mainloop()