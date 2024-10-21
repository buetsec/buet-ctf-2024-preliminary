from PIL import Image

def image_to_text_random_ignore_black(image_path):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()

    hex_string = ""

    # Loop over each pixel and extract the RGB values
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            # Skip black pixels (0, 0, 0)
            if r == 0 and g == 0 and b == 0:
                continue
            
            # Convert RGB values to hex and concatenate to form the hex string
            hex_string += '{:02x}{:02x}{:02x}'.format(r, g, b)

    # Convert the hex string back to ASCII text
    try:
        bytes_object = bytes.fromhex(hex_string)
        decoded_text = bytes_object.decode("utf-8", errors="ignore")  # "ignore" skips invalid bytes
        # Strip out any padding or unnecessary characters at the end
        decoded_text = decoded_text.rstrip('\x00').rstrip()  # Remove any null characters or trailing whitespace
        print("Decoded text:", decoded_text)
        return decoded_text
    except Exception as e:
        print("Error decoding the text:", e)
        return None

# Example usage:
image_to_text_random_ignore_black("output_image_random.png")
