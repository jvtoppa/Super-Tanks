import keyboard
import time
from graphics import *
import random
import math

#Algoritmo A* (adaptações feitas pelo grupo)
#Retirado de https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

#Todos as posições do mapa, centralizadas
pontos_mapa = [[(32, 32), (96, 32), (160, 32), (224, 32), (288, 32), (352, 32), (416, 32), (480, 32), (544, 32), (608, 32), (672, 32), (736, 32), (800, 32)],
              [(32, 96), (96, 96), (160, 96), (224, 96), (288, 96), (352, 96), (416, 96), (480, 96), (544, 96), (608, 96), (672, 96), (736, 96), (800, 96)],
              [(32, 160), (96, 160), (160, 160), (224, 160), (288, 160), (352, 160), (416, 160), (480, 160), (544, 160), (608, 160), (672, 160), (736, 160), (800, 160)],
              [(32, 224), (96, 224), (160, 224), (224, 224), (288, 224), (352, 224), (416, 224), (480, 224), (544, 224), (608, 224), (672, 224), (736, 224), (800, 224)],
              [(32, 288), (96, 288), (160, 288), (224, 288), (288, 288), (352, 288), (416, 288), (480, 288), (544, 288), (608, 288), (672, 288), (736, 288), (800, 288)],
              [(32, 352), (96, 352), (160, 352), (224, 352), (288, 352), (352, 352), (416, 352), (480, 352), (544, 352), (608, 352), (672, 352), (736, 352), (800, 352)],
              [(32, 416), (96, 416), (160, 416), (224, 416), (288, 416), (352, 416), (416, 416), (480, 416), (544, 416), (608, 416), (672, 416), (736, 416), (800, 416)]] 

pontos_mapaY = [32, 64, 96, 160, 224, 288, 352, 416]
pontos_mapaX = [32, 96, 160, 224, 288, 352, 416, 480, 544, 608, 672, 736, 800]


