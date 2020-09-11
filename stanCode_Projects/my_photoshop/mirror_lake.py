"""
File: mirror_lake.py
Name: Calvin Chen
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing the inverse image of
mt-rainier.jpg below the original one
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    Create a blank image.
    Assign the inverse image of original one to the blank image.
    ------------------------------------------------------------
    :param filename: str, the file path of the original image
    :return: img_blank: SimpleImage, the image of mirror lake vibe
    """
    img = SimpleImage('images/mt-rainier.jpg')
    img_blank = SimpleImage.blank(img.width, img.height * 2)
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            p1 = img_blank.get_pixel(x, y)
            p2 = img_blank.get_pixel(x, img_blank.height - 1 - y)
            p1.red = pixel.red
            p1.green = pixel.green
            p1.blue = pixel.blue
            p2.red = pixel.red
            p2.green = pixel.green
            p2.blue = pixel.blue
    return img_blank


def main():
    """
    This function show the original image and is able to show inverse
    image of the mt-rainer.jpg below the original one.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
