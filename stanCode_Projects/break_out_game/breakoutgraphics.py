"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao
-----------------------------------------------
File : breakoutgraphics.py
Name : Calvin Chen
This file practice how to write our own class
and understand the concept of class.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

# Constant
BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10       # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    # Constructor
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height,
                            x=(window_width-paddle_width)/2, y=window_height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.paddle.color = 'black'
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle)
        # extension paddle
        self.new_paddle = GRect(self.window.width, self.paddle.height, x=0,
                                 y=self.window.height-self.paddle.height-PADDLE_OFFSET)
        self.new_paddle.filled = True
        self.new_paddle.fill_color = 'black'

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2,
                          x=window_width/2 - ball_radius, y=window_height/2 - ball_radius)
        self.ball.filled = True
        self.ball.color = 'black'
        self.ball.fill_color = 'black'
        self.window.add(self.ball)

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners.
        self.key = True       # the key to start game.
        onmouseclicked(self.click_start)
        onmousemoved(self.move)

        # Draw bricks.
        self.b_width = brick_width
        self.b_height = brick_height
        self.row = brick_rows
        self.col = brick_cols
        self.b_offset = brick_offset
        self.b_space = brick_spacing
        self.put_bricks()

        # bonus     # extension function
        self.bonus_1 = GOval(10, 10)
        self.bonus_1.filled = True
        self.bonus_1.color = 'gray'
        self.bonus_1.fill_color = 'gray'
        self.bonus_dx = 0
        self.bonus_dy = 0

    def put_bricks(self):
        """
        This method creates the bricks we needed.
        """
        x_point = 0
        y_point = 0 + self.b_offset
        color = 'red'
        # Loop over how many bricks we needed.
        for i in range(self.row):
            for j in range(self.col):
                brick = GRect(self.b_width, self.b_height)
                brick.filled = True
                brick.color = color
                brick.fill_color = color
                self.window.add(brick, x_point, y_point)
                x_point += self.b_width
                x_point += self.b_space
            y_point += self.b_height
            y_point += self.b_space
            x_point = 0
            # The color in each row.
            if i == 1:
                color = 'orange'
            if i == 3:
                color = 'yellow'
            if i == 5:
                color = 'green'
            if i == 7:
                color = 'blue'

    def click_start(self, event):
        """
        This method control when to start the game.
        So, the ball will not be affected by clicking while the ball is moving.
        :param self.key: bool, control when we click.
        """
        if self.key:
            self.key = False
            self.set_ball_velocity()
            self.set_bonus_velocity()

    def set_bonus_velocity(self):       # extension function
        """
        This method get the velocity of bonus ball.
        """
        self.bonus_dx = 0
        self.bonus_dy = 6

    def get_b_dx(self):                 # extension function
        """
        Get the x velocity of bonus ball.
        :return: self.bonus_dx: int, the x velocity of bonus ball
        """
        return self.bonus_dx

    def get_b_dy(self):                 # extension function
        """
        Get the y velocity of bonus ball.
        :return: self.bonus_dy: int, the y velocity of bonus ball.
        """
        return self.bonus_dy

    def set_ball_velocity(self):
        """
        This method decide the velocity of the ball.
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        # Decide the direction of x.
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def get_dx(self):
        """
        Getter method. We can get the x velocity of the ball in breakout.py
        :return: self.__dx: int, the x velocity of the ball.
        """
        return self.__dx

    def get_dy(self):
        """
        Getter method. We can get the y velocity of the ball in breakout.py
        :return: self.__dy: int, the y velocity of the ball.
        """
        return self.__dy

    def set_dx(self, dx):
        """
        Setter method. We can reset the x velocity of the ball in breakout,py.
        :param dx: int, the x velocity.
        """
        self.__dx = dx

    def set_dy(self, dy):
        """
        Setter method. We can reset the y velocity of the ball in breakout,py.
        :param dy: int, the y velocity.
        """
        self.__dy = dy

    def move(self, event):
        """
        This method connects the mouse to the paddle.
        The middle point of the paddle will move where the mouse move.
        Moreover, if the mouse out of the window, the paddle will not
        move beyond the window. The paddle always stays in the window.
        """
        # When the mouse is within the window, the paddle position will move where the mouse move.
        if event.x >= 0 or event.x <= self.window.width:
            self.window.add(self.paddle,
                            x=event.x-self.paddle.width/2, y=self.window.height-PADDLE_OFFSET-self.paddle.height)
        # When the mouse is outside of the right boundary, the paddle will stay inside the right side of the window.
        if event.x >= self.window.width - self.paddle.width:
            self.window.add(self.paddle,
                            x=self.window.width - self.paddle.width,
                            y=self.window.height-PADDLE_OFFSET-self.paddle.height)
        # When the mouse is outside of the left boundary, the paddle will stay inside the left side of the window.
        if event.x <= 0 + self.paddle.width:
            self.window.add(self.paddle, x=0, y=self.window.height-PADDLE_OFFSET-self.paddle.height)

    def check_for_collisions(self):
        """
        When one of the four points of the ball hits a object,
        this method will return that object to the breakout.py.
        :return: obj: Can be the brick, None, or paddle.
        """
        self.obj = self.window.get_object_at(self.ball.x, self.ball.y)
        # first point(x, y)
        if self.obj is not None:
            return self.obj
        else:
            # second point(x + 2r, y)
            self.obj = self.window.get_object_at(self.ball.x + 2*BALL_RADIUS, self.ball.y)
            if self.obj is not None:
                return self.obj
            else:
                # third point(x, y + 2r)
                self.obj = self.window.get_object_at(self.ball.x, self.ball.y + 2*BALL_RADIUS)
                if self.obj is not None:
                    return self.obj
                else:
                    # fourth point(x + 2r, y + 2r)
                    self.obj = self.window.get_object_at(self.ball.x + 2*BALL_RADIUS, self.ball.y + 2*BALL_RADIUS)
                    if self.obj is not None:
                        return self.obj

    def start_again(self):
        """
        First, this method will reset the game and velocity of the ball
        when player die(the ball went below the window).
        Second, this method will open the key to prepare the next play.
        """
        self.set_ball_position()
        self.window.add(self.ball)
        self.__dx = 0
        self.__dy = 0
        self.key = True

    def set_ball_position(self):
        """
        This method sets the ball position.
        """
        self.ball.x = self.window.width/2 - BALL_RADIUS
        self.ball.y = self.window.height/2 - BALL_RADIUS

    def die(self):
        """
        This method knows if your ball out of window.
        :return: die: bool.
        """
        die = self.ball.y + self.ball.height >= self.window.height
        return die

    def brick_needed_remove(self):
        """
        This method counts how many bricks we needed to remove
        to help us know when to end game.
        :return: remove: int, how many bricks user created.
        """
        remove = self.row * self.col
        return remove

    def create_bonus(self):     # extension function
        """
        This method decide which bonus.
        :return: 1: int
        """
        chose = random.randint(1, 5)
        if chose == 1:
            return 1

    def check_get_bonus(self):      # extension function
        """
        This method will know if the bonus ball
        hit the paddle.
        :return: b_obj: obj, when the bonus ball hit the paddle.
        """
        self.b_obj = self.window.get_object_at(self.bonus_1.x, self.bonus_1.y + self.bonus_1.height)
        if self.b_obj is self.paddle:
            return self.b_obj
        else:
            self.b_obj = self.window.get_object_at(self.bonus_1.x+self.bonus_1.width, self.bonus_1.y+self.bonus_1.height)
            if self.b_obj is self.paddle:
                return self.b_obj
