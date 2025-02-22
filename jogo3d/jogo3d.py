from cenario import *
import time
from zumbi3d import *


plantas=plantas_do_cenario()
menu=False
seletor=False
tempo_inteligente=0
tempo_de_criar_zumbi = tempo_anterior = time.time()
zumbis = []
posicaoz=[-1,0.1,1.2,2.3,3.3]
i = int(random.uniform(0,4))
zumbis.append(Zumbi_normal(10,0.6,posicaoz[i]))

def acao():
    global plantas,zumbis,tempo_inteligente,tempo_de_criar_zumbi,tempo_anterior,posicaoz

    for zumbi in zumbis:
        zumbi.desenhar()
        for _,planta in plantas.items():
            if planta.tipo == 'tiro':
                zumbi.verificar_colisao_Projeteis(planta.projeteis)
        zumbi.mover(list(plantas.values()))
        
    

    for _,planta in plantas.items():
        planta.desenhar()
        if planta.tipo == 'tiro':
            if planta.controle:
                planta.atualizar_projeteis(cordenadasDoSeletor(2))
            else:
                planta.atualizar_projeteis()
            
    
    # Faz a planta disparar a cada 1 segundo
    
    tempo_atual = time.time()
   
    if (tempo_atual - tempo_anterior) > 3 : 
        for _,planta in plantas.items():
            if planta.tipo == 'tiro':
                planta.disparar()
            if planta.tipo == 'girasol':
                planta.absorverLuzDoSol()
                planta.atualisarSol()

        tempo_anterior = tempo_atual

    
    if tempo_atual - tempo_de_criar_zumbi > 6:
        i = int(random.uniform(0,4))
        zumbis.append(Zumbi_normal(10,0.6,posicaoz[i]))
        tempo_de_criar_zumbi = tempo_atual
        tempo_inteligente+=1

    if tempo_inteligente == 6:
        i = int(random.uniform(0,4))
        zumbis.append(Zumbi_inteligente(10,0.6,posicaoz[i]))
        tempo_inteligente=0

def adicionar_plantas():
    global plantas
    num=get_selector_Menu()
    x,y,z=cordenadasDoSeletor(1)
    if num ==0:   
        plantas[chave(x,y,z)]=Planta(x,y,z)
    if num == 1:
        plantas[chave(x,y,z)]=Girasol(x,y,z)
    if num == 2:
        plantas[chave(x,y,z)]=planta_barreira(x,y,z)


def controle_de_planta():
    global plantas
    x,y,z=cordenadasDoSeletor(1)
    id=chave(x,y,z)
    if  id in plantas.keys():
        if plantas[id].tipo == 'tiro':
            modo_de_atack()
            plantas[id].controlar()
            return True
    return False








