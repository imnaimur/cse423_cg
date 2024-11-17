from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


width = 720
height = 480 
speed = 0.1
spawn = False
ball = []
freeze = False

def points(x,y):
    r = random.randint(0.0,1.0)
    g = random.randint(0.0,1.0)
    b = random.randint(0.0,1.0)
    glColor3f(r,g,b)
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    
def coordinate(x,y):
    directions = random.randint(0,3)
    return [x-width//2, -(y-height//2),directions]

def ballGen():
    global spawn
    if spawn:
        for i in ball:
            points(i[0],i[1])


def animate():

    glutPostRedisplay()
    global speed , ball
    for i in ball:
        if i[2] == 0: #NE
            i[0] =(i[0] +speed)
            i[1] =(i[1] +speed)
        if i[2] == 1:   #NW
            i[0] =(i[0] -speed)
            i[1] =(i[1] +speed)
        if i[2] == 2:   #WS
            i[0] =(i[0]-speed)
            i[1] =(i[1] -speed)
        if i[2] == 3:   #SE
            i[0] =(i[0] +speed)
            i[1] =(i[1] -speed)



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
    global spawn, ball
    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):
            spawn = True
            ball += [coordinate(x,y)]
           
        
    if button==GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN: 	
           pass

    glutPostRedisplay()
def keyboardListener(key, x, y):

    global speed
    if key==b' ':
        if speed == 0:
            speed = 0.1
        else:
            speed = 0
        
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
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glLoadIdentity()
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    iterate()

    # my work
    ballGen()
    
    glutSwapBuffers()  


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(width, height)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab Assignment 1")  # window name
glutDisplayFunc(display)
glutIdleFunc(animate)	
# glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutKeyboardFunc(keyboardListener)

glutMainLoop()
# animate()