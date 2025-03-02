import cv2
import numpy as np
import os

folderA = "images"
folderB = "masks"
folderC = "colmap_dataset"

os.makedirs(folderC, exist_ok=True)

for image_set in os.listdir(folderA):
    image_folder = os.path.join(folderA, image_set)
    mask_folder = os.path.join(folderB, image_set)
    output_folder = os.path.join(folderC, image_set)

    if not os.path.isdir(image_folder):
        continue

    os.makedirs(output_folder, exist_ok=True)

    for image_name in os.listdir(image_folder):
        if not image_name.endswith(('.png', '.jpg', '.jpeg')):
            continue

        image_path = os.path.join(image_folder, image_name)
        mask_name = os.path.splitext(image_name)[0] + ".png"
        mask_path = os.path.join(mask_folder, mask_name)
        output_path = os.path.join(output_folder, mask_name)

        rgb = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
        
        #mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]

        # Convert mask to alpha channel
        #alpha_channel = mask.astype(np.uint8)

        # Merge RGB image with alpha channel
        #rgba_image = cv2.merge((rgb[..., 0], rgb[..., 1], rgb[..., 2], alpha_channel))
        rgba_image = cv2.bitwise_and(rgb, rgb, mask=mask)

        # Save the RGBA image in the output folder
        cv2.imwrite(output_path, rgba_image)
        print(f"Saved: {output_path}")

print("Processing complete!")

    