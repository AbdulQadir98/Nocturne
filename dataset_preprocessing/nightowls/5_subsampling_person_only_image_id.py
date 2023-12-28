import json

def subsample_and_save(input_file, output_file, iterations):
    with open(input_file, 'r') as file:
        image_ids = json.load(file)

    original_list = []
    new_list = []
    final_original_list = []

    for iteration in range(iterations):

        for idx, image_id in enumerate(image_ids):
            if idx % 2 == 0:
                original_list.append(image_id)
            else:
                new_list.append(image_id)

        # Set the new_list as the image_ids for the next iteration
        original_list.sort()
        new_list.sort()
        image_ids = original_list
        final_original_list = original_list
        original_list = []

    # Save the original list to the output file
    with open(output_file.format(iteration, "original"), 'w') as output1:
        json.dump(final_original_list, output1, indent=2)

    # Save the new list to the output file
    with open(output_file.format(iteration, "new"), 'w') as output2:
        json.dump(new_list, output2, indent=2)

# Replace 'input_category_1_ids.json', 'output_iteration_{}_{}.json', and 3 with your file names or paths and number of iterations
input_file = 'all_the_image_ids_after_4th_json_file.json'
output_file_format = 'image_to_delete_after_final_sub_sampling.json'
iterations = 1
subsample_and_save(input_file, output_file_format, iterations)
