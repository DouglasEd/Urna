import pygame
import sys
import Sheet
import time

pygame.init()
mat=""
state="Mat"
width= 1280
heigth= 720
res=(width,heigth)
clock= pygame.time.Clock()
screen= pygame.display.set_mode(res, pygame.FULLSCREEN)
smallfont= pygame.font.SysFont('arial Bold',50)
smalfont= pygame.font.SysFont('arial Bold',40)
font=pygame.font.SysFont('arial',25)
BigFont= pygame.font.SysFont('arial Bold',100)
text= smallfont.render("confirmar",True,(0,0,0))
text = ['1','2','3','4','5','6','7','8','9','del','0','<-']
pos = [[width/2+10,heigth*0.1], [width/2+150,heigth*0.1], [width/2+290,heigth*0.1],
        [width/2+10,heigth*0.1+140], [width/2+150,heigth*0.1+140], [width/2+290,heigth*0.1+140],
        [width/2+10,heigth*0.1+280], [width/2+150,heigth*0.1+280], [width/2+290,heigth*0.1+280],
        [width/2+10,heigth*0.1+420], [width/2+150,heigth*0.1+420], [width/2+290,heigth*0.1+420]]
teclado = [pygame.Rect(pos[0][0],pos[0][1],130,130),pygame.Rect(pos[1][0],pos[1][1],130,130),pygame.Rect(pos[2][0],pos[2][1],130,130),
            pygame.Rect(pos[3][0],pos[3][1],130,130),pygame.Rect(pos[4][0],pos[4][1],130,130),pygame.Rect(pos[5][0],pos[5][1],130,130),
            pygame.Rect(pos[6][0],pos[6][1],130,130),pygame.Rect(pos[7][0],pos[7][1],130,130),pygame.Rect(pos[8][0],pos[8][1],130,130),
            pygame.Rect(pos[9][0],pos[9][1],130,130),pygame.Rect(pos[10][0],pos[10][1],130,130),pygame.Rect(pos[11][0],pos[11][1],130,130)]

