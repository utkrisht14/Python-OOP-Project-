from PIL import Image
import numpy as np

class Canvas:
    """
    Object where all shapes are going to be drawn.
    It initializes a blank image (as a NumPy array) filled with the background color.
    """
    def __init__(self, height, width, color):
        self.color = color
        self.height = height
        self.width = width

        # Create a 3D numpy array filled with zeros (black image)
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        # Fill the canvas with the background color
        self.data[:] = self.color

    def make(self, imagepath):
        """Converts the current array into an image file and saves it."""
        img = Image.fromarray(self.data, "RGB")
        img.save(imagepath)