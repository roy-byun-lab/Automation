"""
File Organizer 

If you have lots of projects, then you know that your file system can get out of hand pretty quick.
The script sorts your files into folders based on type, automatically. It’s simple, but works for a clean workspace.

What You’ll Need:
    os library (For interacting with the operating system)
    shutil library (For moving files)
"""
import os
import shutil

# Path to the directory you want to organize
source_dir = "your_directory_path"

# Define file type categories
categories = {
    "Images": [".jpg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Documents": [".docx", ".txt"],
    "Spreadsheets": [".xls", ".csv"]
}

# Loop through all files in the source directory
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)
    
    if os.path.isfile(file_path):
        # Extracts the file extension and converts it to lowercase: the return value is a tuple of (filename, extension).
            # ex) os.path.splitext("example.txt") → ("example", ".txt")
        file_extension = os.path.splitext(filename)[1].lower()
        
        # Check the file extension and move to the appropriate folder
        for category, extensions in categories.items():
            if file_extension in extensions:
                category_path = os.path.join(source_dir, category)
                if not os.path.exists(category_path):
                    os.makedirs(category_path)

                    # Once the move is complete, the original file is deleted, and the file is created in the specified destination location.
                shutil.move(file_path, os.path.join(category_path, filename))
                
                print(f"Moved {filename} to {category}")
                break