# Import libraries
import os
import shutil


def organize_files(source_directory, destination_directory):
    # Get a list of files in the source directory
    files = os.listdir(source_directory)

    # Iterate through every file in the files variable
    for file in files:
        # Check if the iterated file is a file, and not a directory
        if os.path.isfile(os.path.join(source_directory, file)):
            file_extension = os.path.splitext(file)[1].lower() # Split the filename from the extension and convert it to lowercase, then save it to a variable

            # Define the destination folders based on file extensions (This can be changed for different applications)
            if file_extension == ".txt":
                destination_folder = "TextFiles"
            elif file_extension == ".jpg" or file_extension == ".png":
                destination_folder = "Images"
            elif file_extension == ".docx" or file_extension == ".xlsx" or file_extension == ".pptx":
                destination_folder = "Documents"
            else:
                # Transfer every other file into this folder
                destination_folder = "Miscellaneous"

            # Join the destination directory and the destination folder paths, and save it to a variable
            destination_path = os.path.join(destination_directory, destination_folder)
            # Create the destination folder if it doesn't exist using the combined paths
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)

            # Move the file to the destination folder
            source_path = os.path.join(source_directory, file)
            destination_file_path = os.path.join(destination_path, file)
            shutil.move(source_path, destination_file_path)
