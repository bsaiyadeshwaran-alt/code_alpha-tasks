
import os
import shutil

# Source folder
source_folder = "Images"

# Destination folder
destination_folder = "JPG_Files"

# Create source folder if it does not exist
if not os.path.exists(source_folder):
    os.makedirs(source_folder)
    print("Source folder created!")

# Create destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    print("Destination folder created!")

# Counter for moved files
moved_count = 0

print("\nStarting File Automation...")

# Read all files from source folder
for filename in os.listdir(source_folder):

    # Check whether the file is a JPG image
    if filename.lower().endswith(".jpg"):

        source_path = os.path.join(source_folder, filename)

        destination_path = os.path.join(
            destination_folder, filename
        )

        # Move the JPG file
        if os.path.isfile(source_path):

            # Avoid overwriting existing files
            if os.path.exists(destination_path):
                print("File already exists:", filename)
                continue

            shutil.move(source_path, destination_path)

            print("Moved:", filename)

            moved_count += 1

# Display final result
print("\n================================")
print("       FILE AUTOMATION")
print("================================")

print("Total JPG files moved:", moved_count)

print("Automation completed successfully!")
