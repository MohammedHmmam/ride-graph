import turtle
import time
time.sleep(5)
window = turtle.Screen()
window.bgcolor("#dfe6e9")
chart = turtle.Turtle()
#chart.hideturtle()
#my nam
chart.up()
chart.setpos(-140,290)
chart.color("#6ab04c")
chart.down()
chart.write("My ride" , font=("Arial",35,"bold"))
#chart title
chart.up()
chart.setpos(-240,255)
chart.color("#badc58")
chart.down()
chart.write("Mohammed Hmmam" , font=("Arial",30,"bold"))
#under Line
chart.up()
chart.setpos(-300,250)
chart.color("#6ab04c")
chart.down()
chart.hideturtle()
chart.pensize(10)
#time.sleep(10)
chart.forward(500)
#draw chart structure
#vertical
chart.up()
chart.setpos(-600,-250)
chart.color("#130f40")
chart.down()
chart.speed(0)
chart.pensize(10)
chart.left(90)
chart.forward(500)
#Horizental
chart.up()
chart.setpos(-600,-250)
chart.color("#130f40")
chart.down()
chart.pensize(10)
chart.shape("arrow")
chart.right(90)
chart.forward(1000)
#KM/H
chart.up()
chart.setpos(-680,250)
chart.color("#be2edd")
chart.down()
chart.write("KM/H" , font=("Arial",20,"bold"))
#Months
chart.up()
chart.setpos(400,-290)
chart.color("#be2edd")
chart.down()
chart.write("MONTHS" , font=("Arial",20,"bold"))
#distance
up = -260
km=0
while up<200:
    chart.up()
    chart.setpos(-640,up)
    chart.color("#f0932b")
    chart.down()
    chart.write(str(km)+"-" , font=("Arial",18,"bold"))
    up=up+60
    km+=10
#Months
mnth = 1
down = -580
while down<380:
    chart.up()
    chart.setpos(down,-280)
    chart.color("#f0932b")
    chart.down()
    chart.write(str(mnth), font=("Arial",18,"bold"))
    down+=80
    mnth+=1
#draw chart column1
chart.up()
chart.setpos(-575,-230)
chart.color("#d63031")
chart.speed(1)
chart.pensize(25)
chart.down()
chart.left(90)
chart.forward(100)
#draw chart column2
chart.up()
chart.setpos(-495,-230)
chart.color("#d63031")
chart.speed(1)
chart.pensize(25)
chart.down()
#chart.left(90)
chart.forward(160)
#draw chart column3
chart.up()
chart.setpos(-415,-230)
chart.color("#d63031")
chart.speed(1)
chart.pensize(25)
chart.down()
#chart.left(90)
chart.forward(400)
#draw chart column3
chart.up()
chart.setpos(-335,-230)
chart.color("#d63031")
chart.speed(1)
chart.pensize(25)
chart.down()
#chart.left(90)
chart.forward(400)
#draw chart column4
chart.up()
chart.setpos(-255,-230)
chart.color("#d63031")
chart.speed(1)
chart.pensize(25)
chart.down()
#chart.left(90)
chart.forward(280)
#draw chart column5
chart.up()
chart.setpos(-175,-230)
chart.color("#d63031")
chart.speed(1)
chart.pensize(25)
chart.down()
#chart.left(90)
chart.forward(220)
#draw chart column6
chart.up()
chart.setpos(-95,-230)
chart.color("#d63031")
chart.speed(1)
chart.pensize(25)
chart.down()
#chart.left(90)
chart.forward(220)



window.exitonclick()
