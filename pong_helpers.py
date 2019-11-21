from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.circle import Circle
import digitalio
from adafruit_pybadger import PyBadger

"""
Pong paddle object that moves up and down on it's own at a steady rate.
"""
class AutoPaddle:
    def __init__(self, width, height, start_x, start_y, debug=False):
        # Store local variables in our object to access later in other functions
        self.height = height
        self.width = width
        self.x = start_x
        self.y = start_y
        
        # create a rect object
        self.rect = Rect(self.x, self.y, self.width, self.height, fill=0x0)
        
        # default to moving up
        self.going_up = True
        
        # screen height needed so it knows when to change direction
        self.SCREEN_HEIGHT = 128
        
    # You must call update() from inside the main loop of code.py    
    def update(self):
        #print("inside paddle update")
        
        # check which direction we are moving and change the y coordinate.
        if self.going_up == True:
            self.y -= 1
        else:
            self.y += 1
            
        # check if we've reached the top or bottom edge, and change direction if so.
        if self.y <= 0:
            self.going_up = False
        if self.y >= self.SCREEN_HEIGHT - self.height:
            self.going_up = True
        
        # copy over x and y from local vars into the rect so it takes effect on the screen
        self.rect.x = self.x
        self.rect.y = self.y


"""
Pong ball that has automatic movement in the horizontal 
direction, and manual control in the up and down directions.
If it hits a paddle it changes direction.
If it flies off a side edge it resets back to the center.
If it touches the top or bottom edges it cannot move that direction any further.
"""        
class ManualBall:
    def __init__(self, diameter, start_x, start_y, debug=False):
        # Store local variables in our object to access later in other functions
        self.diameter = diameter
        self.x = start_x
        self.y = start_y
        self.start_x = start_x
        self.start_y = start_y
        
        # Create a circle object for the screen
        self.circle = Circle(self.x, self.y, self.diameter, fill=0x00FF00, outline=0xFF00FF)
        
        # default to moving right
        self.going_right = True
        
        # Need screen height and width to check for collision with top/bottom and both side edges
        self.SCREEN_HEIGHT = 128
        self.SCREEN_WIDTH = 160
        
        # Badger object for easy button handling
        self.badger = PyBadger()
        
    # function to check for collisions between this ball 
    # and the left and right paddle objects that get passed in as parameters
    def check_collisions(self, left_paddle, right_paddle):
        #TODO: figure out if the x/y coordinate of the ball is centered or top left and adjust the collision check accordingly.
        
        if self.x == left_paddle.x + left_paddle.width and left_paddle.y < self.y < left_paddle.y + left_paddle.height:
            # if we collide with left paddle then change direction to move right
            self.going_right = True
            print("collide left paddle")
            
        if self.x == right_paddle.x - right_paddle.width and right_paddle.y < self.y < right_paddle.y + right_paddle.height:
            # if we collide with right paddle then change direction to move left
            self.going_right = False
            print("collide right paddle")
        
    # you must call update() from inside of main loop and pass the paddle objects   
    def update(self, left_paddle, right_paddle):
    
        # check which horizontal direction we are moving and adjust x coordinate accordingly.
        if self.going_right == True:
            self.x += 1
        else:
            self.x -= 1
            
        # Check if the up button is pressed, and the ball is not at the top edge
        if self.badger.button.up > 0 and self.y > 0:
            # move up
            self.y -= 1
        
        # check if the down button is pressed, and the ball is not at the bottom edge
        if self.badger.button.down > 0 and self.y < self.SCREEN_HEIGHT - (self.diameter+1)*2:
            # move down
            self.y += 1
        
            
        # check if ball went off left edge
        if self.x <= 0:
            # reset back to center
            self.x = self.start_x
            self.y = self.start_y
        
        # check if ball went off right edge        
        if self.x >= self.SCREEN_WIDTH - self.diameter:
            # reset back to center
            self.x = self.start_x
            self.y = self.start_y
        
        # check for collisions with paddles
        self.check_collisions(left_paddle, right_paddle)
        
        # copy over x and y coordinates to the circle object so it takes effect on the screen
        self.circle.x = self.x
        self.circle.y = self.y
            
        