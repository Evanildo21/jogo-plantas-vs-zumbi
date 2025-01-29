Documentação do Jogo 3D

Introdução

Este jogo 3D, implementado em Python, utiliza a biblioteca glfw para renderização e entrada do usuário.
O jogo apresenta um cenário interativo com câmera livre e entidades como plantas e zumbis.

Como Jogar

Setas Direcionais: Movimentam o seletor dentro do jogo.

Enter: Confirma a seleção no menu para escolher as planatas a serem adicionadas.

Space: muda a visão de camera porem nesta visão não pode adicionar platas

O jogo permite interagir com o ambiente e enfrentar desafios relacionados aos zumbis.

Estrutura do Código

O jogo é estruturado em vários arquivos Python, cada um com uma função específica:

jogo3d.py (Arquivo Principal)

  Gerencia a execução do jogo e a entrada do usuário.

  Define a função keyboard, que interpreta comandos do teclado.

  Controla a exibição de menus.

camera.py

  Gerencia a perspectiva da câmera no jogo.

  Permite rotação e movimentação dentro do ambiente 3D.

cenario.py

  Define os elementos do cenário.

  Gera e posiciona objetos no ambiente.

formas.py

  Contém funções relacionadas a objetos geométricos.

  Define formas usadas no cenário e entidades do jogo.

planta3d.py

  Implementa o comportamento das plantas dentro do jogo.

  Pode incluir interação com outras entidades.

zumbi3d.py

  Define o comportamento dos zumbis.

  Implementa movimentação e IA básica dos inimigos.

Considerações Finais

Este jogo pode ser expandido com novas mecanicas, como diferentes tipos de inimigos e interação mais complexa com o ambiente.

