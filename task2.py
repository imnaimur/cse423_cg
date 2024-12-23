from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

rocket_x = 0.0
paused = False
score = 0
width = 720
height = 800


def mpl(x0, y0, x1, y1):
    x_t0 = x0
    x_t1 = x1
    y_t0 = y0
    y_t1 = y1
    dy = y1 - y0
    dx = x1 - x0
    slope = dy/dx
    print(slope,"slope")
    line_pixels = []
    zone1= False
    zone2= False
    zone3 = False


    if slope>1:
        x0,y0 = y0,x0
        print(x0,y0)
        x_t1 = y1
        y_t0 = x0
        y_t1 = x1
        zone1 =True
        print("zone1")
    elif slope < -1:
        x_t0 = -y0
        x_t1 = -y1
        y_t0 = x0
        y_t1 = x1
        zone2 = True
        print("zone2")

    elif -1 <= slope < 0:
        # x_t0 = -x0
        # x_t1 = -x1
        # y_t0 = y0
        # y_t1 = y1
        zone3 = True
        print("zone3")


    dy = y_t1 - y_t0
    dx = x_t1 - x_t0
    d = (2 * dy ) - dx                         
    print(d)
    x, y = x_t0, y_t0
    while (x <= x_t1) and (y<= y_t1):
        if zone1:
            line_pixels.append([y,x])
            glVertex2f(y,x)
        elif zone2:
            line_pixels.append([y,-x])
            glVertex2f(y,-x)
        elif zone3:
            line_pixels.append([x,y])
            glVertex2f(x,y)
        else:
            line_pixels.append([x,y])
            glVertex2f(x,y)
        
        if d >= 0:
            d += (2*dy)-(2*dx)
            x+=1
            y+=1
        else:
            d += 2*dy
            x+=1
    print(line_pixels)

def mpc(cx, cy, r):
    x = 0
    y = r
    d = 1 - r

    while x <= y:
        glVertex2f(cx + x, cy + y)
        glVertex2f(cx - x, cy + y)
        glVertex2f(cx + x, cy - y)
        glVertex2f(cx - x, cy - y)
        glVertex2f(cx + y, cy + x)
        glVertex2f(cx - y, cy + x)
        glVertex2f(cx + y, cy - x)
        glVertex2f(cx - y, cy - x)

        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 0.001
        x += 0.001

def draw_rocket():
    glBegin(GL_POINTS)
    glColor3f(1, 0.8, 0)  # Yellowish color
    # Rocket body
    mpl(rocket_x - 0.1, -0.8, rocket_x + 0.1, -0.8)  # Bottom line
    mpl(rocket_x - 0.1, -0.8, rocket_x - 0.1, -0.6)  # Left line
    mpl(rocket_x + 0.1, -0.8, rocket_x + 0.1, -0.6)  # Right line
    mpl(rocket_x - 0.1, -0.6, rocket_x, -0.5)  # Left diagonal
    mpl(rocket_x + 0.1, -0.6, rocket_x, -0.5)  # Right diagonal

    # Rocket fins
    mpl(rocket_x - 0.1, -0.8, rocket_x - 0.15, -0.85)
    mpl(rocket_x + 0.1, -0.8, rocket_x + 0.15, -0.85)

    # Exhaust lines
    mpl(rocket_x - 0.05, -0.8, rocket_x - 0.05, -0.9)
    mpl(rocket_x, -0.8, rocket_x, -0.9)
    mpl(rocket_x + 0.05, -0.8, rocket_x + 0.05, -0.9)
    glEnd()

def navigation_bar():
    glBegin(GL_POINTS)

    # Play/pause button (yellow triangle)
    # glColor3f(1, 0.8, 0)  # Yellow
    # mpl(0, 0.87, 0.05, 0.9)
    # mpl(0.05, 0.9, 0, 0.93)
    # mpl(0, 0.93, 0, 0.87)

    # # Restart button (blue arrow)
    # glColor3f(0, 1, 1)  # Cyan
    # mpl(0.85, 0.9, 0.9, 0.9)
    # mpl(0.9, 0.9, 0.87, 0.87)
    # mpl(0.87, 0.87, 0.85, 0.9)

    # Exit button (red cross)
    glColor3f(1, 0, 0)  # Red
    mpl(width-50,height,width,height-50)
    print("-----------Line 1 done----------")
    mpl(width-50,height-50,width,height)
    print("-----------Line 2 done----------")
    glEnd()

def keyboard(key, x, y):
    global rocket_x, paused
    if key == b'a':  # Move left
        rocket_x -= 0.05
    elif key == b'd':  # Move right
        rocket_x += 0.05
    elif key == b'p':  # Play/pause
        paused = not paused
    elif key == b'r':  # Restart
        rocket_x = 0.0
    elif key == b'q':  # Exit
        glutLeaveMainLoop()

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
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # glClearColor(1, 1, 1, 1) 
    glClearColor(0.0, 0.0, 0.0, 0.0)
    
    glLoadIdentity()
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    iterate()

    # my work
    navigation_bar()
    
    glutSwapBuffers()  

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(width, height)  
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab Assignment 1") 
glutDisplayFunc(display)
# glutIdleFunc(display)
# glutSpecialFunc(specialKeyListener)
# glutMouseFunc(mouseListener)
glutMainLoop()

