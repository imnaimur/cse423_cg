from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)


    #call the draw methods here

    # draw circle
    # glPointSize(50)
    # glBegin(GL_POINTS)
    # glVertex(250,250)
    # glEnd()

    # glPointSize(30)
    # glBegin(GL_POINTS)
    # glVertex(350,250)
    # glEnd()


    # draw lines
    glLineWidth(50)
    glBegin(GL_LINES)
    glVertex(250,250)
    glVertex(400,250)

    glColor3f(1.0,0.0,1)
    glVertex(250,250)
    glVertex(250,400)

    glColor3f(0.0,1.0,0)
    glVertex(250,400)
    glVertex(400,250)

    glEnd()

    # draw_points(250, 250)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(960,720) #window size 960 720
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Lab 01") #window name
glutDisplayFunc(showScreen)

glutMainLoop()