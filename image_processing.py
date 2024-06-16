from PIL import Image
import os
import sys

def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        img = img.resize(size, Image.LANCZOS)
        img.save(output_path)

def convert_image_format(input_path, output_path, output_format):
    with Image.open(input_path) as img:
        img.save(output_path, format=output_format)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python image_processing.py <task>")
        sys.exit(1)
    
    task = sys.argv[1]

    input_path = "images/input.jpg"
    

    if not os.path.exists(input_path):
        print(f"Input file {input_path} does not exist.")
        sys.exit(1)

    if task == "resize":
        width = 600
        height = 600
        output_path = "images/resize-output.jpg"
        resize_image(input_path, output_path, (width, height))
        print(f"Resized image saved to: {output_path}")
    elif task == "convert":
        output_path = "images/convert-output.png"
        output_format = "PNG"
        convert_image_format(input_path, output_path, output_format)
        print(f"Resized image saved to: {output_path}")
    else:
        print("Unsupported task. Please use 'resize' or 'convert'.")
        sys.exit(1)
