import turtle


def tuxing():
    colors = ["blue", "yellow", "orange", "green",
              "red", "indigo", "purple", 'azure']
    for i in range(len(colors)):
        c = colors[i]
        turtle.color(c)
        turtle.begin_fill()
        turtle.circle(100)
        turtle.rt(360/len(colors))
        turtle.end_fill()
    turtle.done()


if __name__ == "__main__":
    tuxing()
