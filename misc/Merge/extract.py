import os
from PIL import Image
import piexif

def extract_comments_from_images(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Ensure we're only processing JPEG files and sort them
    image_files = sorted([f for f in files if f.lower().endswith(('.jpg', '.jpeg'))])
    
    comments = []
    
    for image_file in image_files:
        # Construct full file path
        image_path = os.path.join(folder_path, image_file)
        
        # Open image
        img = Image.open(image_path)
        
        # Load existing EXIF data
        if 'exif' in img.info:
            exif_dict = piexif.load(img.info['exif'])
            
            # Extract User Comment
            user_comment = exif_dict['Exif'].get(37510)  # 37510 is the UserComment tag
            
            if user_comment is not None:
                comments.append(user_comment.decode('utf-8', 'ignore').strip())
            else:
                comments.append('No comment found')
        else:
            comments.append('No EXIF data')

    return comments

# Usage
folder_path = '/home/sojib/CTF/testing/Merge/Merge'  # Your folder path
comments = extract_comments_from_images(folder_path)
final_string = ''.join(comments)
# Print the extracted comments
for idx, comment in enumerate(comments):
    print(f"Image {idx + 1}: {comment}")
print(final_string)
