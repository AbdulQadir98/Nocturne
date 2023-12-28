import os
import random

# Set the paths to the images and labels folders
images_folder = 'images'
labels_folder = 'labels'

# Step 1: Shuffle image files in the "images" folder
image_files = os.listdir(images_folder)
random.shuffle(image_files)

# Step 2: Rename files in both "images" and "labels" folders
for i, image_file in enumerate(image_files, start=1):
    # Generate new file names with numbers
    new_image_name = f'train_{i}.png'
    new_label_name = f'train_{i}.txt'

    # Update image file name
    old_image_path = os.path.join(images_folder, image_file)
    new_image_path = os.path.join(images_folder, new_image_name)
    

    # Check if corresponding label file exists
    label_file = image_file.replace('.png', '.txt')
    old_label_path = os.path.join(labels_folder, label_file)
    if os.path.exists(old_label_path):
        # Update label file name
        new_label_path = os.path.join(labels_folder, new_label_name)
        os.rename(old_label_path, new_label_path)

        # Print the updated file names
        print(f'Renamed: {old_image_path} -> {new_image_path}')
        print(f'Renamed: {old_label_path} -> {new_label_path}')
    else:
        # Print only the image file name update
        print(f'Renamed: {old_image_path} -> {new_image_path}')
    os.rename(old_image_path, new_image_path)

print('Renaming completed.')
