from PIL import Image

with open("chall.nocap", "r") as file:
    bcapng = file.read()

img_data = bcapng.split("::")
img_width = int(img_data[0][1:])
img_height = int(img_data[1])

print(f"Image dimensions: {img_width} x {img_height}")

image = Image.new("RGB", (img_width, img_height))

encoded_data = img_data[2][:-1]

for idx, pixel in enumerate(encoded_data):
    x = idx % img_width
    y = idx // img_width
    color = (0, 0, 0) if pixel == '?' else (255, 255, 255)
    image.putpixel((x, y), color)

image.show()