import json

# Function to filter images based on category IDs and remove irrelevant annotations
def filter_images_and_annotations(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        images_to_remove = []

        # Identify images that don't contain category 1 or 2
        for idx, image in enumerate(data['images']):
            has_valid_category = False
            for annotation in data['annotations']:
                if annotation['image_id'] == image['id']:
                    if annotation['category_id'] in [1, 2]:
                        has_valid_category = True
                    elif annotation['category_id'] in [3, 4]:
                        data['annotations'].remove(annotation)

            if not has_valid_category:
                images_to_remove.append(image['id'])

            # Track progress every 10000 iterations
            if (idx + 1) % 100 == 0:
                print(f"Processed {idx + 1} images.")

        # Remove unwanted images from the 'images' object
        data['images'] = [image for image in data['images'] if image['id'] not in images_to_remove]

        return data

# Replace 'input.json' with your file name or path
input_file = 'filtered_data_for_night.json'
filtered_data = filter_images_and_annotations(input_file)

# Save the filtered data to a new file or perform any other operations needed
output_file = 'filtered_data_for_person_cyclist.json'
with open(output_file, 'w') as outfile:
    json.dump(filtered_data, outfile, indent=2)
