import json

def save_category_1_image_ids(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Identify images with only pedestrians (category 1)
    category_1_images = [image['id'] for image in data['images'] if all(
        annotation['category_id'] == 1 for annotation in data['annotations'] if annotation['image_id'] == image['id']
    ) and not any(
        annotation['category_id'] == 2 for annotation in data['annotations'] if annotation['image_id'] == image['id']
    )]

    # Save the category 1 image IDs to a new JSON file
    with open(output_file, 'w') as output:
        json.dump(category_1_images, output, indent=2)

# Replace 'input.json' and 'output_category_1_ids.json' with your file names or paths
input_file = 'filtered_data_for_person_cyclist_final.json'
output_file = 'output_category_1_ids.json'
save_category_1_image_ids(input_file, output_file)
