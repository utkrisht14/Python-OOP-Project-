class Rectangle:
    """
    A rectangle shape that can be drawn on a Canvas object.
    """
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw(self, canvas):
        """Draw the rectangle onto the canvas by modifying pixel values."""
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color

class Square:
    """
    A square shape that can be drawn on a Canvas object.
    """
    def __init__(self, x, y, side, color):
        self.color = color
        self.x = x
        self.y = y
        self.side = side

    def draw(self, canvas):
        """Draw the square onto the canvas by modifying pixel values."""
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color
