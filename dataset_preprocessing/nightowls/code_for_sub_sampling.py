import os
import shutil

# Source and destination directories
source_directory = "sub_sampling_cyclists_2"  # Replace with the actual source directory
destination_directory = "sub_sampling_cyclists_3"  # Replace with the actual destination directory

# Create the destination directory if it doesn't exist
os.makedirs(destination_directory, exist_ok=True)

# Number of images to skip (e.g., every second image)
skip_count = 2

# Iterate through the files in the source directory
for root, _, files in os.walk(source_directory):
    for i, file_name in enumerate(files):
        if i % skip_count == 0:
            source_path = os.path.join(root, file_name)
            destination_path = os.path.join(destination_directory, file_name)
            shutil.copy(source_path, destination_path)

print("Selected images copied to:", destination_directory)
