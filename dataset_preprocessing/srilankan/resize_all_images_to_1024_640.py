import os
import cv2

# Define the target size (width, height)
target_width, target_height = 1024, 640  # Desired dimensions

# Input and output directories
input_directory = 'final_frames_output_folder_700'  # Replace with the path to your input folder
output_directory = 'output_directory'  # Replace with the path to your output folder

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Loop through the images in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.png') or filename.endswith('.jpg'):
        # Read the image
        image_path = os.path.join(input_directory, filename)
        img = cv2.imread(image_path)
        
        # Calculate the aspect ratio
        aspect_ratio = img.shape[1] / img.shape[0]

        # Calculate new width based on the aspect ratio
        new_width = int(aspect_ratio * target_height)

        # Crop or resize as needed
        if new_width > target_width:
            crop_width = new_width - target_width
            img = img[:, :-crop_width]
        elif img.shape[0] > target_height:
            crop_height = img.shape[0] - target_height
            img = img[crop_height:, :]

        # Resize the image
        resized_img = cv2.resize(img, (target_width, target_height))
        
        # Save the processed image to the output directory
        output_path = os.path.join(output_directory, filename)
        cv2.imwrite(output_path, resized_img)
