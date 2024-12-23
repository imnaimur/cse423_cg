from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import os
import random


rocket_move = 0
paused = False
score = 0
width = 720
height = 800
speed_asteroids = 1
speed_fire = 1
circle_info = []
fireset = [360,215,5]
missed = 0
missed_fire = 0
firing = False

def asteroid():
    global circle_info
    circle_info = []
    for i in range(5):
        radious = random.randint(30,50)
        x = random.randint(radious, width - radious)
        y = height + random.randint(0, 100)
        circle_info.append([x, y, radious])
    
def zone_check(x0,y0,x1,y1):
    x_t0 = x0
    x_t1 = x1
    y_t0 = y0
    y_t1 = y1
    dy = y1 - y0
    dx = 1
    if x1 != x0:
        dx = x1 - x0
    slope = dy/dx
    line_pixels = []
    zone1 = zone2 = zone3 = False
    if slope>1:
        x_t0 = y0
        y_t0 = x0
        x_t1 = y1
        y_t1 = x1
        zone1 =True
    elif slope < -1:
        x_t0 = -y0
        x_t1 = -y1
        y_t0 = x0
        y_t1 = x1
        zone2 = True
    elif -1 <= slope < 0:
        x_t0 = x0
        x_t1 = x1
        y_t0 = -y0
        y_t1 = -y1
        zone3 = True
    return [x_t0,y_t0,x_t1,y_t1,zone1,zone2,zone3]
    
def mpl(x0, y0, x1, y1):
    x_t0 ,y_t0, x_t1, y_t1 , zone1, zone2, zone3 = zone_check(x0,y0,x1,y1)


    dy = y_t1 - y_t0
    dx = 1
    if x_t0 != x_t1:
        dx = x_t1 - x_t0
    d = (2 * dy ) - dx                         
    x, y = x_t0, y_t0


    while (x <= x_t1):
        if zone1:
            glVertex2f(y,x)
        elif zone2:

            glVertex2f(y,-x)
        elif zone3:

            glVertex2f(x,-y)
        else:
            glVertex2f(x,y)
        
        if d >= 0:
            d += (2*dy)-(2*dx)
            x+=1
            y+=1
        else:
            d += 2*dy
            x+=1

def octant_points(cx, cy, x, y):
    glVertex2f(cx + x, cy + y)
    glVertex2f(cx - x, cy + y)
    glVertex2f(cx + x, cy - y)
    glVertex2f(cx - x, cy - y)
    glVertex2f(cx + y, cy + x)
    glVertex2f(cx - y, cy + x)
    glVertex2f(cx + y, cy - x)
    glVertex2f(cx - y, cy - x)

def mpc(cx, cy, r):
    d = 1 - r
    x = 0
    y = r

    while x <= y:
        octant_points(cx,cy,x,y)
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1

def navigation_bar():
    glBegin(GL_POINTS)
    glColor(0,1,1)
    mpl(10,height-25,50,height-25)
    mpl(10,height-25,20,height-10)
    mpl(10,height-25,20,height-40)

    glColor(1,1,0)
    if paused:
        mpl(370,height,370,height-50)
        mpl(350,height-25,370,height)
        mpl(350,height-25,370,height-50)

    else:
        mpl(350,height,350,height-50)
        mpl(370,height,370,height-50)

    glColor3f(1, 0, 0)  
    mpl(width-50,height,width,height-50)
    mpl(width-50,height-50,width,height)
    glEnd()

