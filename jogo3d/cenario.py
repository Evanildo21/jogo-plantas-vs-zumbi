
from OpenGL.GL import *
from formas import *
from planta3d import *
from camera import *


plantas={}

class seleção:
    def __init__(self,x,y,z,cor=[1.0, 1.0, 0]):
        self.x= x
        self.y= y
        self.z=z
        self.color = cor
        self.coluna=1
      
    def desenha(self):   
        glPushMatrix()
        glTranslatef(self.x, self.y,self.z)
        glScalef(1,0.1,1)
        cube(self.color)
        glPopMatrix()

       
    def cordenadas(self):
        return self.x,self.y+0.3,self.z
    
    def mudar(self,key):
        
        if key =="ParaEsquerda":
            if self.z > 0:
                self.z-=1.1
                
        if key =="ParaDireita":
            if self.z < 3:
                self.z+=1.1
                
        if key == "ParaBaixo":
            if self.x > -4:
                self.x-=1.1
                self.coluna-=1
        if key == "ParaCima":
            if self.x < 4:
                self.x+=1.1
                self.coluna+=1
                
                
   
    def mudarP(self,key):
        
        if key =="ParaCima":
            if self.z > 0:
                self.z-=1.1
        if key =="ParaBaixo":
            if self.z < 3:
                self.z+=1.1
        if key == "ParaEsquerda":
            if self.x > -4:
                self.x-=1.1
                self.coluna-=1
                
        if key == "ParaDireita":
            if self.x < 4:
                self.x+=1.1
                self.coluna+=1
                


class Gramado:
    def __init__(self,x,z):
        self.x= x
        self.z= z
        here = os.path.dirname(os.path.abspath(__file__))
        if not hasattr(gramado, 'texturagrama'): 
            self.texturagrama = load_texture(os.path.join(here, 'grama.png'))
           # self.texturasolo = load_texture(os.path.join(here,"c:/Users/POSITIVO/Documents/computação grafica/cg/jogo plantas vs zumbi/jogo3d/soloplantavszumbies.jpg" ))
        
    def desenha(self):
    
        glPushMatrix()
        glTranslatef(self.x, 0, self.z)
        glScalef(1, 0.1, 1)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texturagrama)
        cube_texture(self.texturagrama)
        glBindTexture(GL_TEXTURE_2D, 0)
        glDisable(GL_TEXTURE_2D)
        glPopMatrix()

        

    
selecionador=seleção(-4,0.1,-1)
selecionador_disparo=seleção(4.8,0.1,-1,[0.8,0,0])
atak=False

def modo_de_atack():
    global atak,aproxima
    atak= not atak
    if atak:
        aproximacao(coluna_do_seletor())
    else :
        aproximacao(0)

def cenario():
    global gramado,mundo
    
    mundo.draw(0,11,0)

    for i in gramado:
       i.desenha()

    selecionador.desenha()
    if atak:
        selecionador_disparo.desenha()


p=0
opsoes=[]
mundo=None
gramado=[]
def carregar_menu():
    global opsoes,mundo,gramado
    mundo=cubo_cenario("cemiterio.png")
    opsoes.append(Quads("tiro.png") )
    opsoes.append(Quads("girasol.png") )
    opsoes.append(Quads("b.png") )
   
    x=-4
    z=-1
    for i in range(5):
        for j in range(9):
            gramado.append(Gramado(x,z))
            x=x+1.1
        z=z+1.1
        x=-4
    
   



def Menu():
    global opsoes
    glPushMatrix()
    glTranslatef(-4.5,2,1)
    glScalef(8.2,3,3)
    quadrado([0,1,0.5])
    glPopMatrix()
    opsoes[p].mudarCor([1,1,0])
    x=-4
    y=3.5
    c=0
  
    while(x<3): 
        glPushMatrix()
        glTranslatef(x,y,1.1)
        if c < len(opsoes):
            opsoes[c].desenha()
        glPopMatrix()
        x+=1.5
        c+=1
    
def selector_Menu(direção:str):
    global p,opsoes
    if direção == "ParaEsquerda":
        if p > 0:
            opsoes[p].mudarCor([1,1,1])
            p-=1
    if direção == "ParaDireita":
        if p < 2:
            opsoes[p].mudarCor([1,1,1])
            p+=1
            
def get_selector_Menu()->int:
    global p
    return p

def selector(direção:str,camera:bool,x):
    global selecionador,selecionador_disparo
    if camera == False:
        selecionador.mudarP(direção)
    else:
        if x==False:
            selecionador.mudar(direção)
        else:
            selecionador_disparo.mudar(direção) 

def cordenadasDoSeletor(x):
    global selecionador,selecionador_disparo
    if x==1:
        return selecionador.cordenadas()
    else:
        return selecionador_disparo.cordenadas()
    
def coluna_do_seletor():
    global selecionador
    return selecionador.coluna

def chave(x,y,z)->float:
    return  x*z

def atacar_planta(x:float,atack):
    global plantas
    status = plantas[x].sofrer_dano(atack)
    
    if not status:
        plantas.pop(x)

def plantas_do_cenario()->dict:
        global plantas
        return plantas

