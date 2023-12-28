import json

def delete_images_and_annotations(input_file, image_ids_to_delete, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Filter out images and annotations to delete
    updated_images = [image for image in data['images'] if image['id'] not in image_ids_to_delete]
    updated_annotations = [annotation for annotation in data['annotations'] if annotation['image_id'] not in image_ids_to_delete]

    # Update the 'images' and 'annotations' objects in the data
    data['images'] = updated_images
    data['annotations'] = updated_annotations

    # Save the updated data to the output file
    with open(output_file, 'w') as output:
        json.dump(data, output, indent=2)

# Replace 'input.json', 'output.json', and 'image_ids_to_delete.json' with your file names or paths
input_file = '4_filtered_after_sub_sampling_of_person_only_11222.json'
output_file = '5_filtered_after_sub_sampling_of_all_images_5611.json'
image_ids_to_delete_file = 'image_to_delete_after_final_sub_sampling.json'

# Load the image IDs to delete from the file
with open(image_ids_to_delete_file, 'r') as file:
    image_ids_to_delete = json.load(file)

# Call the function to delete images and annotations
delete_images_and_annotations(input_file, image_ids_to_delete, output_file)