def rocket():
    glBegin(GL_POINTS)
    glColor3f(1, 0.8, 0) 
    # Rocket body
    mpl(290+rocket_move,60,430+rocket_move,60)     #base
    mpl(330+rocket_move,60,330+rocket_move,160)
    mpl(390+rocket_move,60,390+rocket_move,160)
    mpl(330+rocket_move,160,360+rocket_move,210)
    mpl(360+rocket_move,210,390+rocket_move,160)
    mpl(330+rocket_move,160,390+rocket_move,160)
    mpl(290+rocket_move,60,330+rocket_move,110)
    mpl(390+rocket_move,110,430+rocket_move,60)

    # Rocket exaust
    mpl(335+rocket_move,10,335+rocket_move,60)
    mpl(345+rocket_move,10,345+rocket_move,60)
    mpl(335+rocket_move,10,345+rocket_move,10)

    mpl(355+rocket_move,10,355+rocket_move,60)
    mpl(365+rocket_move,10,365+rocket_move,60)
    mpl(355+rocket_move,10,365+rocket_move,10)

    mpl(375+rocket_move,10,375+rocket_move,60)
    mpl(385+rocket_move,10,385+rocket_move,60)
    mpl(375+rocket_move,10,385+rocket_move,10)



    glEnd()


def collision_check():
    global circle_info, paused, score,missed,firing 

    for circle in circle_info:
        distance = ((circle[0] - fireset[0])**2 + (circle[1] - fireset[1])**2)**0.5

        if distance <= fireset[2] + circle[2]:
            fireset[1] = 215
            circle_info.remove(circle)
            score += 1
            firing = False

            print("Score: ",score)
        
        if (290+rocket_move<= circle[0]<= 430+rocket_move) and (circle[1]+circle[2] <= 210):
            print("game over hit by asteroid")
            print("Score : ",score)
            os._exit(0)
    

def animate():
    global circle_info,speed_asteroids,fireset,missed_fire,missed,firing
    if paused:
        speed_asteroid = 0
    else: speed_asteroid = speed_asteroids

    if firing and not paused:
        fireset[1]+=2.5

    if fireset[1]>height:
        fireset[1] = 215
        firing = False
        missed_fire += 1
    
    if missed_fire == 3:
        print("game over! three miss fire\nScore: ",score)
        os._exit(0)
    


    glColor(1,0,1)
    for circle in circle_info:
        circle[1] -= speed_asteroid

    ground = True
    for circle in circle_info:
        if circle[1] - circle[2] > 0:
            ground = False
       
    if ground:
        missed += len(circle_info)
        if missed >= 3:
            print("game ove! three missed asteroid")
            print("Score : ",score)
            os._exit(0)
        asteroid()
    if firing:
        mpc(fireset[0],fireset[1],fireset[2])
    collision_check()
    
    glutPostRedisplay()


def specialKeyListener(key, x, y):
    global rocket_move,fireset

    if paused == False:
        if key== GLUT_KEY_LEFT:		
            if rocket_move > -360+80:
                rocket_move -=20
                fireset[0] -= 20
        if key== GLUT_KEY_RIGHT:		
            if rocket_move<360-80:
                rocket_move +=20
                fireset[0]+=20
    
    glutPostRedisplay()

def keyboardListener(key, x, y):
    global firing,rocket_move,fireset
    if paused == False:
        if key== b'a':		
            if rocket_move > -360+80:
                rocket_move -=20
                fireset[0] -= 20
        if key== b'd':		
            if rocket_move<360-80:
                rocket_move +=20
                fireset[0]+=20
        if key==b' ':
            firing = True
    glutPostRedisplay()

def mouseListener(button, state, x, y):	
    global paused,rocket_move,circle_info,fireset
    y = abs(y - height)
    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):
                if height-50 <= y <= height:
                    if 0<= x <= 50:
                        fireset[1] = 215
                        rocket_move = 0
                        circle_info = []
                        score = 0
                    elif 350 <= x <= 370:
                        if paused:
                            paused = False
                            print("resume")
                        else:
                            paused = True
                            print("Paused")
                    elif width-50 <= x <= width:
                        print("exited")
                        os._exit(0)
                    
     

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
    rocket()
    glBegin(GL_POINTS)
    glColor(1,0,1)
    for circle in circle_info:
        mpc(circle[0], circle[1], circle[2])

    glColor(1,1,0)
    mpc(fireset[0],fireset[1],fireset[2])
    glEnd()
    glutSwapBuffers()  

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(width, height)  
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab Assignment 2")
glutDisplayFunc(display)
glutIdleFunc(animate)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutKeyboardFunc(keyboardListener)

glutMainLoop()