def Main (Titulo: str, W: int, H:int):
    #Posição inicial da AI
    start = (4, 12)
    astar_counter = 0 
    astar_c  = 0
    tamanho_astar = 0
    astar_valores = []
    astar_f = 0
    astar_j = 0
    colisao = 0
    startgame_counter = 0
    vida_counter = 0
    coli_counter = 0
    direção_bala = "d"

    win = GraphWin(Titulo, W, H, autoflush=False)
    framerate = 1/60.0

    #cenario
    cenario = Image(Point(416,224),"arcade_layout.png")
    cenario.draw(win)
    cenario2 = Image(Point(416,480), "tile.png")
    cenario2.draw(win)
    startgame = Image(Point(416,224),"start-game.png")
    game_over = Image(Point(416,224),"GAME_OVER.png")

    #apaga frames já usadas
    def apaga_tudo():

        lst[7].undraw()
        lst[6].undraw()
        lst[5].undraw()
        lst[4].undraw()
        lst[3].undraw()
        lst[2].undraw()
        lst[1].undraw()
        lst[0].undraw()

    #funcao pega coord
    def pega_cord(item):

        itemx = item.getAnchor().getX()
        itemy = item.getAnchor().getY()
        ponto = [itemx,itemy]
        return ponto

    def pega_cordbala(_bala):
        balax = _bala.getAnchor().getX()
        balay = _bala.getAnchor().getY()
        pontobalaa =[balax,balay]
        return pontobalaa

    #funcao para colisoes tiros-tank

    def colisao_tiro(tank,_bala,tankcord,balacord):
        distancia = math.dist(tankcord,balacord)
        nonlocal colisao
        if distancia <= 16:
            poscoltx = tank4.getAnchor().getX()
            poscolty = tank4.getAnchor().getY()
            colX = 800 - poscoltx
            colY = 352 - poscolty
            tank.move(colX,colY)
            _bala.move(200000,20000)
            colisao = 1
        elif distancia > 16 and distancia <= 1000:
            colisao = 0
    def colisao_tiro2(tank,_bala,tankcord,balacord):
        distancia = math.dist(tankcord,balacord)
        nonlocal vida_counter
        if distancia <= 16:
            poscoltx = lst[0].getAnchor().getX()
            poscolty = lst[0].getAnchor().getY()
            colX = 32 - poscoltx
            colY = 224 - poscolty
            for i in tank:
                i.move(colX,colY)
            _bala.move(200000,20000)
            vida_counter += 1




    # gera o obj tank e projetil
    
    #lst indica todos as animações possíveis para o tanque   
    lst = []
    
    for i in range(8):
        img = Image(Point(32,224), str(i) + ".png")
        lst.append(img)

    lst[2].draw(win)
    bala = Image(lst[0].getAnchor(),"tiro_cima.png")
    bala1 = Image(lst[0].getAnchor(),"tiro_direita.png")
    bala2 = Image(lst[0].getAnchor(),"tiro_baixo.png")
    bala3 = Image(lst[0].getAnchor(),"tiro_esquerda.png")
    bala4 = Image(lst[0].getAnchor(),"tiro_direita_baixo.png")
    bala5 = Image(lst[0].getAnchor(),"tiro_direita_cima.png")
    bala6 = Image(lst[0].getAnchor(),"tiro_esquerda_baixo.png")
    bala7 = Image(lst[0].getAnchor(),"tiro_esquerda_cima.png")
    tank4 = Image(Point(800,352), "maquina.png")
    bala_cima = Image(tank4.getAnchor(), 'tiro_cima_2.png')
    bala_direita = Image(tank4.getAnchor(), 'tiro_direita_2.png')
    bala_esquerda = Image(tank4.getAnchor(), 'tiro_esquerda_2.png')
    bala_baixo = Image(tank4.getAnchor(), 'tiro_baixo_2.png')
    tank4.draw(win)

   #vida gráficos
    vida = Image(Point(155,478), "vida.png")
    vida2 = Image(Point(192,478), "vida2.png")
    vida3 = Image(Point(229,478), "vida3.png")
    vida.draw(win)
    vida2.draw(win)
    vida3.draw(win)

    #scoreboard gráficos

    score = Text(Point(672, 477), '0')
    score.draw(win)
    score.setTextColor('white')
    score.setSize(30)
    #janela
    
    while win.closed == False:

        key = win.checkKey()
    #start-game
        if startgame_counter == 0:
            startgame.draw(win)
        elif startgame_counter == 60:
            startgame.undraw()
        if startgame_counter <= 60:
            startgame_counter += 1

    #vida-counter
        if vida_counter == 1:
            vida3.undraw()
        elif vida_counter == 2:
            vida2.undraw()
        elif vida_counter == 3:
            vida.undraw()
            tank4.undraw()
            apaga_tudo()
            bala.undraw()
            bala1.undraw()
            bala2.undraw()
            bala3.undraw()
            bala4.undraw()
            bala5.undraw()
            bala6.undraw()
            bala7.undraw()
            bala_cima.undraw()
            bala_baixo.undraw()
            bala_direita.undraw()
            bala_esquerda.undraw()
            game_over.draw(win)
            time.sleep(2)
            break
        


    #movimento
        if keyboard.is_pressed("w"):
            apaga_tudo()
            lst[1].draw(win)
            for i in range(8):
                lst[i].move(0,-2.5)
            direção_bala = "w"
            #a & d nested dentro do w
            if keyboard.is_pressed("a"):
                apaga_tudo()
                lst[7].draw(win)
                for i in range(8):
                    lst[i].move(-1.25,1.25)
                direção_bala = "wa"
            
            elif keyboard.is_pressed("d"):
                apaga_tudo()
                lst[5].draw(win)
                for i in range(8):
                    lst[i].move(1.25,1.25)
                direção_bala = "wd"


        if keyboard.is_pressed("a") and not keyboard.is_pressed("w"):

            apaga_tudo()
            lst[3].draw(win)
            for i in range(8):
                lst[i].move(-2.5,0)

            direção_bala = "a"
        

        if keyboard.is_pressed("s"):
            apaga_tudo()
            lst[0].draw(win)
            for i in range(8):
                lst[i].move(0, 2.5)
            direção_bala = "s"
            if keyboard.is_pressed("a"):
                apaga_tudo()
                lst[6].draw(win)
                for i in range(8):
                    lst[i].move(1.25,-1.25)
                direção_bala = "sa"
            
            elif keyboard.is_pressed("d"):
                apaga_tudo()
                lst[4].draw(win)
                for i in range(8):
                    lst[i].move(1.25,-1.25)
                direção_bala = "sd"
            

        if keyboard.is_pressed("d") and not keyboard.is_pressed("w") and not keyboard.is_pressed('s'):

            apaga_tudo()
            lst[2].draw(win)
            for i in range(8):
                lst[i].move(2.5, 0)

            direção_bala = "d"
    #movimento AI
        #valores posicionais do tanque aliado
        posAtx = lst[0].getAnchor().getX()
        posAty = lst[0].getAnchor().getY()
        tup = (int(posAtx), int(posAty)) 
        nearestX = min(pontos_mapaX, key=lambda x: abs(x-tup[0]))
        nearestY = min(pontos_mapaY, key=lambda y: abs(y-tup[1]))
        tupPos = (nearestX, nearestY)

        #valores posicionais do tanque inimigo
        posItx = tank4.getAnchor().getX()
        posIty = tank4.getAnchor().getY()
        tupI = (int(posItx), int(posIty))
        nearestXI = min(pontos_mapaX, key=lambda x: abs(x-tupI[0]))
        nearestYI = min(pontos_mapaY, key=lambda y: abs(y-tupI[1]))
        tupPosI = (nearestXI, nearestYI)
        
        #Compara os valores em pixels com os valores nas posições das matrizes (em tupla)

        mapa_compara = [(i, el.index(tupPos)) for i, el in enumerate(pontos_mapa) if tupPos in el]
        mapa_comparaI = [(i, el.index(tupPosI)) for i, el in enumerate(pontos_mapa) if tupPosI in el]
        start = mapa_comparaI[0]
        #Gera caminho A*
        if mapa_compara != []:
            
            astar_counter += 1
            
            if astar_counter == 10 or colisao == 1:
                astar_valores = []
                astar_counter = 0
                astar_c = 1
                astar_execucao = astar(maze, start, mapa_compara[0])
                print(astar_execucao)
                if colisao == 1:
                    coli_counter += 1
                    score.setText(coli_counter)
                colisao = 0
                
                
                #Gera o caminho a ser percorrido em pixels no formato tupla e adiciona a astar_valores
                for i in astar_execucao:
                    caminho_pixels = pontos_mapa[i[0]][i[1]]
                    #astar_valores é a lista que corresponde a todos os valores de tuplas posicionais geradas na ultima passada do algoritmo
                    astar_valores.append(caminho_pixels)
            #astar_c indica quantas vezes o movimento real é atualizado por frame para cada movimento astar

            if (astar_c < len(astar_valores) and astar_c >= 1):
                if astar_j == 0:
                    move_framesX = (int(astar_valores[astar_c][0]) - int(posItx))/30
                    move_framesY = (int(astar_valores[astar_c][1]) - int(posIty))/30
                if astar_f <= 30:
                    astar_j += 1
                    astar_f += 1
                    tank4.move(move_framesX,move_framesY)
                else:
                    astar_f = 1
                    astar_c += 1
                    astar_j = 0
                    astar_valores = []
                    
                    
    
    #Colisão aliado-parede

        if (posAtx >= 60 and posAty >= 60 and posAtx <= 196 and posAty <= 132) or (posAtx >= 188 and posAty >= 0 and posAtx <= 260 and posAty <= 196) or (posAtx >= 188 and posAty >= 250 and posAtx <= 260 and posAty <= 484) or (posAtx >= 60 and posAty >= 316 and posAtx <= 196 and posAty <= 390) or (posAtx >= 570 and posAty >= 0 and posAtx <= 644 and posAty <= 196) or (posAtx >= 636 and posAty >= 60 and posAtx <= 772 and posAty <= 132) or (posAtx >= 700 and posAty >= 60 and posAtx <= 772 and posAty <= 260) or (posAtx >= 570 and posAty >= 316 and posAtx <= 772 and posAty <= 390) or (posAtx >= 572 and posAty >= 252 and posAtx <= 644 and posAty <= 324) or (posAtx >= 700 and posAty >= 380 and posAtx <= 772 and posAty <= 452) or posAty <= 64 or posAty >= 416 or posAtx >= 832 or posAtx <= 0:
            for i in range(8):
                if direção_bala == 'w':
                    lst[i].move(0,2.5)
                elif direção_bala == 's':
                    lst[i].move(0,-2.5)
                elif direção_bala == 'd':
                    lst[i].move(-2.5,0)
                elif direção_bala == 'a':
                    lst[i].move(2.5,0)
                elif direção_bala == 'sd':
                    lst[i].move(-1.25,-1.25)
                elif direção_bala == 'sa':
                    lst[i].move(1.25,-1.25)
                elif direção_bala == 'wd':
                    lst[i].move(-1.25,1.25)
                elif direção_bala == 'wa':
                    lst[i].move(1.25,1.25)

    #tiros aliado
        
        if keyboard.is_pressed("z") and direção_bala == "w":
            bala.undraw()
            bala = Image(lst[0].getAnchor(),"tiro_cima.png")
            bala.draw(win)
        
        if keyboard.is_pressed("z") and direção_bala == "s":
            bala2.undraw()
            bala2 = Image(lst[0].getAnchor(),"tiro_baixo.png")
            bala2.draw(win)
            

        if keyboard.is_pressed("z") and direção_bala == "a":
            bala3.undraw()
            bala3 = Image(lst[0].getAnchor(),"tiro_esquerda.png")
            bala3.draw(win)

        if keyboard.is_pressed("z") and direção_bala == "d":
            bala1.undraw()
            bala1 = Image(lst[0].getAnchor(),"tiro_direita.png")
            bala1.draw(win)
        
        if keyboard.is_pressed("z") and direção_bala == "wa":
            bala7.undraw()
            bala7 = Image(lst[0].getAnchor(),"tiro_esquerda_cima.png")
            bala7.draw(win)
        
        if keyboard.is_pressed("z") and direção_bala == "wd":
            bala5.undraw()
            bala5 = Image(lst[0].getAnchor(),"tiro_direita_cima.png")
            bala5.draw(win)
        
        if keyboard.is_pressed("z") and direção_bala == "sd":
            bala4.undraw()
            bala4 = Image(lst[0].getAnchor(),"tiro_direita_baixo.png")
            bala4.draw(win)
        
        if keyboard.is_pressed("z") and direção_bala == "sa":
            bala6.undraw()
            bala6 = Image(lst[0].getAnchor(),"tiro_esquerda_baixo.png")
            bala6.draw(win)
        

        else:

            bala.move(0,-7)
            bala2.move(0,7)
            bala3.move(-7,0)
            bala1.move(7,0)
            bala7.move(-7,-7)
            bala5.move(7,-7)
            bala4.move(7,7)
            bala6.move(-7,7)
        
        #Tiros AI
        
        tiro_random = random.randint(0, 60)

        if tiro_random == 60:
            bala_baixo.undraw()
            bala_cima.undraw()
            bala_esquerda.undraw()
            bala_direita.undraw()
            bala_baixo = Image(tank4.getAnchor(),"tiro_baixo_2.png")
            bala_cima = Image(tank4.getAnchor(),"tiro_cima_2.png")
            bala_direita = Image(tank4.getAnchor(),"tiro_direita_2.png")
            bala_esquerda = Image(tank4.getAnchor(),"tiro_esquerda_2.png")
            bala_baixo.draw(win)
            bala_cima.draw(win)
            bala_direita.draw(win)
            bala_esquerda.draw(win)
        else:
            bala_baixo.move(0, 7)
            bala_cima.move(0, -7)
            bala_esquerda.move(-7, 0)
            bala_direita.move(7, 0)
        
        #Coordenadas para colisão da bala

        pontotank4 = pega_cord(tank4)
        pontobala  = pega_cordbala(bala)
        pontobala1 = pega_cordbala(bala1)
        pontobala2 = pega_cordbala(bala2)
        pontobala3 = pega_cordbala(bala3)
        pontobala4 = pega_cordbala(bala4)
        pontobala5 = pega_cordbala(bala5)
        pontobala6 = pega_cordbala(bala6)
        pontobala7 = pega_cordbala(bala7)
        pontoaliado = pega_cord(lst[0])
        pontobala_cima = pega_cordbala(bala_cima)
        pontobala_baixo = pega_cordbala(bala_baixo)
        pontobala_direita = pega_cordbala(bala_direita)
        pontobala_esquerda = pega_cordbala(bala_esquerda)



        #Colisões 
        colisao_tiro(tank4,bala,pontotank4,pontobala)
        colisao_tiro(tank4,bala1,pontotank4,pontobala1)
        colisao_tiro(tank4,bala2,pontotank4,pontobala2)
        colisao_tiro(tank4,bala3,pontotank4,pontobala3)
        colisao_tiro(tank4,bala4,pontotank4,pontobala4)
        colisao_tiro(tank4,bala5,pontotank4,pontobala5)
        colisao_tiro(tank4,bala6,pontotank4,pontobala6)
        colisao_tiro(tank4,bala7,pontotank4,pontobala7)
        colisao_tiro2(lst,bala_baixo,pontoaliado,pontobala_baixo)
        colisao_tiro2(lst,bala_cima,pontoaliado,pontobala_cima)
        colisao_tiro2(lst,bala_direita,pontoaliado,pontobala_direita)
        colisao_tiro2(lst,bala_esquerda,pontoaliado,pontobala_esquerda)
        

        
        #Este comando faz a janela ser atualizada a cada frame
        win.update()
        #Este comando faz com que o framerate fique sempre abaixo de 60fps
        time.sleep(framerate)

Main("Super Tanks", 832, 512)