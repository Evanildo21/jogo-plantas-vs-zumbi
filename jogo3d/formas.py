from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math
from PIL import Image
import os

def cube(color:list):
    vertices = [
            [-0.5, -0.5, -0.5],
            [0.5, -0.5, -0.5],
            [0.5, 0.5, -0.5],
            [-0.5, 0.5, -0.5],
            [-0.5, -0.5, 0.5],
            [0.5, -0.5, 0.5],
            [0.5, 0.5, 0.5],
            [-0.5, 0.5, 0.5],
        ]
    faces = [
            [0, 1, 2, 3], # front
            [1, 5, 6, 2], # dir
            [5, 4, 7, 6], # tras
            [4, 0, 3, 7], # esq
            [3, 2, 6, 7], # sup
            [4, 5, 1, 0], # inf
        ]

    normais = [
            [0, 0, -1],
            [1, 0, 0],
            [0, 0, 1],
            [-1, 0, 0],
            [0, 1, 0],
            [0, -1, 0]
        ]
    
    glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
    glMaterialfv(GL_FRONT, GL_SPECULAR,color)
    glMaterialfv(GL_FRONT, GL_AMBIENT, color)
    glMaterialfv(GL_FRONT, GL_SHININESS, 100)

    
    
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        glNormal3fv(normais[i])
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()
   

def piramide():
    vertices = [
        [1, 1, 1],
        [-1, -1, 1],
        [-1, 1, -1],
        [1, -1, -1],
    ]
    faces = [
        [0, 1, 2],
        [0, 1, 3],
        [0, 2, 3],
        [1, 2, 3],
    ]
    cores = [
        [0, 0.3921, 0], [0, 0.3921, 0], [0, 1, 0], [0, 1, 0],
    ]
    
    glBegin(GL_TRIANGLES)
    for face in faces:
        for vertex in face:
            glColor3fv(cores[vertex])
            glVertex3fv(vertices[vertex])
    glEnd()
    

def sphere(radius, slices, stacks,cor=list):
    cor.append(1)

    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, cor )  # Define cor da esfera

    for i in range(stacks):
        lat0 = np.pi * (-0.5 + float(i) / stacks)
        z0 = radius * np.sin(lat0)
        zr0 = radius * np.cos(lat0)

        lat1 = np.pi * (-0.5 + float(i + 1) / stacks)
        z1 = radius * np.sin(lat1)
        zr1 = radius * np.cos(lat1)

        glBegin(GL_QUAD_STRIP)
        for j in range(slices + 1):
            lng = 2 * np.pi * float(j) / slices
            x = np.cos(lng)
            y = np.sin(lng)

            # Normal para iluminação correta
            glNormal3f(x, y, z0)
            glVertex3f(x * zr0, y * zr0, z0)

            glNormal3f(x, y, z1)
            glVertex3f(x * zr1, y * zr1, z1)
        glEnd()


class Quads:
    def __init__(self, texture_file=None):
        here = os.path.dirname(os.path.abspath(__file__))  # Obtém o caminho absoluto
        self.texture_id = None
        self.cor = [1.0, 1.0, 1.0,1]  # Inicializa a cor padrão (branco)

        # Certifique-se de que o contexto OpenGL está ativo antes de chamar `glGenTextures`
        if texture_file:
            self.texture_id = load_texture(os.path.join(here, texture_file))

    def desenha(self):
       
        glMaterialfv(GL_FRONT, GL_DIFFUSE, self.cor)

        uvs = [[0, 0], [1, 0], [1, 1], [0, 1]]
        vertices = [[0, 0], [1, 0], [1, 1], [0, 1]]

        if self.texture_id:
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, self.texture_id)

        glBegin(GL_QUADS)
        glNormal3f(0, 1, 0)

        for i in range(4):
            glTexCoord2fv(uvs[i])
            glVertex2fv(vertices[i])

        glEnd()

        if self.texture_id:
            glDisable(GL_TEXTURE_2D)

    def mudarCor(self, cor):
        self.cor = cor


def quadrado(color:list):

    vetor=[ [ 0 , 0 ],
            [1, 0 ],
            [1,1],
            [ 0 ,1,]]
    
    glColor3f(*color)
    glBegin(GL_QUADS)
    for i in vetor:
        glVertex2f(i[0],i[1]) 
    glEnd()


def circle(radius,cor=list):
    cor.append(1)
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, cor )  # Define cor do círculo

    glBegin(GL_TRIANGLE_FAN)
    glNormal3f(0, 0, 1)  # Normal apontando para o eixo Z (iluminação correta)
    glVertex3f(0, 0, 0)  # Centro do círculo

    for angle in range(361):
        x = math.cos(math.radians(angle)) * radius
        y = math.sin(math.radians(angle)) * radius
        glVertex3f(x, y, 0)

    glEnd()
 

