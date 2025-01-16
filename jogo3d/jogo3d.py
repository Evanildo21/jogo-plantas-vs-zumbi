import glfw
from planta3d import *

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

while not glfw.window_should_close(window):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    glTranslatef(0, 0, -20)
    glRotate(angle,0,1,0)
    p.desenha()
    

    glfw.swap_buffers(window)
glfw.terminate()