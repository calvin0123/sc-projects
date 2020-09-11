"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
------------------------------------------
File: babygraphics.py
Name: Calvin Chen
This file shows the rank of baby name from 1900 to
2010 in the US.
"""

import tkinter
import babynames
import babygraphicsgui as gui

# The data we want to analyze
FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]


# CONSTANT
CANVAS_WIDTH = 1000                                                               # The width of canvas
CANVAS_HEIGHT = 600                                                               # The height of canvas
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]  # The year we want to analyze
GRAPH_MARGIN_SIZE = 20                                                            # Distance between border and line
COLORS = ['red', 'purple', 'green', 'blue']                                       # The color of each line
TEXT_DX = 2                                                                       # Distance between the text and line
LINE_WIDTH = 2                                                                    # The width of each line
MAX_RANK = 1000                                                                   # Last rank of each name


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    start_x = GRAPH_MARGIN_SIZE
    interval = width / (len(YEARS) + 1)
    interval_dic = {}
    for year in YEARS:
        if year == YEARS[0]:
            interval_dic[year] = GRAPH_MARGIN_SIZE
        else:
            start_x += interval
            interval_dic[year] = start_x
    year = YEARS[year_index]
    x_coordinate = interval_dic[year]
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # Create the top and bottom line.
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)

    # Create the line between each year.
    for x in range(len(YEARS)):
        point = get_x_coordinate(CANVAS_WIDTH, x)
        canvas.create_line(point, 0, point, CANVAS_HEIGHT)
        canvas.create_text(point+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[x], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    # The proportion help fit in the canvas.
    proportion = (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE) / MAX_RANK
    # The start point that you draw the rank.
    start_point = CANVAS_HEIGHT - (CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE) - GRAPH_MARGIN_SIZE

    for n in range(len(lookup_names)):
        name = lookup_names[n]
        n = change_color(n)
        for yr in range(len(YEARS)):
            year = str(YEARS[yr])  # str
            # Create the condition to add text on canvas
            # and provide the information for adding line condition.
            if year in name_data[name]:
                rank = int(name_data[name][year])
                y_point = (rank * proportion) + start_point
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, yr) + TEXT_DX, y_point, text=(name, str(rank)),
                                   anchor=tkinter.SW, fill=COLORS[n])

            else:
                y_point = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, yr) + TEXT_DX, y_point, text=(name, '*'),
                                   anchor=tkinter.SW, fill=COLORS[n])

            # Create the condition to help add line in canvas.
            if yr + 1 != len(YEARS):
                x_point = get_x_coordinate(CANVAS_WIDTH, yr)
                next_x = get_x_coordinate(CANVAS_WIDTH, yr + 1)

                if str(YEARS[yr + 1]) in name_data[name]:
                    next_y = (int(name_data[name][str(YEARS[yr + 1])])) * proportion + start_point
                else:
                    next_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

                canvas.create_line(x_point, y_point, next_x, next_y, width=LINE_WIDTH, fill=COLORS[n])


def change_color(n):
    """
    This function return which color we are going to use.
    :param: n:int, the number of the name.
    :return: n:int, the number of the COLORS
    """
    # This condition will loop back to the first color
    # in COLORS and start again.
    if n + 1 > len(COLORS):
        n = ((n+1) % len(COLORS)) - 1
        return n
    return n


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
