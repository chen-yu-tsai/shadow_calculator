import cv2
import numpy as np

import os

def list_png_files():
    return [f for f in os.listdir() if f.endswith('.jpg')]

# Use the function on your directory
png_files = list_png_files()


def process_image(input_path, output_path):
    # Load the image
    image = cv2.imread(input_path)

    # Define the threshold color (converted to integer values)
    threshold_color = np.array([125, 128, 140], dtype=np.uint8)

    # Find all pixels that are darker than the threshold
    darker_pixels = np.all(image < threshold_color, axis=-1)

    # Color these pixels blue
    image[darker_pixels] = [255, 0, 0]

    # Calculate the percentage of pixels that are now blue
    blue_pixels = np.all(image == [255, 0, 0], axis=-1)
    percentage_blue = np.sum(blue_pixels) / (image.shape[0] * image.shape[1]) * 100

    # Add this percentage as text to the image
    cv2.putText(image, f"{percentage_blue:.2f}%", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Save the image
    cv2.imwrite(output_path, image)




for file in png_files:
    output = file.replace('.jpg', '-output.jpg')
    # Use the function on your image
    process_image(file, output)
    print("tasks completed!")
