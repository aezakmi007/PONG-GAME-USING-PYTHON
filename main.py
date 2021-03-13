from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor('Black')
screen.setup(height=600, width=800)
screen.title('Pong')
screen.tracer(0)




r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
bal = Ball()
score = Scoreboard()







screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_dow, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_dow, "s")

game_is_on = True
while game_is_on:
     time.sleep(bal.move_speed)
     screen.update()
     bal.move()

     if bal.ycor() > 280 or bal.ycor() < - 280:
          bal.bounce_y()


     if bal.distance(r_paddle) < 50 and bal.xcor() > 320 or bal.distance(l_paddle) < 50 and bal.xcor() < -320:
          bal.bounce_x()


     if bal.xcor() > 380:
          bal.reset_position()
          score.l_point()


     if bal.xcor() < -380:
          bal.reset_position()
          score.r_point()


screen.exitonclick()