import json

# Load the updated JSON file
updated_json_file = 'updated_cyclists.json'  # Replace with the path to your updated JSON file
with open(updated_json_file, 'r') as file:
    updated_data = json.load(file)

# Count the number of image objects
num_image_objects = len(updated_data["images"])

print(f"Number of image objects in the updated JSON file: {num_image_objects}")
