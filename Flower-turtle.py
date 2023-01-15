import turtle
tao = turtle.Pen() #ดึงความสามารถการใช้ปากกา
tao.shape('turtle') #แปลงร่างเป็นเต่า
def Rectangle():
    '''ฟังก์ชั่นนี้เอาไว้วาดรูปสี่เหลี่ยม'''
    for i in range(4):
        tao.forward(100)
        tao.left(90)

def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

def Octagon():
    for i in range(8):
        tao.forward(100)
        tao.left(45)

def Pen_Move():
    tao.penup()
    tao.forward(-10)
    tao.left(45)
    tao.pendown()

round = 7
while round > 0:
    Octagon()
    Pen_Move()
    round -= 1
Octagon()
Pen-Move()
