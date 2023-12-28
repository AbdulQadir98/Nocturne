import json

# Function to remove unnecessary attributes in the JSON data
def clean_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

        # Removing unnecessary attributes in the 'images' object array
        for image in data['images']:
            image_keys = list(image.keys())
            for key in image_keys:
                if key not in ['daytime', 'file_name', 'id']:
                    del image[key]

        # Removing unnecessary attributes in the 'annotations' object
        for annotation in data['annotations']:
            annotation_keys = list(annotation.keys())
            for key in annotation_keys:
                if key not in ['bbox', 'category_id', 'image_id']:
                    del annotation[key]

        return data

# Replace 'input.json' with your file name or path
input_file = 'data.json'
cleaned_data = clean_json(input_file)

# Save the updated data to a new file or perform any other operations needed
output_file = 'cleaned_data.json'
with open(output_file, 'w') as outfile:
    json.dump(cleaned_data, outfile, indent=2)
