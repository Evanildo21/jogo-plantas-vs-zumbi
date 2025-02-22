import glfw
from camera import *
from iluminacao import iluminacao
from jogo3d import *

menu = False

def keyboard(window, key, scancode, action, mods):
    global menu,plantas,girasol,cam,seletor
    rotacaoDaCamera=cam.get_rotacao_camera()
    if action == glfw.PRESS:
        if rotacaoDaCamera == True: 
            if key == glfw.KEY_ENTER:   
                if controle_de_planta():
                    seletor = not seletor
        if menu == False:
            if key == glfw.KEY_LEFT:
                selector("ParaEsquerda",rotacaoDaCamera,seletor)
            if key == glfw.KEY_RIGHT:
                selector("ParaDireita",rotacaoDaCamera,seletor)
            if key == glfw.KEY_UP:
                selector("ParaCima",rotacaoDaCamera,seletor)
            if key ==glfw.KEY_DOWN:
                selector("ParaBaixo",rotacaoDaCamera,seletor)
        if rotacaoDaCamera == False: 
            if menu == True:
                if key == glfw.KEY_LEFT:
                    selector_Menu("ParaEsquerda")
                if key == glfw.KEY_RIGHT:
                    selector_Menu("ParaDireita") 
            
            if key == glfw.KEY_ENTER:
                    if menu==False:
                        menu=True
                    else:
                        adicionar_plantas()
                        menu=False 

        if key == glfw.KEY_SPACE:
            cam.process_input()

    elif action == glfw.RELEASE: pass 


if not glfw.init():
    raise Exception("Falha ao iniciar")

width, height = 800, 600
window = glfw.create_window(width, height, "Planta vs zumbi", None, None)
if not window:
    raise Exception("Falha ao criar a janela")


glfw.make_context_current(window)
glfw.set_key_callback(window,keyboard)
glfw.swap_interval(1)

glEnable(GL_DEPTH_TEST)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, width / height, 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)


glClearColor(1, 1, 0.8, 1)

luz = iluminacao()
cam=Camera()


while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    cam.exibir_camera()
    cenario()
    luz.configurar_luz_potual(GL_LIGHT1, [1, 6, -1], [1, 1, 1], 0.5)
    if menu==True:
        Menu()

    acao()

             
    glfw.swap_buffers(window)    
    time.sleep(1/60)
    glfw.poll_events()
    
glfw.terminate()