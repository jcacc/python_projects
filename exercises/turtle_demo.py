from PIL import Image
import turtle

# Load the image
img = Image.open('image.jpg')

# Create a turtle instance
t = turtle.Turtle()

# Iterate over each pixel in the image
for x in range(img.width):
    for y in range(img.height):
        
        # Get the color of the pixel
        color = 'black'
        
        # Set the turtle color
        t.pencolor(color)
        
        # Move the turtle to the pixel location and draw a dot
        t.up()
        t.goto(x, y)
        t.down()
        t.dot()
        t.speed(10)
t.tracer(True)

        
# Hide the turtle
t.hideturtle()
# Save the Turtle graphics as a PNG image
turtle.getcanvas().postscript(file='output.eps')
