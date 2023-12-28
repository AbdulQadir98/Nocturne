import json

# Function to filter out 'daytime: night' in images and remove corresponding annotations
def filter_and_clean_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        images_to_remove = []
        annotations_to_remove = []

        # Identify images with 'daytime' as 'night' and collect their IDs
        for image in data['images']:
            if image['daytime'] != 'night':
                images_to_remove.append(image['id'])

        # Identify annotations related to images to be removed and collect their indices
        annotations_to_remove_indices = []
        for i, annotation in enumerate(data['annotations']):
            if annotation['image_id'] in images_to_remove:
                annotations_to_remove_indices.append(i)

        # Remove unwanted images from the 'images' object
        data['images'] = [image for image in data['images'] if image['id'] not in images_to_remove]

        # Remove unwanted annotations from the 'annotations' object using collected indices
        data['annotations'] = [annotation for i, annotation in enumerate(data['annotations']) if i not in annotations_to_remove_indices]

        return data

# Replace 'input.json' with your file name or path
input_file = 'cleaned_attribute_data.json'
filtered_data = filter_and_clean_json(input_file)

# Save the filtered data to a new file or perform any other operations needed
output_file = 'filtered_data.json'
with open(output_file, 'w') as outfile:
    json.dump(filtered_data, outfile, indent=2)
