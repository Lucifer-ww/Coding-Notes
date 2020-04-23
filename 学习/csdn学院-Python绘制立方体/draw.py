import turtle

turtle.goto(200, 0)
turtle.goto(200, 200)
turtle.goto(0, 200)
turtle.goto(0, 0)

turtle.penup()
turtle.goto(100, 100)
turtle.pendown()

turtle.goto(100, -100)
turtle.goto(-100, -100)
turtle.goto(-100, 100)
turtle.goto(100, 100)

turtle.goto(200, 200)
turtle.penup()
turtle.goto(100, -100)
turtle.pendown()
turtle.goto(200, 0)

turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()
turtle.goto(0, 0)

turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()
turtle.goto(0, 200)

turtle.done()