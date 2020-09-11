"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao
-----------------------------------------------
File : breakout.py
Name : Calvin Chen
This file practice how to write the breakout game
by using the class we created.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# Constant
FRAME_RATE = 1000 / 120     # 120 frames per second.
NUM_LIVES = 3               # player's lives.


def main():
    """
    This function plays a breakout game.
    """
    graphics = BreakoutGraphics()
    lives = NUM_LIVES       # player's lives.
    count_brick = 0         # count how many removed brick.
    # Animation loop here!
    while True:
        pause(FRAME_RATE)
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        graphics.ball.move(dx, dy)

        obj = graphics.check_for_collisions()
        # This condition will change the ball direction if the ball touches the paddle.
        if obj == graphics.paddle and dy >= 0:
            graphics.set_dy(-dy)
        # This condition will remove the obj(brick) and change direction.
        if obj is not graphics.paddle and obj is not None:
            graphics.set_dy(-dy)
            graphics.window.remove(obj)
            count_brick += 1

        # If the ball touches the window boundary, the ball will bounce back.
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.set_dx(-dx)
        if graphics.ball.y <= 0:
            graphics.set_dy(-dy)

        # When the ball out of scope(go deep in the window), condition will reset the ball and minus one lives.
        if graphics.die():
            graphics.window.remove(graphics.ball)
            lives -= 1
            # No lives and End games.
            if lives == 0:
                break
            graphics.start_again()
        # When you remove all the brick, you win and end the game.
        if count_brick == graphics.brick_needed_remove():
            graphics.window.remove(graphics.ball)
            break


if __name__ == '__main__':
    main()
