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
        self.isjump = True
        self.v = 8
        self.m = 2
        self.gravity = False 
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
    def __init__(self,x,y,ex,ey,color):
        self.x = x
        self.y = y
        self.ex = ex
        self.ey = ey
        self.color = color
class platforms(object):
    def __init__(self):
        self.container = list([])
    def add(self, p):
        self.container.append(p)
    def collision(self, player, main_platform):
        for p in self.container:
            if player.y >= main_platform.y - 64:
                player.y = main_platform.y - 64
                player.isjump = False
                player.v = 8
            if player.y >= p.y and player.y <= p.y+40 and player.x+64 >= p.x and player.x <= p.ex+20:
                player.y = p.y-64
                player.isjump = False
                player.v = 8
    def gravity(self, player,main_platform):
        for p in self.container:
            if player.y >= main_platform.y-64:
                player.y = main_platform.y-64
            elif player.y >= p.y-64 and player.y < p.y+25 and player.x+64 > p.x and player.x < p.ex+20:
                player.y = p.y-64
            else:
                player.y += 4**2
        
        
    def draw(self,win):
        for p in self.container:
            pygame.draw.line(win,p.color,(p.x,p.y),(p.ex,p.ey),1) 
        
def redraw():
    win.fill((250,50,150))
    main_p.draw(win)
    player.draw(win)
    plat_f.draw(win)
    pygame.display.update()
platform_M = True
platform_S = False 
player = player(300,100,64,64,(0,50,250))
main_p = main_platform((250,0,0),0,490,500,490)
#plat_f = platform((100,230,100),100,300,200,300)
plat_f = platforms()
plat_f.add(platform(0,300,100,300,(100,230,100)))
plat_f.add(platform(400,300,500,300,(100,230,100)))
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
        
    if player.isjump == False:
        plat_f.gravity(player,main_p)
    if not(player.isjump):
        if keys[pygame.K_UP]:
            player.isjump = True
    else:
        player.isjump = 1
        if player.v > 0:
            F = ( 0.5 * player.m * (player.v*player.v))
        else:
            F = -( 0.5 * player.m * (player.v*player.v))

        player.y -= F
        player.v -= 1
        
        plat_f.collision(player,main_p)
                
            
            
    redraw()
    
