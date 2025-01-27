import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np


#Variáveis da câmera
camera_pos = np.array([0, 3, 14])
camera_front = np.array([0, 0, -1.0])
camera_up = np.array([0.0, 1.0, 0.0])
camera_speed = 0.1

keys = {}

rotation_index = False




def camera():
    global rotation_index
    vetor=[[0.5, 3.5, 15],
           [0, 0, -1.0],
           [0.0, 1.0, 0.0]]
    c=[x + y for x,y in zip(vetor[0],vetor[1])]
    if rotation_index == True:
        d_input()
    gluLookAt(vetor[0][0],vetor[0][1],vetor[0][2],c[0],c[1],c[2],vetor[2][0],vetor[2][1],vetor[2][2])


def d_input():
    
    glTranslated(13,1,-13)
    glRotatef(90,0,1,0)
    
    






def camer():
    global camera_pos, camera_front, camera_up
    glLoadIdentity()
    camera_target = camera_pos + camera_front
    gluLookAt(camera_pos[0], camera_pos[1], camera_pos[2], camera_target[0], camera_target[1], camera_target[2], camera_up[0], camera_up[1], camera_up[2])

def key_callback(window, key, scancode, action, mods):
    if action == glfw.PRESS:
        keys[key] = True
    elif action == glfw.RELEASE:
        keys[key] = False

# Variáveis globais para controle da câmera
yaw = -90.0  # Ângulo inicial em graus (direção horizontal)
pitch = 0.0  # Ângulo inicial em graus (direção vertical)
delta_yaw = 2.0  # Incremento de rotação em graus
# Função para calcular a direção da câmera
def update_camera_direction():
    global camera_front, yaw, pitch
    direction = np.array([
        np.cos(np.radians(yaw)) * np.cos(np.radians(pitch)),
        np.sin(np.radians(pitch)),
        np.sin(np.radians(yaw)) * np.cos(np.radians(pitch))
    ])
    camera_front = direction / np.linalg.norm(direction)


def process_input():
    global rotation_index
    if keys.get(glfw.KEY_W, False):
        if rotation_index == True:
            rotation_index = False
        else:   
            rotation_index = True
        