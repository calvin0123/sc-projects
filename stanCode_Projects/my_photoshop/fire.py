"""
File: fire.py
Name: Calvin Chen
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation
"""
from simpleimage import SimpleImage

# Controls the pixel of big fire
HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    Remove all the green and blue color from the photo and
    assign 255 to pixel.red in order to enhance the big fire spot.
    -----------------------------------------------------------------
    :param filename: str, the file path of the image
    :return: img : SimpleImage, the image of red spot with big fire and the gray scale with no fire
    """
    img = SimpleImage('images/greenland-fire.png')
    for pixel in img:
        avg = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg

    return img


def main():
    """
    This function show the original image
    and the fire spot of the greenland.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