Val=[True,'']
VT=False
conf=False
confV=False
mouse = pygame.mouse.get_pos()
while True:
    screen.fill((60,25,60))
    mouse = pygame.mouse.get_pos()
    for ev in pygame.event.get():
        if state == 'Mat':
            if ev.type==pygame.QUIT:
                pygame.quit()
            if ev.type==pygame.MOUSEBUTTONUP:
                if pos[0][0]+130 >= mouse[0]>=pos[0][0] and pos[0][1]+130 >= mouse[1] >= pos[0][1]:
                    mat+='1'
                    conf=False
                elif pos[1][0]+130 >= mouse[0]>=pos[1][0] and pos[1][1]+130 >= mouse[1] >= pos[1][1]:
                    mat+='2'
                    conf=False
                elif pos[2][0]+130 >= mouse[0]>=pos[2][0] and pos[2][1]+130 >= mouse[1] >= pos[2][1]:
                    mat+='3'
                    conf=False
                elif pos[3][0]+130 >= mouse[0]>=pos[3][0] and pos[3][1]+130 >= mouse[1] >= pos[3][1]:
                    mat+='4'
                    conf=False
                elif pos[4][0]+130 >= mouse[0]>=pos[4][0] and pos[4][1]+130 >= mouse[1] >= pos[4][1]:
                    mat+='5'
                    conf=False
                elif pos[5][0]+130 >= mouse[0]>=pos[5][0] and pos[5][1]+130 >= mouse[1] >= pos[5][1]:
                    mat+='6'
                    conf=False
                elif pos[6][0]+130 >= mouse[0]>=pos[6][0] and pos[6][1]+130 >= mouse[1] >= pos[6][1]:
                    mat+='7'
                    conf=False
                elif pos[7][0]+130 >= mouse[0]>=pos[7][0] and pos[7][1]+130 >= mouse[1] >= pos[7][1]:
                    mat+='8'
                    conf=False
                elif pos[8][0]+130 >= mouse[0]>=pos[8][0] and pos[8][1]+130 >= mouse[1] >= pos[8][1]:
                    mat+='9'
                    conf=False
                elif pos[9][0]+130 >= mouse[0]>=pos[9][0] and pos[9][1]+130 >= mouse[1] >= pos[9][1]:
                    mat=""
                    conf=False
                elif pos[10][0]+130 >= mouse[0]>=pos[10][0] and pos[10][1]+130 >= mouse[1] >= pos[10][1]:
                    mat+='0'
                    conf=False
                elif pos[11][0]+130 >= mouse[0]>=pos[11][0] and pos[11][1]+130 >= mouse[1] >= pos[11][1]:
                    mat=mat[0:-1]
                    conf=False
                elif heigth*0.1+110 >= mouse[1]>= heigth*0.1+60 and 610 >= mouse[0] >= 10:
                    if mat=="03062003":
                        pygame.quit()
                        exit()
                    else:
                        Val=[False,'']
                        VT=True
                        Val=Sheet.AcessarMats(mat)
                        VT=Sheet.VerVotAnt(mat)
                        if Val[0] == True and VT == False:
                            conf=True
                if conf== True:
                    if heigth*0.1+210 >= mouse[1] >= heigth*0.1+160 and 210 >= mouse[0]>= 10:
                        state='Wait'
                print(mat,'-------')
                print(ev.type,'-------')
                mat=mat[0:12]
        #elif ev.type==pygame.MOUSEBUTTONUP:
         #   pass   
        if state == 'VotoC':
            if ev.type==pygame.MOUSEBUTTONUP:
                if confV == False:
                    if heigth/2+170 >= mouse[1] >= heigth/2-200 and 420 >= mouse[0]>= 50:
                        confV = True
                        voto="Chapa Turing"
                    if heigth/2+170 >= mouse[1] >= heigth/2-200 and width/2+185 >= mouse[0]>= width/2-185:
                        # width/2-185,heigth/2-200,370,370
                        confV = True
                        voto="Branco"
                    if heigth/2+170 >= mouse[1] >= heigth/2-200 and width/2+590 >= mouse[0]>= width/2+220:
                        # width/2+220,heigth/2-200,370,370
                        confV = True
                        voto=""
                if confV == True:
                    if heigth/2+300 >= mouse[1]>= heigth/2+150 and width/2-10 >= mouse[0] >= width/2-210:
                        Sheet.EnviarVoto(mat,voto)
                        Val=[True,'']
                        VT=False
                        conf=False
                        confV=False
                        mat=""
                        voto=None
                        state="Fim"

                    if heigth/2+300 >= mouse[1] >= heigth/2+150 and width/2+205 >= mouse[0]>= width/2+5:
                        confV = False
                    

                    
    if state == "Wait":
        screen.fill((60,25,60))
        pygame.display.flip()
        time.sleep(2)
        state = "VotoC"
    for i in range(0,12):
        pygame.draw.rect(screen,(255,255,255),teclado[i])
        texto=smallfont.render(text[i],True,(255,0,0))
        screen.blit(texto, (pos[i][0],pos[i][1]))
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(10,heigth*0.1,600,50))
    textent=smallfont.render(mat,True,(255,0,0))
    screen.blit(textent, (10,heigth*0.1))
    pygame.draw.rect(screen,(0,255,0), pygame.Rect(10,heigth*0.1+60,600,50))
    textconf=smallfont.render("confirmar",True,(255,255,255))
    screen.blit(textconf, (200,heigth*0.1+60))
    if Val[0] == False:
        Inv=smallfont.render("Matricula Invalida",True,(255,0,0))
        screen.blit(Inv,(10,heigth*0.1+110))
    elif VT == True:
        VotJR=smallfont.render("Voto Já Efetuado",True,(255,0,0))
        screen.blit(VotJR,(10,heigth*0.1+110))
    elif conf==True:
        name=font.render(f"Nome:{Val[1]}",True,(255,255,255))
        matr=font.render(f"Matricula:{mat}",True,(255,255,255))
        CN=smalfont.render(f"SOU EU",True,(255,255,255))
        screen.blit(name,(10,heigth*0.1+110))
        screen.blit(matr,(10,heigth*0.1+130))
        pygame.draw.rect(screen,(0,255,0), pygame.Rect(10,heigth*0.1+160,200,50))
        screen.blit(CN,(10,heigth*0.1+160))

    if state == 'VotoC':
        image = pygame.image.load("img/Turing.png")
        image = pygame.transform.scale(image,(370,370))
        screen.fill((100,100,100))
        screen.blit(image,(50,heigth/2-200))
        #chapC=smalfont.render(f'Chapa Cabelittle',True,(255,255,255))
        Branc=smalfont.render(f'BRANCO',True,(0,0,0))
        Nul=smalfont.render(f'NULO', True,(255,255,255))
        # pygame.draw.rect(screen,(38,13,38),pygame.Rect(50,heigth/2+10,370,160))
        #screen.blit(chapC,(100,heigth/2+50))
        pygame.draw.rect(screen,(255,255,255),pygame.Rect(width/2-185,heigth/2-200,370,370))
        screen.blit(Branc,(width/2-75,heigth/2-20))
        pygame.draw.rect(screen,(30,30,30),pygame.Rect(width/2+220,heigth/2-200,370,370))
        screen.blit(Nul,(width/2+350,heigth/2-20))
        if confV == True:
            pygame.draw.rect(screen,(255,255,255),pygame.Rect(10,10,width-20,heigth-20))
            pygame.draw.rect(screen,(0,255,0),pygame.Rect(width/2-210,heigth/2+150,200,150))
            pygame.draw.rect(screen,(255,0,0),pygame.Rect(width/2+5,heigth/2+150,200,150))
            confirm = smalfont.render('Confirmar',True,(255,255,255))
            screen.blit(confirm,(width/2-205,heigth/2+160))
            Cancel = smalfont.render('Cancelar',True,(255,255,255))
            screen.blit(Cancel,(width/2+10,heigth/2+160))
            Voto=BigFont.render(f'Voce quer Votar em {voto}?',True,(0,0,0))
            screen.blit(Voto,(20,20))
    if state == "Fim":
        screen.fill((255,255,255))
        Fim=BigFont.render('FIM',True,(0,0,0))
        screen.blit(Fim,(width/2-100,heigth/2-50))
        state="Mat"
        pygame.mixer.init()
        pygame.mixer.music.load("AudioUrna.mp3") 
        pygame.mixer.music.set_volume(0.7) 
        pygame.mixer.music.play() 
        pygame.display.flip()
        time.sleep(3)
    pygame.display.flip()

    clock.tick(60)
