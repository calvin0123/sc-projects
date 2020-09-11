"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao
-----------------------------------------------
File : extension.py
Name : Calvin Chen
This file try to write the extension of breakout game.
But I think there is a little bit wrong. When the score
come to 100+, ball will start to move really slow.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel, GRect, GOval

# Constant
FRAME_RATE = 1000 / 120                          # 120 frames per second.
NUM_LIVES = 3                                    # player's lives.

# Global Variables
lives = NUM_LIVES                                # how many lives you can play
score = 0                                        # remove one bricks and score will plus one
label_s = GLabel('Score: ' + str(score))         # label to show your score
label_l = GLabel('Lives: ' + str(lives))         # label to show your lives


def main():
    global score, lives
    graphics = BreakoutGraphics(title='extension_breakout')
    count_brick = 0
    label_s.font = '-20'
    label_l.font = '-20'
    graphics.window.add(label_s, 0, label_s.height)
    graphics.window.add(label_l, 0, label_l.height + label_s.height)
    # graphics.extension_brick()
    bonus_count = 0

    while True:
        pause(FRAME_RATE)
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        graphics.ball.move(dx, dy)
        # Create bonus's velocity and needed information / Bonus times.
        bonus_dx = graphics.get_b_dx()
        bonus_dy = graphics.get_b_dy()
        # bonus_count = 0
        graphics.bonus_1.move(bonus_dx, bonus_dy)
        bonus_obj = graphics.check_get_bonus()
        # This condition show the first bonus time.
        if bonus_obj == graphics.paddle:
            graphics.window.remove(graphics.bonus_1)
            graphics.window.add(graphics.new_paddle)

        # Regular situation and bonus situation when ball hits paddle
        obj = graphics.check_for_collisions()
        if obj == graphics.paddle and dy >= 0:
            bonus_count += 1
            graphics.set_dy(-dy)
        if obj == graphics.new_paddle:
            graphics.set_dy(-dy)
            bonus_count += 1
            # Condition that ends bonus time
            if bonus_count > 4:
                graphics.window.remove(graphics.new_paddle)
                bonus_count = 0

        # This condition will remove the obj(brick), change direction, and create bonus.
        if obj is not graphics.paddle and obj is not None and obj is not label_l and obj is not label_s\
                and obj is not graphics.bonus_1 and obj is not graphics.new_paddle:
            graphics.set_dy(-dy)
            graphics.window.remove(obj)
            # This condition controls which bonus will be processed.
            if graphics.create_bonus() == 1:
                graphics.window.add(graphics.bonus_1, x=obj.x, y=obj.y)

            count_brick += 1
            score += 10
            label_s.text = 'Score: ' + str(score)

        # If the ball touches the window boundary, the ball will bounce back.
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.set_dx(-dx)
        if graphics.ball.y <= 0:
            graphics.set_dy(-dy)

        # When the ball out of scope(go deep in the window), condition will reset the ball and minus one lives.
        if graphics.die():
            graphics.window.remove(graphics.ball)
            lives -= 1
            label_l.text = 'Lives: ' + str(lives)
            # No lives and End games.
            if lives == 0:
                game_over = GLabel('Game Over! QAQ')
                game_over.font = '-40'
                graphics.window.add(game_over, graphics.window.width/6, graphics.window.height/2)
                break
            graphics.start_again()
        # When you remove all the brick, you win and end the game.
        if count_brick == graphics.brick_needed_remove():
            graphics.window.remove(graphics.ball)
            break


if __name__ == '__main__':
    main()
