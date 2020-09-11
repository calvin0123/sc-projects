"""
File: best_photoshop_award.py
Name: Calvin Chen
----------------------------------
This file creates a photoshopped image
that is going to compete for the 2020 Best
Photoshop Award for SC101P.
Please put all the images you use in image_contest folder
and make sure to choose which award you are aiming at
"""
from simpleimage import SimpleImage

# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.1
# Controls the upper bound for black pixel
BLACK_PIXEL = 150


def combine(back, me):
    """
    I hope I can code as good as Jerry, so I photoshop myself onto Jerry's
    Facebook profile picture to remind myself.
    --------------------------------------------------------------------
    :param back: SimpleImage, the background image, Jerry's Facebook profile picture
    :param me: SimpleImage, green screen figure image
    :return: SimpleImage, the green screen pixels are replaced by pixels background image
    """
    for y in range(back.height):
        for x in range(back.width):
            pixel_me = me.get_pixel(x, y)
            avg = (pixel_me.red + pixel_me.blue + pixel_me.green) // 3
            total = pixel_me.red + pixel_me.blue + pixel_me.green
            if pixel_me.green > avg * THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = back.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
    return me


def main():
    """
    This function conducts green screen replacement
    that is able to photoshop a person onto the background.
    """
    fg = SimpleImage('image_contest/calvin.jpg')
    bg = SimpleImage('image_contest/jerry.jpg')
    bg.make_as_big_as(fg)
    combined_img = combine(bg, fg)
    bg.show()
    combined_img.show()


if __name__ == '__main__':
    main()
