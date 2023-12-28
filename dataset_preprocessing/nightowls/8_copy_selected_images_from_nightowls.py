import json
import shutil
import os

def copy_images(json_file, source_folder, destination_folder):
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Copy images to the destination folder
    for image in data['images']:
        file_name = image['file_name']
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        # Copy the image file
        shutil.copy2(source_path, destination_path)

# Replace 'filtered_images.json', 'original_images_folder', and 'destination_folder' with your file names or paths
json_file = '5_filtered_after_sub_sampling_of_all_images_5611.json'
original_images_folder = '/Users/msmohamed/Desktop/fourth/final_project/pedestrian/pedestrian_detection/nightowls_training'
destination_folder = '/Users/msmohamed/Desktop/fourth/final_project/pedestrian/pedestrian_detection/final_nightowls_dataset/selected_images'

# Call the function to copy relevant images
copy_images(json_file, original_images_folder, destination_folder)
