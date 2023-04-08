import os
from PIL import Image

# Define the input and output directories
ins = list(range(1, 10))
for i in ins:
    input_dir = r"C:\Users\Vikash\Desktop\Dataset\{}"
    formatted_input_dir = input_dir.format(str(i))

    output_dir = r"C:\Users\Vikash\Desktop\Dataset\output_{}"
    formatted_output_dir = output_dir.format(str(i))

    # Create the output directory if it doesn't exist
    if not os.path.exists(formatted_output_dir):
        os.makedirs(formatted_output_dir)
    
    # Loop through all the files in the input directory
    for file_name in os.listdir(formatted_input_dir):
    
        # Check if the file is a JPG or PNG image
        if file_name.endswith(".JPG") or file_name.endswith(".png"):
            # Open the image file
            image_path = os.path.join(formatted_input_dir, file_name)
            image = Image.open(image_path)
    
            # Convert the image to grayscale
            grayscale_image = image.convert("L")
    
            # Save the grayscale image to the output directory
            new_file_name = file_name.split(".")[0] + "_grayscale.jpg"
            new_file_path = os.path.join(formatted_output_dir, new_file_name)
            grayscale_image.save(new_file_path) 

    