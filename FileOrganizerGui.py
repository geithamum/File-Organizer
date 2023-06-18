import tkinter as tk
from tkinter import filedialog
import FileOrganizerMainScript

def browse_source_button():
    source_directory = filedialog.askdirectory()
    source_directory_label.config(text=source_directory)
    return source_directory


def browse_destination_button():
    destination_directory = filedialog.askdirectory()
    destination_directory_label.config(text=destination_directory)
    return destination_directory

def organize_button():
    sourceDirectory = browse_source_button
    destinationDirectory = browse_destination_button
    if sourceDirectory and destinationDirectory:
        FileOrganizerMainScript.organize_files(sourceDirectory, destinationDirectory)
        status_label.config(text="Files organized successfully!")
    else:
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
