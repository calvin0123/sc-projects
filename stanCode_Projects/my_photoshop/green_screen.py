"""
File: green_screen.py
Name: Calvin Chen
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in ReyGreenScreen.png
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    This function removes the green screen and replaces the green screen
    with background image.
    ---------------------------------------------------------------------
    :param background_img: SimpleImage, the background image
    :param figure_img: SimpleImage, green screen figure image
    :return: figure_img: SimpleImage, the green screen pixels are replaced by background image pixels
    """
    for y in range(background_img.height):
        for x in range(background_img.width):

            pixel_fig = figure_img.get_pixel(x, y)
            bigger = max(pixel_fig.red, pixel_fig.blue)

            if pixel_fig.green > bigger * 2:
                pixel_bg = background_img.get_pixel(x, y)
                pixel_fig.red = pixel_bg.red
                pixel_fig.green = pixel_bg.green
                pixel_fig.blue = pixel_bg.blue

    return figure_img


def main():
    """
    This function conducts green screen replacement
    that is able to photoshop a person onto the background.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
