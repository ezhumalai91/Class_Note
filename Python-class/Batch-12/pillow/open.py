'''
from PIL import Image

# Location of the image
img = Image.open("image.jpg")
img.show()
'''


'''
#properties of image
from PIL import Image
img = Image.open("image.jpg")

print(img.size)
print(img.format)
'''

'''
from PIL import Image
import PIL
img = Image.open(r"image.jpg")
# rotating a image 90 deg counter clockwise
img = img.rotate(45, PIL.Image.NEAREST, expand = 1)

# to show specified image
img.show()
img.save("new.jpg")
'''
'''
from PIL import Image

# creating a object
image = Image.open(r"image.jpg")
image.load()

# Splitting the image into individual
# bands
r, g, b, = image.split()

# merge function used
im1 = Image.merge('RGB', (g, b, r))
im1.show()
'''


'''
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Open an image
img = Image.open('image.jpg')

# Initialize ImageDraw
draw = ImageDraw.Draw(img)

# Define the text and font
text = "Ajith"
font = ImageFont.truetype("arial.ttf", 300)  # Make sure to have the font file available or adjust accordingly

# Add text to image
draw.text((28, 36), text, fill=(255, 0, 0), font=font)

# Display the edited image
img.show()
# Save the edited image
img.save("ajith_new.jpg")
'''

from PIL import Image
img = Image.open("image.jpg")

# Setting the points for cropped image
left = 155
top = 65
right = 360
bottom = 270

# Cropped image of above dimension
# (It will not change original image)
img1 = img.crop((left, top, right, bottom))

# Shows the image in image viewer
img1.show()
img1.save("crop.jpg")


'''
from PIL import Image, ImageDraw
from math import cos, sin, radians

def draw_spiderman_face(draw, center, radius):
    # Colors
    red = (255, 0, 0)
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Draw face
    draw.ellipse(
        [center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius],
        fill=red, outline=black
    )

    # Draw eyes
    eye_width = 80
    eye_height = 40
    eye_distance = 40
    draw.ellipse(
        [center[0] - eye_width - eye_distance, center[1] - eye_height // 2, center[0] - eye_distance, center[1] + eye_height // 2],
        fill=white, outline=black
    )
    draw.ellipse(
        [center[0] + eye_distance, center[1] - eye_height // 2, center[0] + eye_width + eye_distance, center[1] + eye_height // 2],
        fill=white, outline=black
    )

    # Draw web lines
    web_thickness = 3
    num_web_lines = 12
    for i in range(num_web_lines):
        angle = (360 / num_web_lines) * i
        end_x = center[0] + radius * 0.9 * cos(radians(angle))
        end_y = center[1] + radius * 0.9 * sin(radians(angle))
        draw.line(
            [center, (end_x, end_y)],
            fill=black, width=web_thickness
        )

    # Draw web circles
    num_web_circles = 4
    for i in range(num_web_circles):
        r = radius * (0.1 + 0.2 * i)
        draw.ellipse(
            [center[0] - r, center[1] - r, center[0] + r, center[1] + r],
            outline=black, width=web_thickness
        )

# Create a blank image with white background
width, height = 400, 600
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Draw Spider-Man face
face_center = (width // 2, height // 2)
face_radius = 200
draw_spiderman_face(draw, face_center, face_radius)

# Save and show the image
image.save('spiderman_detailed.png')
image.show()

'''


'''
import math 
from PIL import Image, ImageDraw 
  
w, h = 220, 190
shape = [(40, 40), (w - 10, h - 10)] 
  
# creating new Image object 
img = Image.new("RGB", (w, h)) 
  
# create ellipse image 
img1 = ImageDraw.Draw(img)   
img1.ellipse(shape, fill ="yellow", outline ="red") 
img.show() 
'''

'''
from PIL import Image, ImageDraw

# Create a new blank image with a white background
img = Image.new('RGB', (500, 500), 'white')
draw = ImageDraw.Draw(img)

# Coordinates and sizes for Mickey Mouse's head and ears
head_center = (250, 250)
head_radius = 100

ear_radius = 50
left_ear_center = (head_center[0] - head_radius, head_center[1] - head_radius)
right_ear_center = (head_center[0] + head_radius, head_center[1] - head_radius)

# Draw the head
draw.ellipse(
    [
        (head_center[0] - head_radius, head_center[1] - head_radius),
        (head_center[0] + head_radius, head_center[1] + head_radius)
    ],
    fill='black'
)

# Draw the left ear
draw.ellipse(
    [
        (left_ear_center[0] - ear_radius, left_ear_center[1] - ear_radius),
        (left_ear_center[0] + ear_radius, left_ear_center[1] + ear_radius)
    ],
    fill='black'
)

# Draw the right ear
draw.ellipse(
    [
        (right_ear_center[0] - ear_radius, right_ear_center[1] - ear_radius),
        (right_ear_center[0] + ear_radius, right_ear_center[1] + ear_radius)
    ],
    fill='black'
)

# Display the image
img.show()

# Save the image
img.save('mickey_mouse.png')


'''
