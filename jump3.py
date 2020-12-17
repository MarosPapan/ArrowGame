from pygame. locals import *
import pygame
import math
from time import sleep
pygame.init()

win = pygame.display.set_mode((500,500))
win.fill((250,50,150))
class player(object):
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 5
        self.jump = False
        self.jumpcount = 0
    def draw(self,win):
        pygame.draw.rect(win,(self.color),(self.x,self.y,self.width,self.height))

class main_platform(object):
    def __init__(self,color,x,y,ex,ey):
        self.x = x
        self.y = y
        self.ex = ex
        self.ey = ey
        self.color = color
    def draw(self,win):
        pygame.draw.line(win,self.color,(self.x, self.y),(self.ex,self.ey))
        
class platform(object):
    def __init__(self,color,x,y,ex,ey):
        self.color = color
        self.x = x
        self.y = y
        self.ex = ex
        self.ey = ey
    def draw(self,win):
        pygame.draw.line(win,self.color,(self.x,self.y),(self.ex,self.ey))
def redraw():
    win.fill((250,50,150))
    main_p.draw(win)
    player.draw(win)
    plat_f.draw(win)
    pygame.display.update()
player = player(400,426,64,64,(0,50,250))
main_p = main_platform((250,0,0),0,490,500,490)
plat_f = platform((100,230,100),100,300,200,300)
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0 :
        player.x -= player.speed
    if keys[pygame.K_RIGHT] and player.x < 500 - player.width:
        player.x += player.speed
    if keys[pygame.K_UP] and player.y > 0:
        player.jump = True
        if player.y <= player.y + 80 and player.jumpcount <= 80:
            player.y -= 4
            player.jumpcount += 4
    
            
    redraw()
