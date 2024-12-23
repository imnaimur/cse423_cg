#--------------------Task 1---------------------#
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


width = 1440
height = 1080 
direction = 0

rain_positions = [-380, -400, -420, -440,- 460, -480, -500, -520, -540, -560, -580, -600, -620,-360, -340, -320, -300, -280, -260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620]
y1 =height//2 
speed = 0.1
day_night = 0.0

def points(x,y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()


def lines(x1, x2, y1, y2):

    glColor3f(1.0-day_night, 1.0-day_night, 1.0-day_night)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def house(x,y,rheight = None):

    glColor3f(0, 0, 0)
    x = x//2
    y = y//2
    if rheight == None:
        rheight = y

    glLineWidth(5)

    # horiaizontal
    lines(-x, x, 0, 0)
    lines(-x, x, -y, -y)
    # veritcal
    lines(-x, -x, 0, -y)
    lines(x, x, 0, -y)
    # roof
    lines(-x, 0, 0, rheight)
    lines(x, 0, 0, rheight)
    # door
    glLineWidth(2)

    lines(-x//4-(x*40/100), x//4-(x*40/100), -y//2, -y//2)

    lines(-x//4-(x*40/100), -x//4-(x*40/100), -y//2, -y)
    lines(x//4-(x*40/100), x//4-(x*40/100), -y//2, -y)

    mid = ( -y//2 -y)//2
    points(x//4-(x*40/100)-10,mid)



    # window
    # w_horizontal
    lines(x//1.5-(x*40/100), x-(x*40/100), -y//8, -y//8)
    lines(x//1.5-(x*40/100), x-(x*40/100), -y/2.5, -y/2.5)
    mid =  (-y//8+ ( -y/2.5))//2
    lines(x//1.5-(x*40/100), x-(x*40/100), mid, mid)

    # w_vertical
    lines(x//1.5-(x*40/100),x//1.5-(x*40/100), -y//8, -y/2.5)
    lines( x-(x*40/100),  x-(x*40/100), -y//8, -y/2.5)
    mid = (x//1.5-(x*40/100) +  x-(x*40/100))/2
    lines( mid, mid, -y//8, -y/2.5)
    
    



    # axixs
    # lines(-width//2, width//2, 0, 0)
    # lines(0, 0, -height//2, height//2)


def rains():


    for pos in rain_positions:
        # y1 = random.randint(0,height//2)

        lines(pos,pos+direction,y1,(y1)-20)


def animate():

    glutPostRedisplay()
    global y1,speed
    y1=(y1-speed)%240

def specialKeyListener(key, x, y):
    global speed, direction
    if key=='w':
        print(1)
    if key==GLUT_KEY_UP:
        speed *= 2
        print("Speed Increased")
    if key== GLUT_KEY_DOWN:		
        speed /= 2
        print("Speed Decreased")
    if key== GLUT_KEY_LEFT:		
        direction -= 1
        print(direction)
        print("left")
    if key== GLUT_KEY_RIGHT:		
        direction += 1
        print(direction)
        print("right")
    glutPostRedisplay()
def mouseListener(button, state, x, y):	
    global day_night
    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):   
            day_night-=0.1
            print("night shifting")
        
    if button==GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN: 	
           day_night+=0.1
           print("day shifting")

    if day_night<0.0:
        day_night = 0.0
    elif day_night>1.0:
        day_night = 1.0

    glutPostRedisplay()


def iterate():
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-width/2, width/2, -height/2, height/2, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # glClearColor(1, 1, 1, 1) 
    # glClearColor(1.0, 1.0, 1.0, 1.0)
    glClearColor(0.0+day_night, 0.0+day_night, 0.0+day_night, 0.0+day_night)
    glLoadIdentity()
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    iterate()

    # my work
    house(480,360,120)
    # house(300,240,120)
    rains()
    
    glutSwapBuffers()  


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(width, height)  
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab Assignment 1") 
glutDisplayFunc(display)
glutIdleFunc(animate)	
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()





#--------------------Task 2---------------------#


# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import random


# width = 720
# height = 480 
# speed = 5
# spawn = False
# ball = []
# freeze = False
# def points(x,y):
#     # glColor3f(r,g,b)
#     glPointSize(5)
#     glBegin(GL_POINTS)
#     glVertex2f(x,y)
#     glEnd()
    
# def properties(x,y):
#     directions = random.randint(0,3)
#     r = random.randint(0.0,1.0)
#     g = random.randint(0.0,1.0)
#     b = random.randint(0.0,1.0)
#     return [x-width//2, -(y-height//2),directions,r,g,b]

# def ballGen():
#     global spawn
#     if spawn:
#         for i in ball:
#             glColor3f(i[3],i[4],i[5])
#             points(i[0],i[1])


# def animate():

#     glutPostRedisplay()
#     global speed , ball
#     xmax = width//2
#     xmin = xmax * (-1)
#     ymax = height//2
#     ymin = ymax * (-1)
#     for i in ball:
#             if i[2] == 0: #NE
#                 i[0] =(i[0] +speed)
#                 i[1] =(i[1] +speed)
#             elif i[2] == 1:   #NW
#                 i[0] =(i[0] -speed)
#                 i[1] =(i[1] +speed)
#             elif i[2] == 2:   #WS
#                 i[0] =(i[0]-speed)
#                 i[1] =(i[1] -speed)
#             elif i[2] == 3:   #SE
#                 i[0] =(i[0] +speed)
#                 i[1] =(i[1] -speed)

#             if (i[0]>= xmax) and (i[2] == 3):
#                 i[2] = 2
#             elif (i[0]>= xmax) and (i[2] == 0):
#                 i[2] = 1
#             if (i[0]<= xmin) and (i[2] == 2):
#                 i[2] = 3
#             elif (i[0]<= xmin) and (i[2] == 1):
#                 i[2] = 0
            
#             if (i[1]>=ymax) and (i[2] == 0):
#                 i[2] = 3
#             elif (i[1] >= ymax) and (i[2] == 1):
#                 i[2] = 2
#             if (i[1] <=ymin) and (i[2] == 2):
#                 i[2] = 1
#             elif (i[1] <= ymin) and (i[2] == 3):
#                 i[2] = 0


# def mouseListener(button, state, x, y):	
#     global spawn, ball,balck
#     if button==GLUT_LEFT_BUTTON:
#         if(state == GLUT_DOWN):
#             spawn = True
#             ball += [properties(x,y)]           
        
#     if button==GLUT_RIGHT_BUTTON:
#         if state == GLUT_DOWN: 	
#             if spawn:
#                spawn = False
#             else:
#                spawn = True

#     glutPostRedisplay()
# def keyboardListener(key, x, y):

#     global speed
#     if key==b' ':
#         if speed == 0:
#             speed = 5
#         else:
#             speed = 0
        
#     glutPostRedisplay()


# def specialKeyListener(key, x, y):
#     global speed
#     if key==GLUT_KEY_UP:
#         speed += 1
#         print("Speed Increased")
#     if key== GLUT_KEY_DOWN:		
#         speed -= 1
#         print("Speed Decreased")



# def iterate():
#     glViewport(0, 0, width, height)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(-width/2, width/2, -height/2, height/2, -1, 1)
#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()

# def display():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     # glClearColor(1, 1, 1, 1) 
#     # glClearColor(1.0, 1.0, 1.0, 1.0)
#     glClearColor(0.0, 0.0, 0.0, 0.0)
#     glLoadIdentity()
#     gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
#     iterate()

#     # my work
#     ballGen()
    
#     glutSwapBuffers()  


# glutInit()
# glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
# glutInitWindowSize(width, height)  # window size
# glutInitWindowPosition(0, 0)
# wind = glutCreateWindow(b"Lab Assignment 1")  # window name
# glutDisplayFunc(display)
# glutIdleFunc(animate)	
# glutMouseFunc(mouseListener)
# glutKeyboardFunc(keyboardListener)
# glutSpecialFunc(specialKeyListener)


# glutMainLoop()
