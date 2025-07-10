from turtle import Turtle

class Ball(Turtle):
    """
    Represents the game ball.
    """
    def __init__(self):
        super().__init__()
        self.shape("circle") 
        self.color("red")
        self.penup() 
        self.goto(0, 0)
        self.dx = 10           # Initial horizontal speed (change in x)
        self.dy = 10           # Initial vertical speed (change in y)
        self.move_speed = 0.1  # Speed of the ball movement, can be adjusted for difficulty

    def move(self):
        """
        Moves the ball by updating its x and y coordinates based on its speed.
        """
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)
        

    def bounce_x(self):
        """
        Reverses the horizontal direction of the ball.
        """
        self.dx *= -1
        self.move_speed *= 0.9 # Increase speed slightly on bounce

    def bounce_y(self):
        """
        Reverses the vertical direction of the ball.
        """
        self.dy *= -1

    def reset_position(self):
        """
        Resets the ball to the center of the screen and reverses its direction.
        Useful after a point is scored.
        """
        self.goto(0, 0)
        self.bounce_y() # Reverse vertical direction for a new serve
        self.move_speed = 0.1  # Reset speed after scoring
