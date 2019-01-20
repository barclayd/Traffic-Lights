import turtle
import time

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

    def draw_background(self):
        self.showturtle()
        self.setposition(0, 60)
        self.shape("square")
        self.shapesize(6, 3)
        self.color("#000")


class TrafficLights(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("circle")
        self.color("#A9A9A9")
        self.shapesize(1.5)
        self.red = '#cc0605'
        self.amber = '#fad201'
        self.green = '#33a532'

    def red_light(self, switch):
        self.penup()
        self.setposition(0, 100)
        self.color("#A9A9A9")
        if switch:
            self.color(self.red)

    def amber_light(self, switch):
        self.penup()
        self.setposition(0, 60)
        self.color("#A9A9A9")
        if switch:
            self.color(self.amber)

    def green_light(self, switch):
        self.penup()
        self.setposition(0, 20)
        self.color("#A9A9A9")
        if switch:
            self.color(self.green)


# functions
def stop():
    traffic_light_red.red_light(True)
    traffic_light_amber.amber_light(False)
    traffic_light_green.green_light(False)


def ready_to_go():
    traffic_light_red.red_light(False)
    traffic_light_amber.amber_light(True)
    traffic_light_green.green_light(True)


def go():
    traffic_light_amber.amber_light(False)


def ready_to_stop():
    traffic_light_amber.amber_light(True)
    traffic_light_green.green_light(False)


# class instances
traffic_light_box = TrafficLightBox()
traffic_light_background = TrafficLightBox()
traffic_light_red = TrafficLights()
traffic_light_amber = TrafficLights()
traffic_light_green = TrafficLights()

# traffic light outline
traffic_light_box.draw_box()
traffic_light_box.draw_stand()
traffic_light_background.draw_background()

# main loop
while True:
    # traffic light colours patterns
    stop()
    time.sleep(3)
    ready_to_go()
    time.sleep(1)
    go()
    time.sleep(3)
    ready_to_stop()
    time.sleep(1)
