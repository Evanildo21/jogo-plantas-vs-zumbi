import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np



#Variáveis da câmera
camera_pos = np.array([0.0, 0.0, 3])
camera_front = np.array([0.0, 0.0, -1.0])
camera_up = np.array([0.0, 1.0, 0.0])
camera_speed = 0.01

keys = {}

def camera():
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
    global camera_pos, camera_front, camera_up, camera_speed,delta_yaw,yaw
    if keys.get(glfw.KEY_W, False):
        camera_pos += camera_speed * camera_front
    if keys.get(glfw.KEY_S, False):
        camera_pos -= camera_speed * camera_front
    if keys.get(glfw.KEY_A, False):
        camera_pos -= np.cross(camera_front, camera_up) * camera_speed
    if keys.get(glfw.KEY_D, False):
        camera_pos += np.cross(camera_front, camera_up) * camera_speed
    if keys.get(glfw.KEY_UP,False):
        camera_pos += camera_up * camera_speed
    if keys.get(glfw.KEY_DOWN,False):
        camera_pos -= camera_up * camera_speed
    if keys.get(glfw.KEY_N):  # Rotação para a esquerda
        yaw -= delta_yaw
        update_camera_direction()
    if keys.get(glfw.KEY_M):  # Rotação para a direita
        yaw += delta_yaw
        update_camera_direction()