def load_texture(texture_file):
    try:
        image = Image.open(texture_file)
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        image = image.convert("RGB")  # Certifica que a imagem está no formato correto
        img_data = np.array(image, dtype=np.uint8)

        texture_id = glGenTextures(1)  # Garante que OpenGL está ativo antes
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.width, image.height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

        
        return texture_id

    except Exception as e:
        print(f"❌ Erro ao carregar textura: {e}")
        return None

class cubo_cenario:
    def __init__(self, texture_file=None):
        here = os.path.dirname(os.path.abspath(__file__)) 
        self.texture_id = None
        if texture_file:
            self.texture_id = load_texture(os.path.join(here, texture_file))

    def draw(self, x, y, z):
        vertices = [
            [-0.5, -0.5, -0.5],
            [0.5, -0.5, -0.5],
            [0.5, 0.5, -0.5],
            [-0.5, 0.5, -0.5],
            [-0.5, -0.5, 0.5],
            [0.5, -0.5, 0.5],
            [0.5, 0.5, 0.5],
            [-0.5, 0.5, 0.5],
        ]
        faces = [
            [0, 1, 2, 3],  # front
            [1, 5, 6, 2],  # dir
            [5, 4, 7, 6],  # tras
            [4, 0, 3, 7],  # esq
            [3, 2, 6, 7],  # sup
            [4, 5, 1, 0],  # inf
        ]
        #cordenadas da textura
        uvs = [ 
            [0, 0], [1, 0], [1, 1], [0, 1],
            [0, 0], [1, 0], [1, 1], [0, 1],
            [0, 0], [1, 0], [1, 1], [0, 1],
            [0, 0], [1, 0], [1, 1], [0, 1],
            [0, 0], [1, 0], [1, 1], [0, 1],
            [0, 0], [1, 0], [1, 1], [0, 1],
        ]

        # Ajustar normais para apontar para dentro
        normais = [
            [0, 0, -1],  
            [1, 0, 0],    
            [0, 0, 1],    
            [-1, 0, 0],   
            [0, 1, 0],    
            [0, -1, 0]    
        ]

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

        # Ajuste de luz principal
        glLightfv(GL_LIGHT0, GL_POSITION, [0.0, 0.0, 0.0, 1.0])  # Posição dentro do cubo
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])  # Reduzida para evitar excesso de brilho
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.6, 0.6, 0.6, 1.0])  # Luz difusa menos intensa
        glLightfv(GL_LIGHT0, GL_SPECULAR, [0.3, 0.3, 0.3, 1.0])  # Reflexos mais suaves

        # Ajuste do material
        glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.8, 0.8, 0.8, 1.0])
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0.2, 0.2, 0.2, 1.0])
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 20)  # Brilho reduzido


        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [1.0,1.0,1.0,1.0])
        glPushMatrix()
        glTranslatef(x, y, z)
        glScalef(30, 30, 35)

        if self.texture_id:
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, self.texture_id)

        glBegin(GL_QUADS)
        for i, face in enumerate(faces):
            glNormal3fv(normais[i])
            for j, vertex in enumerate(face):
                glTexCoord2fv(uvs[j])
                glVertex3fv(vertices[vertex])
        glEnd()

        if self.texture_id:
            glDisable(GL_TEXTURE_2D)
        
        glPopMatrix()



def cube_texture(texId):
    vertices = [
        [-0.5, -0.5, -0.5],
        [0.5, -0.5, -0.5],
        [0.5, 0.5, -0.5],
        [-0.5, 0.5, -0.5],
        [-0.5, -0.5, 0.5],
        [0.5, -0.5, 0.5],
        [0.5, 0.5, 0.5],
        [-0.5, 0.5, 0.5],
    ]
    faces = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [0, 1, 5, 4],
        [2, 3, 7, 6],
        [0, 3, 7, 4],
        [1, 2, 6, 5],
    ]
    
    normais = [
        [0,0,-1],
        [1,0,0],
        [0,0,1],
        [-1,0,0],
        [0,1,0],
        [0,-1,0],
    ]
    coordenadas_de_texturas = [
        [0,0],
        [1,0],
        [1,1],
        [0,1],
    ]
   
    glScale(1,1,1)
    glBindTexture(GL_TEXTURE_2D, texId)
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        glNormal3fv(normais[i])
        for j, vertex in enumerate(face): 
            glTexCoord2fv(coordenadas_de_texturas[j])
            glVertex3fv(vertices[vertex])
    glEnd()
    glBindTexture(GL_TEXTURE_2D, 0)
    
