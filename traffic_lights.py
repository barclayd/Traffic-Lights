import turtle

# set up
wn = turtle.Screen()
wn.bgcolor('#000')
wn.title('Traffic Lights')
wn.bgpic("./img/road.gif")
wn.setup(width=800, height=580)


# classes
class TrafficLightBox(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color('#000')
        self.width(3)
        self.pensize(5)

    def draw_box(self):
        self.setposition(-30, 120)
        self.pendown()
        self.fd(60)
        self.rt(90)
        self.fd(120)
        self.rt(90)
        self.fd(60)
        self.rt(90)
        self.fd(120)
        self.penup()

    def draw_stand(self):
        self.setposition(0, 0)
        self.pendown()
        self.pensize(5)
        self.fd(-60)
        self.rt(90)
        self.fd(30)
        self.fd(-60)


# class instances
traffic_light_box = TrafficLightBox()
traffic_light_box.draw_box()
traffic_light_box.draw_stand()

# main loop
wn.mainloop()
