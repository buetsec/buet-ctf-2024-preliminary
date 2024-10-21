
# Bong Bang Maze - Short Writeup

In this challenge, you are provided with an image named **`1. Treasure.jpg`**, which contains hidden information. To retrieve the hidden file, follow these steps:

## 1. Using StegSeek
Run **StegSeek** on the image file to extract the hidden content:
```bash
stegseek 1.\ Treasure.jpg
```
Output:
```
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "zarapatterson@81" 
[i] Original filename: "poem.txt".
[i] Extracting to "1. Treasure.jpg.out".
```

## 2. Analyzing `poem.txt`
Upon extraction, you will find a file named **`poem.txt`**. This file contains important hints about how the text has been embedded in the **alpha channel** of the image. The text is embedded in a **zig-zag pattern** within the alpha channel.

## 3. Extracting the Alpha Channel
To observe the hidden message, you need to extract the **alpha channel** from the image to detect the pattern. 

## solution code 

```


from PIL import Image

def unhide_text_from_alpha(image_path):
    """
    Extracts hidden text from the alpha channel of an image.
    
    Args:
        image_path (str): Path to the image containing hidden text.
    
    Returns:
        str: The extracted hidden text.
    """
    # Open the RGBA image
    image = Image.open(image_path)

    if image.mode != 'RGBA':
        print("Image is not in RGBA mode, cannot extract hidden data.")
        return ""

    # Get pixel data
    pixels = image.load()
    width, height = image.size

    # List to store extracted characters
    extracted_values = []

    # Process rows in pairs to extract text in a zigzag pattern
    for row in range(0, height, 2):
        if row + 1 >= height:
            break

        # Process columns in zigzag pairs with 10 pixel gap 
        for col in range(9, width + 1, 10):
            if (col + 1) % 20 != 0:
                # Extract the alpha value from the first row of the pair
                r1, g1, b1, a1 = pixels[col, row]
                extracted_values.append(255 - a1)
            else:
                # Extract the alpha value from the second row of the pair
                r2, g2, b2, a2 = pixels[col, row + 1]
                extracted_values.append(255 - a2)

    # Convert the extracted values back to text
    extracted_text = ''.join(chr(value) for value in extracted_values)
    print(f"Extracted Text: {extracted_text}")
    return extracted_text


image_path = '2. Maze.png'
print(unhide_text_from_alpha(image_path))

```




