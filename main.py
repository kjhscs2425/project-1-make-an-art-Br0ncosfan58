from turtle import *
speed(5)
penup()
backward(200)
pendown()
pencolor("green")
speed(10)

print("football field")

field_length = 450 # Possible values: 400, 450, 500
field_width = 250 # Possible values: 200, 250, 300
fieldgoal_width = 25 # Possible values: 20, 25, 30
fieldgoal_height = 50 # Possible values: 40, 50, 60


for i in range(2):
        forward(field_length)
        left(90)
        forward(field_width)
        left(90)

def draw_rectangle(length, width, color_name, distance):
    penup()
    forward(distance)
    pendown()
    begin_fill()
    color(color_name)
    for _ in range(2):
        forward(length)
        left(90)
        forward(width)
        left(90)
    end_fill()

def draw_field():
    draw_rectangle(field_length, field_width, "green", 0)

forward(field_length)
forward(50)
left(90)
forward(field_width)
left(90)
forward(50)
begin_fill()
color("orange")
left(90)
forward(field_width)
left(90)
forward(50)
left(90)
forward(field_width)
left(90)
forward(50)
end_fill()
penup()
forward(field_length)

def draw_yard_marker(loops):
    for i in range(loops):
         left(90)
         forward(field_width)
         backward (field_width)
         right(90)
         forward(45)

pendown()
forward(50)
left(90)
forward(field_width)
left(90)
forward(50)
begin_fill()
color("orange")
left(90)
forward(field_width)
left(90)
forward(50)
left(90)
forward(field_width)
left(90)
forward(50)
end_fill()
color("green")
forward(45)
left(90)

forward(field_width)
penup()
backward (field_width)
right(90)
forward(45)
pendown()

draw_yard_marker(8)

forward(50)
left(90)
forward(125)
right(90)
forward(20)
left(90)
forward(10)
right(90)
forward(25)
backward(25)
left(90)
backward(20)
right(90)
forward(25)
penup()
backward(45)
left(90)
backward(115)
pendown()

color("black")
forward(field_width)
left(90)
forward(field_length+100)
left(90)
forward(field_width)
left(90)
forward(field_length+100)

backward(field_length+50)
begin_fill()
color("forest green")
forward(45)
left(90)
forward(field_width)
left(90)
forward(45)
left(90)
forward(field_width)
end_fill()
penup()
left(90)
forward(90)

pendown()
begin_fill()
color("dark green")
left(90)
forward(field_width)
left(90)
forward(45)
left(90)
forward(field_width)
end_fill()
penup()
left(90)
forward(90)

draw_rectangle

pendown()
begin_fill()
color("forest green")
left(90)
forward(field_width)
left(90)
forward(45)
left(90)
forward(field_width)
end_fill()
penup()
left(90)
forward(90)

pendown()
begin_fill()
color("dark green")
left(90)
forward(field_width)
left(90)
forward(45)
left(90)
forward(field_width)
end_fill()
penup()
left(90)
forward(90)

pendown()
begin_fill()
color("forest green")
left(90)
forward(field_width)
left(90)
forward(45)
left(90)
forward(field_width)
end_fill()
penup()
left(90)
forward(90)

pendown()
begin_fill()
color("dark green")
left(90)
forward(field_width)
left(90)
forward(45)
left(90)
forward(field_width)
end_fill()
penup()
left(90)
forward(90)

pendown()
begin_fill()
color("forest green")
left(90)
forward(field_width)
left(90)
forward(45)
left(90)
forward(field_width)
end_fill()
penup()
left(90)
forward(90)

pendown()
begin_fill()
color("dark green")
left(90)
forward(field_width)
left(90)
forward(45)
left(90)
forward(field_width)
end_fill()
penup()
left(90)
forward(90)

pendown()
begin_fill()
color("forest green")
left(90)
forward(field_width)
left(90)
forward(45)
left(90)
forward(field_width)
end_fill()
penup()
left(90)
forward(90)

pendown()
begin_fill()
color("dark green")
left(90)
forward(field_width)
left(90)
forward(45)
left(90)
forward(field_width)
end_fill()

penup()
right(90)
forward(455)
right(90)
forward(125)
left(90)
pendown()
forward(20)
left(90)
forward(10)
right(180)
forward(25)
backward(25)
right(90)
backward(20)
forward(20)
left(90)
forward(25)
left(90)
forward(25)


exitonclick()