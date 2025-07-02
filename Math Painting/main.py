from canvas import Canvas
from shapes import Rectangle, Square

# Get canvas width and height from the user
canvas_width = int(input("Enter the canvas width: "))
canvas_height = int(input("Enter the canvas height: "))

# Define color options
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}

# Prompt user for canvas color
canvas_color = input("Enter canvas color (white or black): ").lower()

# Create a canvas using the selected color
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

# Start drawing loop
while True:
    shape_type = input("What shape would you like to draw? (rectangle/square or 'quit' to exit): ").lower()

    if shape_type == "rectangle":
        rec_x = int(input("Enter x of rectangle: "))
        rec_y = int(input("Enter y of rectangle: "))
        rec_width = int(input("Enter the width of the rectangle: "))
        rec_height = int(input("Enter the height of the rectangle: "))
        red = int(input("How much red should the rectangle have (0–255): "))
        green = int(input("How much green should the rectangle have (0–255): "))
        blue = int(input("How much blue should the rectangle have (0–255): "))

        # Create and draw the rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        r1.draw(canvas)

    elif shape_type == "square":
        sq_x = int(input("Enter x of square: "))
        sq_y = int(input("Enter y of square: "))
        sq_side = int(input("Enter side of the square: "))
        red = int(input("How much red should the square have (0–255): "))
        green = int(input("How much green should the square have (0–255): "))
        blue = int(input("How much blue should the square have (0–255): "))

        # Create and draw the square
        s1 = Square(x=sq_x, y=sq_y, side=sq_side, color=(red, green, blue))
        s1.draw(canvas)

    elif shape_type == "quit":
        break

    else:
        print("Invalid input. Please enter 'rectangle', 'square', or 'quit'.")

# Save the final drawing
canvas.make("canvas.png")
