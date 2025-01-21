import glfw
from planta3d import *
from cenario import *
from camera import *
angle = 0

def keyboard(window, key, scancode, action, mods):
    global angle
    if action == glfw.PRESS:
        if key == glfw.KEY_ENTER:
            angle+=3


if not glfw.init():
    raise Exception("Falha ao iniciar")

width, height = 800, 600
window = glfw.create_window(width, height, "Aula 3", None, None)
if not window:
    raise Exception("Falha ao criar a janela")



glfw.make_context_current(window)
glfw.set_key_callback(window,keyboard)
glEnable(GL_DEPTH_TEST)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, width / height, 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)




glClearColor(0 , 0.2, 0.5, 1)



p=planta(0,0,0)

glfw.set_key_callback(window, key_callback)
while not glfw.window_should_close(window):
    glfw.poll_events()
    process_input()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    camera()
    glRotate(angle,0,1,0)
    glTranslatef(0,0,0)
    cube()
    

    glfw.swap_buffers(window)
glfw.terminate()