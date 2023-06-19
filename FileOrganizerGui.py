# Import tkinter and the main script
import tkinter as tk
from tkinter import filedialog
import FileOrganizerMainScript

def browse_source_button():
    global source_directory # Open the source_directory variable for use in other functions
    source_directory = filedialog.askdirectory() # Ask for the directory, then save it to a variable
    source_directory_label.config(text=source_directory) # Show the source directory below the selection button
    return source_directory # Return the source directory

def browse_destination_button():
    global destination_directory # Open the destination_directory variable for use in other functions
    destination_directory = filedialog.askdirectory() # Ask for the directory, then save it to a variable
    destination_directory_label.config(text=destination_directory) # Show the destination directory below the selection button
    return destination_directory # Return the destination directory

def organize_button():
    global source_directory, destination_directory # Get the source_directory and destination_directory variables
    if source_directory and destination_directory: # Check if the user selected the directories

        # Execute the organize_files function in the main script using the source and destination directories as arguments
        FileOrganizerMainScript.organize_files(source_directory, destination_directory)
        # Display a message
        status_label.config(text="Files organized successfully!")
    else:
        # Display a message
        status_label.config(text="Please select both source and destination directories.")


# Create the GUI window
window = tk.Tk()
window.title("File Organization Tool")
window.geometry("400x250")

# Create the browse button and label for source directory selection
browse_source_button = tk.Button(window, text="Select Source Directory", command=browse_source_button)
browse_source_button.pack(pady=10)
source_directory_label = tk.Label(window, text="No source directory selected")
source_directory_label.pack()

# Create the browse button and label for destination directory selection
browse_destination_button = tk.Button(window, text="Select Destination Directory", command=browse_destination_button)
browse_destination_button.pack(pady=10)
destination_directory_label = tk.Label(window, text="No destination directory selected")
destination_directory_label.pack()

# Create the organize button
organize_button = tk.Button(window, text="Organize Files", command=organize_button)
organize_button.pack(pady=10)

# Create the status label
status_label = tk.Label(window, text="")
status_label.pack(pady=10)

# Start the GUI event loop
window.mainloop()
