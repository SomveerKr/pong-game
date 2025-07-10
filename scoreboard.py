from turtle import Turtle

class Scoreboard(Turtle):
    """A class to represent the score in a ping pong game."""
    
    def __init__(self):
        """Initialize the score display."""
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        """Update the displayed score."""
        self.clear()
        self.write(f"Left: {self.score_left} Right: {self.score_right}", align="center", font=("Courier", 24, "normal"))

    def left_player_scores(self):
        """Increment the left player's score."""
        self.score_left += 1
        self.update_score()

    def right_player_scores(self):
        """Increment the right player's score."""
        self.score_right += 1
        self.update_score()