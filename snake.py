from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake = []
        self.x = 0
        self.y = 0
        for _ in range(0, 3):
            snake_segment = Turtle(shape="square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(x=self.x, y=self.y)
            self.snake.append(snake_segment)
            self.x -= 20

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment - 1].xcor()
            new_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(x=new_x, y=new_y)

        self.snake[0].forward(20)
