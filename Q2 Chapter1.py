import time
from PIL import Image

# Generate a number based on the current time
current_time = int(time.time())
generated_number = (current_time % 100) + 50  # Generates n

# Load the image(If any case of error load exact file directory in source)
img = Image.open("Chapter1.png")
pixels = img.load()

# Modify the pixel values (r, g, b) by adding 'n'
width, height = img.size
red_sum = 0

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        new_r = min(r + generated_number, 255)  # Ensure values are within 0-255
        new_g = min(g + generated_number, 255)
        new_b = min(b + generated_number, 255)
        pixels[x, y] = (new_r, new_g, new_b)
        red_sum += new_r  # Accumulate the red pixel values

# Save the new image
img.save("chapter1out.png")

# Output the sum of the red pixel values
print(f"Sum of red pixel values: {red_sum}")

