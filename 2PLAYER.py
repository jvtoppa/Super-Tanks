import keyboard
import time
from graphics import *
import random
import math

#Algoritmo A* (adaptações feitas pelo grupo)
#Retirado de https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2


def Main (Titulo: str, W: int, H:int):



    #scoreboard gráficos

    score1 = 1
    score2 = 1


    score = Text(Point(680, 477), F"{str(score1)} -- {str(score2)}")
    score.setTextColor('white')
    score.setSize(30)


    win = GraphWin(Titulo, W, H, autoflush=False)
    framerate = 1/60.0
    colisao = 0

    #cenario
    cenario = Image(Point(416,224),"arcade_layout.png")
    cenario.draw(win)
    #cenario2 = Image(Point(416,480), "tile.png")
    #cenario2.draw(win)
    startgame = Image(Point(416,224),"start-game.png")
    game_over = Image(Point(416,224),"GAME_OVER.png")
    #score.draw(win)
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

    def apaga_tudo2():

        lst2[7].undraw()
        lst2[6].undraw()
        lst2[5].undraw()
        lst2[4].undraw()
        lst2[3].undraw()
        lst2[2].undraw()
        lst2[1].undraw()
        lst2[0].undraw()

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
    contador1 = 0

    def colisao_tiro(tank,_bala,tankcord,balacord):
        nonlocal score1
        nonlocal score
        nonlocal contador1
        
        
        distancia = math.dist(tankcord,balacord)

    
        if distancia <= 16:
            poscoltx = tank.getAnchor().getX()
            poscolty = tank.getAnchor().getY()
            colX = 800 - poscoltx
            colY = 352 - poscolty
            tank.move(colX,colY)
            _bala.move(200000,20000)


            
            


    def colisao_tiro2(tank,_bala,tankcord,balacord):
        distancia = math.dist(tankcord,balacord)
        nonlocal score2
        nonlocal score
    
        if distancia <= 16:
            poscoltx = tank.getAnchor().getX()
            poscolty = tank.getAnchor().getY()
            colX = 32 - poscoltx
            colY = 224 - poscolty
            tank.move(colX,colY)
            _bala.move(200000,20000)
            score2 += 1
            score.undraw()
            score = Text(Point(680, 477), F"{str(score1)} -- {str(score2)}")
            score.setTextColor('white')
            score.setSize(30)
            score.draw(win)
     
  





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


