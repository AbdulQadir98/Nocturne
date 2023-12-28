import json
import os

def coco_to_yolo(json_file, images_folder, output_folder):
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for image in data['images']:
        image_id = image['id']
        file_name = image['file_name']
        width = 1024
        height = 640

        # Create YOLO format label file
        label_file_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + '.txt')

        with open(label_file_path, 'w') as label_file:
            for annotation in data['annotations']:
                if annotation['image_id'] == image_id:
                    category_id = annotation['category_id']

                    # Replace category 1 with 0 and category 2 with 1
                    category_id = 0 if category_id == 1 else 1

                    bbox = annotation['bbox']

                    # Convert COCO bbox format (x, y, width, height) to YOLO format (x_center, y_center, width, height)
                    x_center = bbox[0] + bbox[2] / 2
                    y_center = bbox[1] + bbox[3] / 2
                    x_center /= width
                    y_center /= height
                    bbox_width = bbox[2] / width
                    bbox_height = bbox[3] / height

                    # Write YOLO format annotation to the label file
                    label_file.write(f"{category_id} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}\n")

# Replace 'filtered_images.json', 'original_images_folder', and 'yolo_labels' with your file names or paths
json_file = '5_filtered_after_sub_sampling_of_all_images_5611.json'
original_images_folder = '/Users/msmohamed/Desktop/fourth/final_project/pedestrian/pedestrian_detection/final_nightowls_dataset/selected_images'
output_folder = '/Users/msmohamed/Desktop/fourth/final_project/pedestrian/pedestrian_detection/final_nightowls_dataset/yolo_labels'

# Call the function to convert COCO to YOLO format and generate label files
coco_to_yolo(json_file, original_images_folder, output_folder)
