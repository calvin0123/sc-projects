"""
File: blur.py
Name: Calvin Chen
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    First, this function create the blank image.
    Second, it will get the blur color in each point from old image.
    Third, it will assign the blur color to the blank image.
    --------------------------------------------------
    :param img: SimpleImage, the original image.
    :return: new_img: SimpleImage, blur image.
    """

    new_img = SimpleImage.blank(img.width, img.height)

    for r in range(img.height):
        for c in range(img.width):
            pixel = img.get_pixel(c, r)
            pixel_blur = new_img.get_pixel(c, r)
            new_pixel = get_blur_color(c, r)
            pixel_blur.red = new_pixel.red
            pixel_blur.green = new_pixel.green
            pixel_blur.blue = new_pixel.blue
    return new_img


def get_blur_color(x, y):
    """
    This function calculate the Red, Green, and Blue from each
    point. Then, assign the blur color to (x,y).
    --------------------------------------------------
    :param x: int, the column of each spot.
    :param y: int, the row of each spot.
    :return: new_pixel: the R, G, and B of that point pixel.
    """
    img = SimpleImage("images/smiley-face.png")
    new_img = SimpleImage.blank(img.width, img.height)
    new_pixel = new_img.get_pixel(x, y)
    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0

    if x == 0:
        start_x = 0
        end_x = x + 2
        start_y = 0
        end_y = y + 2
    elif x == img.width - 1:
        start_x = x - 1
        end_x = x + 1
    else:
        start_x = x - 1
        end_x = x + 2

    if y == 0:
        start_y = 0
        end_y = y + 2
    elif y == img.height - 1:
        start_y = y - 1
        end_y = y + 1
    else:
        start_y = y - 1
        end_y = y + 2
    total_r = 0
    total_g = 0
    total_b = 0
    counts = 0

    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            pixel = img.get_pixel(x, y)
            total_r += pixel.red
            total_g += pixel.green
            total_b += pixel.blue
            counts += 1
    print('total r g b', total_r, total_g, total_b)     # make sure the algorithm is running

    new_r = total_r / counts
    new_g = total_g / counts
    new_b = total_b / counts
    new_pixel.red = new_r
    new_pixel.green = new_g
    new_pixel.blue = new_b

    return new_pixel


def main():
    """
    This function will blur the old image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(1):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
