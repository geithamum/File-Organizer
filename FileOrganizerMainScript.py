import os
import shutil


def organize_files(source_directory, destination_directory):
    # Get a list of files in the source directory
    files = repr(os.listdir(source_directory))


    for file in files:
        if os.path.isfile(os.path.join(source_directory, file)):  # Only process files, not directories
            file_extension = os.path.splitext(file)[1]  # Get the file extension
            print('extensions split')
            # Define destination folders based on file types
            if file_extension == ".txt":
                destination_folder = "TextFiles"
            elif file_extension == ".jpg" or file_extension == ".png":
                destination_folder = "Images"
            elif file_extension == ".docx" or file_extension == ".xlsx" or file_extension == ".pptx":
                destination_folder = "Documents"


            else:
                destination_folder = "Miscellaneous"

            # Create the destination folder if it doesn't exist
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Move the file to the destination folder
            shutil.move(os.path.join(source_directory, file),
                        os.path.join(destination_directory, destination_folder, file))