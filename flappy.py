import pygame
import time
import random
from random import randint
pygame.init()

width=800
height=600

black = (0,0,0)
white = (255,255,255)
blue = (0,255,0)
green=(0,255,0)
red =(255,0,0)
bright_green=(0,200,0)
bright_red =(200,0,0)
space=160
x=(width *0.45)
y=(height *0.8)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Flappy bird v2.0")
clock = pygame.time.Clock()


def things_count(count,color):
    font=pygame.font.SysFont("comicsansms",25)
    pygame.draw.rect(screen,color,[30,30,60,50])
    SmallText=pygame.font.SysFont("comicsansms",50)
    TextSurf, TextRect=text_objects(str(count),SmallText,black)
    TextRect.center=(60,55)
    screen.blit(TextSurf, TextRect)


def obstacle(xloc,yloc,xsize,ysize):
    pygame.draw.rect(screen,green,[xloc,0,xsize,ysize])
    pygame.draw.rect(screen,green,[xloc,ysize+space,xsize,600])

def ball(x,y):
    pygame.draw.circle(screen,black,[x,y],20)
    
def text_objects(text,font,color):
    textSurface=font.render(text,True,color)
    return textSurface,textSurface.get_rect()
    
def message_display(text,color):
    largeText=pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect=text_objects(text,largeText,color)
    TextRect.center=((width/2),(height/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop(x,y)

    
def gameover():
    message_display('Game over',red)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] >x and y+h > mouse[1] >y:
        pygame.draw.rect(screen,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action(width *0.45,height *0.8)
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))

    SmallText=pygame.font.SysFont("comicsansms",30)
    TextSurf, TextRect=text_objects(msg,SmallText,black)
    TextRect.center=((x+(w/2)),(y+(h/2)))
    screen.blit(TextSurf, TextRect)

def quitgame(x,y):
    pygame.quit()
    quit()
    
def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Flappy bird v2.0",largeText,black)
        TextRect.center  =  ((width/2),(height/2-150))
        screen.blit(TextSurf, TextRect)
        button("Play!!",150,350,100,50,green,bright_green,game_loop)
        button("Quit",550,350,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
def game_loop(x,y):
    crashed=False
    x=300
    y=300
    x_speed=0
    y_speed=0
    ground=580
    xloc1=800
    yloc=0
    xsize=70
    ysize1=randint(70,350)
    xloc2=1300
    ysize2=randint(70,350)
    space=160
    obspeed=2.5
    dodged=0
    while not crashed:
        

        for event in pygame.event.get():
            
                if event.type==pygame.QUIT:
                    crashed =True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        y_speed=-8

                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_UP:
                        y_speed=4

        
        screen.fill(white)
        obstacle(xloc1,yloc,xsize,ysize1)
        obstacle(xloc2,yloc,xsize,ysize2)
        things_count(dodged,bright_green)
        
        ball(x,y)
        y+=y_speed
        xloc1-=obspeed
        xloc2-=obspeed

        if y>ground:
            things_count(dodged,bright_red)
            gameover()
            y_speed=0

        if x+20>xloc1 and y-20<ysize1 and x-15<xsize+xloc1:
            things_count(dodged,bright_red)
            gameover()
            obspeed=0
            y_speed=0

        if x+20>xloc1 and y+20>ysize1+space and x-15<xsize+ xloc1:
            things_count(dodged,bright_red)
            gameover()
            obspeed=0
            y_speed=0
        
        if xloc1<-80:
            xloc1=xloc2
            ysize1=ysize2
            xloc2=850
            ysize2=randint(70,350)
            

        if x>xloc1+xsize and x<xloc1+xsize+3:
            dodged+=1
        
        
        pygame.display.flip()
        clock.tick(60)


game_intro()
game_loop(x,y)
pygame.quit()
quit()
