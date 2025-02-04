import tkinter as tk
import os
from tkinter import filedialog
from Controller.get_site_name import get_site_name
from Controller.able_config_to_csv_alarm_list import able_config_to_csv_alarm_list
from Controller.able_config_to_csv_asset_list import able_config_to_csv_asset_list

selected_file_path = None  # Variable to store the selected file path
user_input_text = None  # Variable to store the user's input
radial_selection = None  # Variable to store the radial selection

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
    global user_input_text, radial_selection
    user_input_text = user_input.get()
    radial_selection = radio_var.get()
    
    if selected_file_path:
        print("File path:", selected_file_path)
        print("User input:", user_input_text)
        print("Radial selection:", radial_selection)
        site = get_site_name(selected_file_path)
        output_dir = os.path.join(".\\Output\\", site)

        # Check if the directory exists and create it if it does not
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        if radial_selection == 1:
            able_config_to_csv_asset_list(selected_file_path, output_dir + "\\" + user_input_text + "_assets.csv")
        else:
            able_config_to_csv_alarm_list(selected_file_path, output_dir + "\\" + user_input_text + "_alarms.csv")
    else:
        print("No file selected to use")
    
    root.destroy()  # Close the main window

def on_user_input_change(*args):
    """Enables the OK button if there is text in the user input entry."""
    if user_input.get().strip():
        ok_button.config(state=tk.NORMAL)
    else:
        ok_button.config(state=tk.DISABLED)

if __name__ == '__main__':

    # Create main window
    root = tk.Tk()
    root.title("File Selector")

    # Create a button to trigger file selection
    select_button = tk.Button(root, text="Select an ABLE IDCConfig", command=select_file)
    select_button.pack(pady=10)

    # Label to display the selected file path
    file_path_label = tk.Label(root, text="")
    file_path_label.pack(pady=10)

    # Create a label for the user input
    user_input_label = tk.Label(root, text="Enter a name for the file, .csv will be automatically added. Do not add it:")
    user_input_label.pack(pady=10)

    # Create an entry widget for user input
    user_input = tk.Entry(root)
    user_input.pack(pady=10)
    user_input.bind("<KeyRelease>", on_user_input_change)

    # Create a label for the radio buttons
    radio_label = tk.Label(root, text="Select an option:")
    radio_label.pack(pady=10)

    # Create a variable to store the radio button selection
    radio_var = tk.IntVar()
    radio_var.set(1)  # Set default value

    # Create a frame to hold the radio buttons
    radio_frame = tk.Frame(root)
    radio_frame.pack(pady=10)

    # Create radio buttons
    asset_radio = tk.Radiobutton(radio_frame, text="Asset List", variable=radio_var, value=1)
    asset_radio.pack(side=tk.LEFT, padx=5)

    alarm_radio = tk.Radiobutton(radio_frame, text="Alarm List", variable=radio_var, value=2)
    alarm_radio.pack(side=tk.LEFT, padx=5)

    # Create an OK button
    ok_button = tk.Button(root, text="OK", command=ok_button_pressed, state=tk.DISABLED)
    ok_button.pack(pady=10)

    # Run the main loop
    root.mainloop()