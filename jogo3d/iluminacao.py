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



    def configurar_luz_direcional(self,light_id, direction, color, intensity):
        glLightfv(light_id, GL_POSITION, direction + [0])

        glLightfv(light_id, GL_DIFFUSE, [color[0] * intensity, color[1] * intensity, color[2] * intensity, 1])
        glLightfv(light_id, GL_SPECULAR, color + [1])

        glLightf(light_id, GL_CONSTANT_ATTENUATION, 1)
        glLightf(light_id, GL_LINEAR_ATTENUATION, 0)
        glLightf(light_id, GL_QUADRATIC_ATTENUATION, 0)

        glEnable(light_id)
        


    

    


