import os
import shutil

# Source and destination folders
source_folder = "source_folder"
destination_folder = "destination_folder"

# Get all files from source folder
files = os.listdir(source_folder)

# Move only JPG files
for file in files:

    if file.endswith(".jpg"):

        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)

        print(f"Moved: {file}")

print("\n All JPG files moved successfully!")
