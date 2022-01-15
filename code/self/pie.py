import math
import turtle

#画等腰三角形，给出对边的长度和顶角
def triangle(t,length,angle):
    t.fd(length/2/math.sin(angle/2*math.pi/180))
    t.rt(180-(180-angle)/2)
    t.fd(length)
    t.rt(180-(180-angle)/2)
    t.fd(length/2/math.sin(angle/2*math.pi/180))
    t.rt(180-angle)
def pie(t,n,length):
    angle=360/n
    for i in range(n):
        triangle(t,length,angle)
        t.rt(angle)

if __name__=="__main__":
    t=turtle.Turtle()
    t.pd()
    pie(t,8,100)
    turtle.mainloop()
