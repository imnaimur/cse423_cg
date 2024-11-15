from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width = 1440
height = 1080
r = 1.0
g = 1.0
b = 1.0
a = 1.0


def points(x,y):
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

    
def lines(x1, x2, y1, y2):

    glColor3f(r, g, b)
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
    pass


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
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glLoadIdentity()
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    iterate()

    # my work
    house(480,360,120)
    # house(300,240,120)

    
    glutSwapBuffers()  


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(width, height)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab Assignment 1")  # window name
glutDisplayFunc(display)
glutMainLoop()
