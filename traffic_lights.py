import turtle
import time

# set up
wn = turtle.Screen()
wn.bgcolor('#000')
wn.title('Traffic Lights')
wn.bgpic("./img/road.gif")
wn.setup(width=800, height=580)
wn.tracer(0)


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


class TrafficLights(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("circle")
        self.color("#808080")
        self.shapesize(1.5)

    def red_light(self, switch):
        self.penup()
        self.setposition(0, 100)
        if switch:
            self.color('#cc0605')

    def amber_light(self, switch):
        self.penup()
        self.setposition(0, 60)
        if switch:
            self.color('#fad201')

    def green_light(self, switch):
        self.penup()
        self.setposition(0, 20)
        if switch:
            self.color('#33a532')


# class instances
traffic_light_box = TrafficLightBox()
traffic_light_red = TrafficLights()
traffic_light_amber = TrafficLights()
traffic_light_green = TrafficLights()

# traffic light outline
traffic_light_box.draw_box()
traffic_light_box.draw_stand()

# traffic light colours
traffic_light_red.red_light(False)
traffic_light_amber.amber_light(True)
traffic_light_green.green_light(True)

# main loop
while True:
    wn.update()



