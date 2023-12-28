import json

def save_category_1_image_ids(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Identify images with only pedestrians (category 1)
    image_ids = [image['id'] for image in data['images']]

    # Save the category 1 image IDs to a new JSON file
    with open(output_file, 'w') as output:
        json.dump(image_ids, output, indent=2)

# Replace 'input.json' and 'output_category_1_ids.json' with your file names or paths
input_file = '4_filtere_after_sub_sampling_of_person_only.json'
output_file = 'all_the_image_ids_after_4th_json_file.json'
save_category_1_image_ids(input_file, output_file)
