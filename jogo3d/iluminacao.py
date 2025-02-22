from OpenGL.GL import *
from OpenGL.GLU import *


class iluminacao:
    def __init__(self,luz_ambiente=[0.5,0.5,0.5,1]):
        #LUZ
        glEnable(GL_LIGHTING)
        glEnable(GL_DEPTH_TEST)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.15, 0.15, 0.15, 1])


    def configurar_luz_potual(self,light_id, position, color, intensity):
        glLightfv(light_id, GL_POSITION, position + [1])
        glLightfv(light_id, GL_DIFFUSE, [color[0] * intensity, color[1] * intensity, color[2] * intensity, 1])
        glLightfv(light_id, GL_SPECULAR, color + [1])

        glLightf(light_id, GL_CONSTANT_ATTENUATION, 0)
        glLightf(light_id, GL_LINEAR_ATTENUATION, 0.1)
        glLightf(light_id, GL_QUADRATIC_ATTENUATION, 0.01)

        glEnable(light_id)

        #self.desenhar_esfera(position, color)


    def desenhar_esfera(self,position, cor):
        glPushMatrix()
        glTranslatef(position[0], position[1], position[2])

        shininess = 50

        glMaterialfv(GL_FRONT, GL_DIFFUSE, cor + [1])
        glMaterialfv(GL_FRONT, GL_SPECULAR, cor + [1])
        glMaterialfv(GL_FRONT, GL_AMBIENT, cor + [1])
        glMaterialfv(GL_FRONT, GL_SHININESS, shininess)

        quadric = gluNewQuadric()
        gluSphere(quadric, 0.5, 32, 32)
        glPopMatrix()


    def configurar_luz_direcional(self,light_id, direction, color, intensity):
        glLightfv(light_id, GL_POSITION, direction + [0])

        glLightfv(light_id, GL_DIFFUSE, [color[0] * intensity, color[1] * intensity, color[2] * intensity, 1])
        glLightfv(light_id, GL_SPECULAR, color + [1])

        glLightf(light_id, GL_CONSTANT_ATTENUATION, 1)
        glLightf(light_id, GL_LINEAR_ATTENUATION, 0)
        glLightf(light_id, GL_QUADRATIC_ATTENUATION, 0)

        glEnable(light_id)
        self.desenhar_linha(direction)


    def desenhar_linha(self,direction):
        glPushMatrix()
        glTranslatef(0, 0, 0)

        glBegin(GL_LINES)
        glVertex3f(0, 0, 0)
        glVertex3f(direction[0], direction[1], direction[2])
        glEnd()
        glPopMatrix()


    def configurar_luz_spot(self,light_id, position, direction, color, intensity, cutoff, exponent):
        glLightfv(light_id, GL_POSITION, position + [1])

        glLightfv(light_id, GL_SPOT_DIRECTION, direction)

        glLightfv(light_id, GL_DIFFUSE, [color[0] * intensity, color[1] * intensity, color[2] * intensity, 1])
        glLightfv(light_id, GL_SPECULAR, color + [1])

        glLightf(light_id, GL_SPOT_CUTOFF, cutoff)
        glLightf(light_id, GL_SPOT_EXPONENT, exponent)

        glLightf(light_id, GL_CONSTANT_ATTENUATION, 0)
        glLightf(light_id, GL_LINEAR_ATTENUATION, 0.1)
        glLightf(light_id, GL_QUADRATIC_ATTENUATION, 0.01)

        glEnable(light_id)

        self.desenhar_esfera(position, color)
        glPushMatrix()
        glTranslatef(position[0], position[1], position[2])

        glBegin(GL_LINES)
        glVertex3f(0, 0, 0)
        glVertex3f(direction[0], direction[1], direction[2])
        glEnd()
        glPopMatrix()

