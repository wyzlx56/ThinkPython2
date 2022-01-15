from point import Point
from rectangle import Rectangle
from circle import Circle
import turtle


def draw_rect(t, rect):
    t.pu()
    t.goto(rect.corner.x,rect.corner.y)
    t.pd()
    t.fd(rect.width)
    t.lt(90)
    t.fd(rect.height)
    t.lt(90)
    t.fd(rect.width)
    t.lt(90)
    t.fd(rect.height)

def draw_circle(t,circle):
    t.pu()
    t.goto(circle.center.x,circle.center.y)
    t.pd()
    t.circle(circle.radius)
t = turtle.Turtle()
rect = Rectangle(Point(0, 50), 100, 100)
circle=Circle(Point(0,0),50)
draw_rect(t, rect)
draw_circle(t,circle)
turtle.mainloop()
