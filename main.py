from turtle import Screen , Turtle

screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("Snake | Score Yours")

segment_1 = Turtle("square")
# we can set shape = "square"
segment_1.color("white")

segment_2 = Turtle("square")
segment_2.color("white")
segment_2.goto(-20,0)
# it simply takes goto (x , y)

segment_3 = Turtle("square")
segment_3.color("white")
segment_3.goto(-40 , 0)

#if we dont want repeated code we can use it by declaring a loop

#let's declare a tuple for diffrent position

# starting_position = [(0, 0) , (-20 , 0) , (-40 , 0) ,]

# for position in starting_position:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.goto(position)

#this 3 lines of code will generate the same gui


screen.exitonclick()