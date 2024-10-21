from PIL import Image

with open("chall.nocap", "rb") as file:
    nocap_data = file.read()

width = nocap_data[0]
height = nocap_data[1]
pixels = int.from_bytes(nocap_data[2:], "big")

image = Image.new("RGB", (width, height))

for y in range(height - 1, -1, -1):
    for x in range(width - 1, -1, -1):
        if pixels % 3 == 0:
            color = (255, 255, 255)
        elif pixels % 3 == 1:
            color = (255, 37, 0)
        else:
            color = (0, 0, 0)
        
        image.putpixel((x, y), color)
        pixels //= 3

image.save("out.png")