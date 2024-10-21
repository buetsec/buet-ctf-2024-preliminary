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

        # Process columns in zigzag pairs
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

"""
# Steganography Tools: A Comprehensive Guide for CTF Competitions

Steganography is a fascinating technique that allows users to conceal information within various types of media, such as images, audio, and video files. For participants in Capture The Flag (CTF) competitions, understanding and using steganography tools can provide a significant advantage when it comes to finding hidden flags. In this article, we'll explore several popular steganography tools, their features, and how to use them effectively.

## 1. Steghide

**Overview**:  
Steghide is a command-line tool designed for hiding data within various types of media files, including JPEG, BMP, WAV, and AU formats. It uses a robust algorithm to embed data in a way that is difficult to detect.

**Key Features**:
- **Support for Multiple Formats**: Hides data in images (JPEG, BMP) and audio files (WAV, AU).
- **Password Protection**: Allows users to encrypt hidden data using a password.
- **Extraction Capabilities**: Can extract hidden data from files that were previously used for embedding.

**Usage**:
To hide data using Steghide:
```bash
steghide embed -cf cover_image.jpg -ef secret.txt -p your_password
```

To extract data:
```bash
steghide extract -sf cover_image.jpg -p your_password
```

**Tips**:
- Always try various file formats when searching for hidden data.
- Test different passwords if you suspect data might be protected.

---

## 2. StegSolve

**Overview**:  
StegSolve is a versatile tool primarily used for analyzing images for hidden data. It provides various image manipulation techniques that can help in revealing concealed information.

**Key Features**:
- **Image Analysis**: Allows users to perform operations like color channel manipulation, bit manipulation, and pixel analysis.
- **Ease of Use**: Offers a graphical user interface (GUI) for straightforward navigation.
- **Hex and ASCII View**: Can display the hex and ASCII representation of image data.

**Usage**:
StegSolve is a standalone Java application. Simply download it, run it, and open your target image. Use the various functions available in the GUI to analyze the image.

**Tips**:
- Explore each image channel to find hidden data.
- Use the “Extract” feature to pull pixel values and analyze them for patterns.

---

## 3. StegSeek

**Overview**:  
StegSeek is a specialized tool that focuses on identifying hidden data in files that use steganography. It works by scanning files for known steganography techniques.

**Key Features**:
- **File Type Agnostic**: Can analyze any file type to detect hidden data.
- **Supports Multiple Techniques**: Uses various algorithms to search for hidden messages.
- **Command Line Interface**: Operates through command-line commands for flexibility and automation.

**Usage**:
To use StegSeek, run the following command:
```bash
stegseek cover_image.jpg /path/to/directory/
```

**Tips**:
- Use it in combination with other tools like Steghide for better detection results.
- Analyze multiple files to improve chances of finding hidden data.

---

## 4. OpenStego

**Overview**:  
OpenStego is a user-friendly tool for data hiding and watermarking. It is open-source and supports various image formats.

**Key Features**:
- **Data Hiding**: Allows users to embed data in images easily.
- **Watermarking**: Offers watermarking features to protect images.
- **GUI Support**: Provides a graphical interface, making it accessible for beginners.

**Usage**:
To hide data with OpenStego:
1. Open the application.
2. Select “Data Hiding.”
3. Choose the cover image and the file to hide, then specify output filename.

To extract data:
1. Select “Data Extraction.”
2. Choose the image with the hidden data and specify the output filename.

**Tips**:
- Test the output file visually to ensure it appears unchanged.
- Use the watermarking feature to protect your own images.

---

## 5. S-tools

**Overview**:  
S-tools is another command-line based tool used for hiding data in bitmap images. It is known for its simplicity and effectiveness.

**Key Features**:
- **Bitmap Format Support**: Works exclusively with BMP files.
- **Fast Processing**: Embeds and extracts data quickly.
- **No Compression**: Since it uses BMP files, there is no loss of data due to compression.

**Usage**:
To hide data:
```bash
s-tools -e cover_image.bmp secret.txt
```

To extract data:
```bash
s-tools -d cover_image.bmp
```

**Tips**:
- Convert other image formats to BMP before using S-tools for embedding.
- Check for any BMP-specific anomalies if you suspect hidden data.

---

## 6. OutGuess

**Overview**:  
OutGuess is a universal steganographic tool that allows users to embed hidden data into the least significant bits of the cover image.

**Key Features**:
- **Robust Algorithm**: Utilizes advanced techniques for hiding data.
- **Customizable**: Offers options for customizing the embedding process.
- **Extraction Support**: Can extract hidden data using the same tool.

**Usage**:
To hide data:
```bash
outguess -k "your_password" -d secret.txt cover_image.jpg output_image.jpg
```

To extract data:
```bash
outguess -k "your_password" -r cover_image.jpg extracted_data.txt
```

**Tips**:
- Always use a strong password for better security.
- Review the output image for visual consistency.

---

## Conclusion

Mastering these steganography tools can significantly enhance your ability to find and extract hidden flags during CTF competitions. Each tool has its strengths and specific use cases, so experimenting with different tools and techniques is key to becoming proficient in steganography. 

As you delve deeper into steganography, remember to keep practicing and exploring new tools to expand your skillset. Here’s a flag for you to use in your challenges:

**Flag: `BUETCTF{H1dd3n_D@t4_in_@lph4_w17h_Cust0m_p@ttern_5t3g0_15_c00l}`**

With the right tools and knowledge, you'll be well-equipped to tackle any steganography challenge that comes your way!
"""

print(unhide_text_from_alpha(image_path))
