import os
import cv2
import numpy as np
from albumentations import HorizontalFlip, Rotate, BboxParams
from albumentations.core.composition import Compose

# Function to read labels from a file
def read_labels(label_file):
    with open(label_file, 'r') as file:
        lines = file.readlines()
    return [list(map(float, line.strip().split())) for line in lines]

# Function to write labels to a file
def write_labels(label_file, labels):
    with open(label_file, 'w') as file:
        for label in labels:
            file.write(' '.join(map(str, label)) + '\n')

# Function to convert bounding box coordinates to YOLO format
def convert_to_yolo_format(bbox, image_width, image_height):
    x_center, y_center, box_width, box_height = bbox
    x_center /= image_width
    y_center /= image_height
    box_width /= image_width
    box_height /= image_height
    return [x_center, y_center, box_width, box_height]

# Function to augment images and corresponding labels
def augment_dataset(image_folder, label_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    # Load original labels
    original_labels = [read_labels(os.path.join(label_folder, label_name)) for label_name in os.listdir(label_folder)]

    # Define augmentations
    transform = Compose([
        HorizontalFlip(p=0.7),
        Rotate(limit=10),
    ], bbox_params=BboxParams(format='yolo', label_fields=['category_ids']))

    for i, (image_name, labels) in enumerate(zip(os.listdir(image_folder), original_labels)):
        # Read image
        image_path = os.path.join(image_folder, image_name)
        image = cv2.imread(image_path)
        image_height, image_width, _ = image.shape

        # Convert bounding box coordinates to YOLO format
        labels_yolo = [[int(label[0])] + convert_to_yolo_format(label[1:], image_width, image_height) for label in labels]

        # Apply augmentations
        augmented = transform(image=image, bboxes=labels_yolo, category_ids=[int(label[0]) for label in labels])

        # Update augmented labels
        augmented_labels = [[int(label)] + bbox for label, bbox in zip(augmented['category_ids'], augmented['bboxes'])]

        # Ensure that coordinates are in the range (0, 1]
        for label in augmented_labels:
            if any(coord <= 0 or coord > 1 for coord in label[1:]):
                raise ValueError("In YOLO format, all coordinates must be float and in range (0, 1]")

        # Save augmented image
        augmented_image_path = os.path.join(output_folder, f"augmented_{i}_{image_name}")
        cv2.imwrite(augmented_image_path, augmented['image'])

        # Append augmented labels to the new label file
        augmented_label_file = os.path.join(output_folder, f"augmented_{i}_{os.path.splitext(image_name)[0]}.txt")
        write_labels(augmented_label_file, augmented_labels)

if __name__ == "__main__":
    # Specify your original dataset folders, label folder, and output folder
    original_image_folder = "images"
    original_label_folder = "labels"
    output_dataset_folder = "dataset"

    augment_dataset(original_image_folder, original_label_folder, output_dataset_folder)
