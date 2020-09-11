"""
File: shrink.py
Name: Calvin Chen
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    This function first create a shrink blank image and assign the
    original pixel to the shrink blank point(x, y) which is divided by 2.
    ---------------------------------------------------------------
    :param filename: str, the file path of the original image
    :return img: SimpleImage, the shrink image of the original one
    """
    img = SimpleImage("images/poppy.png")
    img_shrink = SimpleImage.blank(img.width // 2, img.height // 2)
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            pixel_shrink = img_shrink.get_pixel(x // 2, y // 2)
            pixel_shrink.red = pixel.red
            pixel_shrink.green = pixel.green
            pixel_shrink.blue = pixel.blue
    return img_shrink


def main():
    """
    This function show the original image and shrink the
    original image.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
