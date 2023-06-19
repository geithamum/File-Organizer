# File Organizer

This project utilizes various Python libraries to automate organizing files.

### Libraries utilized:
    - os (Scans files, and lists directories)
    - tkinter (GUI)
    - shutil (Moves files)


### Future changes:

- More user-friendly GUI
- Allow users to edit the destination folders and file extensions in the GUI, rather than in the program
- Different sorting methods (Date/Time, Alphabetical)

    
## Design Process

**I faced many challenges in the development of this project, such as:**

- Ensuring the versatility of the scripts
- Integrating two separate scripts into each-other
- Determining which sorting method to use
- File collisions and conflicts, such as two files having the same name
- File type handling
- Fixing bugs


**How I got around these problems:**
- Allowing users to edit the source and destination directories, destination folders and file extensions, allowing the scripts to be more versatile and tailored to the user
- Deciding that one script would be strictly used for the GUI, and another script would be used for the main organization function
- Sorting files by extensions
- Replacing duplicate files to fix file collisions
- Iterating through the different files in the directory, and splitting the file extensions from the filenames.
- Using print statements to find where the bugs came from, thoroughly analyzing what's happening in the script, then coming up with a solution based on the information.

## Installation
**You must have Python installed. Make sure to select "Add Python to Path" in the installer.** [Install Python](https://www.python.org/downloads/)

1: After installing Python, go into Command Prompt if you're on Windows, or go to Terminal if you're on MacOS. Make sure to run as an administrator,

2: After opening your terminal, you now need to install the tkinter package by running this commands in the terminal. The other packages don't need to be installed, as they are included in Python's standard library. 

    pip install tk

3: Clone this Github repository by clicking "Code" on the top-right of the main page.

4: Inside the drop-down menu, click "Download as ZIP".

5: Extract the ZIP file.

6: To run the file, in the folder, right click on FileOrganizerGui.py and go to Open With > Python.

## Usage

1: To select the directory that has the files that you want to organize, click on "Select Source Directory".

2: To select the directory where the destination folders will be created, click on "Select Destination Directory"

3: Click "Organize Files". It may take a while depending on how many files you have.

4: The files will be sorted based on file extension into the corresponding folders. These folders will be located in the destination directory.