# player 2

    lst2 = []

    for f in range(8):
        img = Image(Point(800,352), str(f) + "_.png")
        lst2.append(img)

    lst2[2].draw(win)
    bala_0 = Image(lst2[0].getAnchor(),"tiro_cima.png")
    bala1_1 = Image(lst2[0].getAnchor(),"tiro_direita.png")
    bala2_2 = Image(lst2[0].getAnchor(),"tiro_baixo.png")
    bala3_3 = Image(lst2[0].getAnchor(),"tiro_esquerda.png")
    bala4_4 = Image(lst2[0].getAnchor(),"tiro_direita_baixo.png")
    bala5_5 = Image(lst2[0].getAnchor(),"tiro_direita_cima.png")
    bala6_6 = Image(lst2[0].getAnchor(),"tiro_esquerda_baixo.png")
    bala7_7 = Image(lst2[0].getAnchor(),"tiro_esquerda_cima.png")
    direção_bala2 = "o"



   #vida gráficos
    vida = Image(Point(155,478), "vida.png")
    vida2 = Image(Point(192,478), "vida2.png")
    vida3 = Image(Point(229,478), "vida3.png")
    #vida.draw(win)
    #vida2.draw(win)
    #vida3.draw(win)


    #janela
    
    while win.closed == False:

        key = win.checkKey()

    #vida-counter
      
        


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


    #movimento 2

        if keyboard.is_pressed("up"):
            apaga_tudo2()
            lst2[1].draw(win)
            for i in range(8):
                lst2[i].move(0,-2.5)
            direção_bala2 = "o"
            #a & d nested dentro do w
            if keyboard.is_pressed("left"):
                apaga_tudo2()
                lst2[7].draw(win)
                for i in range(8):
                    lst2[i].move(-1.25,1.25)
                direção_bala2 = "ok"
            
            elif keyboard.is_pressed("right"):
                apaga_tudo2()
                lst2[5].draw(win)
                for i in range(8):
                    lst2[i].move(1.25,1.25)
                direção_bala2 = "oç"


        if keyboard.is_pressed("left") and not keyboard.is_pressed("up"):

            apaga_tudo2()
            lst2[3].draw(win)
            for i in range(8):
                lst2[i].move(-2.5,0)

            direção_bala2 = "k"
        

        if keyboard.is_pressed("down"):
            apaga_tudo2()
            lst2[0].draw(win)
            for i in range(8):
                lst2[i].move(0, 2.5)
            direção_bala2 = "l"
            if keyboard.is_pressed("left"):
                apaga_tudo2()
                lst2[6].draw(win)
                for i in range(8):
                    lst2[i].move(1.25,-1.25)
                direção_bala2 = "lk"
            
            elif keyboard.is_pressed("right"):
                apaga_tudo2()
                lst2[4].draw(win)
                for i in range(8):
                    lst2[i].move(1.25,-1.25)
                direção_bala2 = "çl"
            

        if keyboard.is_pressed("right") and not keyboard.is_pressed("up") and not keyboard.is_pressed('down'):

            apaga_tudo2()
            lst2[2].draw(win)
            for i in range(8):
                lst2[i].move(2.5, 0)

            direção_bala2 = "ç"



    #movimento AI
        #valores posicionais do tanque aliado
        posAtx = lst[0].getAnchor().getX()
        posAty = lst[0].getAnchor().getY()
        tup = (int(posAtx), int(posAty)) 

        #valores posicionais do tanque inimigo
        posItx = lst2[0].getAnchor().getX()
        posIty = lst2[0].getAnchor().getY()


    

                
                
                    
                    
    
    #Colisão aliado-parede

        if (posAtx >= 62 and posAty >= 62 and posAtx <= 190 and posAty <= 130) or (posAtx >= 190 and posAty >= 0 and posAtx <= 254 and posAty <= 190) or (posAtx >= 192 and posAty >= 256 and posAtx <= 256 and posAty <= 480) or (posAtx >= 64 and posAty >= 320 and posAtx <= 192 and posAty <= 384) or (posAtx >= 576 and posAty >= 0 and posAtx <= 640 and posAty <= 192) or (posAtx >= 640 and posAty >= 64 and posAtx <= 768 and posAty <= 128) or (posAtx >= 704 and posAty >= 64 and posAtx <= 768 and posAty <= 256) or (posAtx >= 576 and posAty >= 320 and posAtx <= 768 and posAty <= 384) or (posAtx >= 576 and posAty >= 256 and posAtx <= 640 and posAty <= 320) or (posAtx >= 704 and posAty >= 384 and posAtx <= 768 and posAty <= 448) or posAty <= 0 or posAty >= 448 or posAtx >= 832 or posAtx <= 0:
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
    
        if (posItx >= 62 and posIty >= 62 and posItx <= 190 and posIty <= 130) or (posItx >= 190 and posIty >= 0 and posItx <= 254 and posIty <= 190) or (posItx >= 192 and posIty >= 256 and posItx <= 256 and posIty <= 480) or (posItx >= 64 and posIty >= 320 and posItx <= 192 and posIty <= 384) or (posItx >= 576 and posIty >= 0 and posItx <= 640 and posIty <= 192) or (posItx >= 640 and posIty >= 64 and posItx <= 768 and posIty <= 128) or (posItx >= 704 and posIty >= 64 and posItx <= 768 and posIty <= 256) or (posItx >= 576 and posIty >= 320 and posItx <= 768 and posIty <= 384) or (posItx >= 576 and posIty >= 256 and posItx <= 640 and posIty <= 320) or (posItx >= 704 and posIty >= 384 and posItx <= 768 and posIty <= 448) or posIty <= 0 or posIty >= 448 or posItx >= 832 or posItx <= 0:
            for i in range(8):
                if direção_bala2 == 'o':
                    lst2[i].move(0,2.5)
                elif direção_bala2 == 'l':
                    lst2[i].move(0,-2.5)
                elif direção_bala2 == 'ç':
                    lst2[i].move(-2.5,0)
                elif direção_bala2 == 'k':
                    lst2[i].move(2.5,0)
                elif direção_bala2 == 'çl':
                    lst2[i].move(-1.25,-1.25)
                elif direção_bala2 == 'lk':
                    lst2[i].move(1.25,-1.25)
                elif direção_bala2 == 'oç':
                    lst2[i].move(-1.25,1.25)
                elif direção_bala2 == 'çl':
                    lst2[i].move(1.25,1.25)


    

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



    #tiros aliado 2
        
        if keyboard.is_pressed("n") and direção_bala2 == "o":
            bala_0.undraw()
            bala_0 = Image(lst2[0].getAnchor(),"tiro_cima.png")
            bala_0.draw(win)
        
        if keyboard.is_pressed("n") and direção_bala2 == "l":
            bala2_2.undraw()
            bala2_2 = Image(lst2[0].getAnchor(),"tiro_baixo.png")
            bala2_2.draw(win)
            

        if keyboard.is_pressed("n") and direção_bala2 == "k":
            bala3_3.undraw()
            bala3_3 = Image(lst2[0].getAnchor(),"tiro_esquerda.png")
            bala3_3.draw(win)

        if keyboard.is_pressed("n") and direção_bala2 == "ç":
            bala1_1.undraw()
            bala1_1 = Image(lst2[0].getAnchor(),"tiro_direita.png")
            bala1_1.draw(win)
        
        if keyboard.is_pressed("n") and direção_bala2 == "ok":
            bala7_7.undraw()
            bala7_7 = Image(lst2[0].getAnchor(),"tiro_esquerda_cima.png")
            bala7_7.draw(win)
        
        if keyboard.is_pressed("n") and direção_bala2 == "oç":
            bala5_5.undraw()
            bala5_5 = Image(lst2[0].getAnchor(),"tiro_direita_cima.png")
            bala5_5.draw(win)
        
        if keyboard.is_pressed("n") and direção_bala2 == "çl":
            bala4_4.undraw()
            bala4_4 = Image(lst2[0].getAnchor(),"tiro_direita_baixo.png")
            bala4_4.draw(win)
        
        if keyboard.is_pressed("n") and direção_bala2 == "lk":
            bala6_6.undraw()
            bala6_6 = Image(lst2[0].getAnchor(),"tiro_esquerda_baixo.png")
            bala6_6.draw(win)
  

        else:

            bala_0.move(0,-7)
            bala2_2.move(0,7)
            bala3_3.move(-7,0)
            bala1_1.move(7,0)
            bala7_7.move(-7,-7)
            bala5_5.move(7,-7)
            bala4_4.move(7,7)
            bala6_6.move(-7,7)
            bala.move(0,-7)
            bala2.move(0,7)
            bala3.move(-7,0)
            bala1.move(7,0)
            bala7.move(-7,-7)
            bala5.move(7,-7)
            bala4.move(7,7)
            bala6.move(-7,7)
        
       
        #Coordenadas para colisão da bala

        pontotank4 = pega_cord(lst2[0])
        pontobala  = pega_cordbala(bala)
        pontobala1 = pega_cordbala(bala1)
        pontobala2 = pega_cordbala(bala2)
        pontobala3 = pega_cordbala(bala3)
        pontobala4 = pega_cordbala(bala4)
        pontobala5 = pega_cordbala(bala5)
        pontobala6 = pega_cordbala(bala6)
        pontobala7 = pega_cordbala(bala7)
        pontoaliado = pega_cord(lst[0])

        pontobala_0  = pega_cordbala(bala_0)
        pontobala1_1 = pega_cordbala(bala1_1)
        pontobala2_2 = pega_cordbala(bala2_2)
        pontobala3_3 = pega_cordbala(bala3_3)
        pontobala4_4 = pega_cordbala(bala4_4)
        pontobala5_5 = pega_cordbala(bala5_5)
        pontobala6_6 = pega_cordbala(bala6_6)
        pontobala7_7 = pega_cordbala(bala7_7)
    







        #colisoes com o tank 2


        for i in range(8):
            	colisao_tiro(lst2[i],bala,pontotank4,pontobala)

        for i in range(8):
                colisao_tiro(lst2[i],bala1,pontotank4,pontobala1)

        for i in range(8):
                colisao_tiro(lst2[i],bala2,pontotank4,pontobala2)

        for i in range(8):
                colisao_tiro(lst2[i],bala3,pontotank4,pontobala3)

        for i in range(8):
                colisao_tiro(lst2[i],bala4,pontotank4,pontobala4)

        for i in range(8):
                colisao_tiro(lst2[i],bala5,pontotank4,pontobala5)

        for i in range(8):
                colisao_tiro(lst2[i],bala6,pontotank4,pontobala6)

        for i in range(8):
                colisao_tiro(lst2[i],bala7,pontotank4,pontobala7)

        ###########################################################

        for i in range(8):
                colisao_tiro2(lst[i],bala_0,pontoaliado,pontobala_0)

        for i in range(8):
                colisao_tiro2(lst[i],bala1_1,pontoaliado,pontobala1_1)

        for i in range(8):
                colisao_tiro2(lst[i],bala2_2,pontoaliado,pontobala2_2)

        for i in range(8):
                colisao_tiro2(lst[i],bala3_3,pontoaliado,pontobala3_3)

        for i in range(8):
                colisao_tiro2(lst[i],bala4_4,pontoaliado,pontobala4_4)

        for i in range(8):
                colisao_tiro2(lst[i],bala5_5,pontoaliado,pontobala5_5)

        for i in range(8):
                colisao_tiro2(lst[i],bala6_6,pontoaliado,pontobala6_6)

        for i in range(8):
                colisao_tiro2(lst[i],bala7_7,pontoaliado,pontobala7_7)







            

    




        
        







  

        
        #Este comando faz a janela ser atualizada a cada frame
        win.update()
        #Este comando faz com que o framerate fique sempre abaixo de 60fps
        time.sleep(framerate)

Main("Super Tanks", 832, 440)