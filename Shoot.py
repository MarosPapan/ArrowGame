import pygame
import random
import timer3
pygame.init()

timer = timer3.Timer()
win_x = 1366
win_y = 768
win = pygame.display.set_mode((win_x,win_y)) 
pygame.display.set_caption("Archer vs Archer")
#win.fill((100,100,100))

walk_left = [pygame.image.load("L1.png"),pygame.image.load("L2.png"),
             pygame.image.load("L3.png"),pygame.image.load("L4.png"),
             pygame.image.load("L5.png"),pygame.image.load("L6.png"),
             pygame.image.load("L7.png"),pygame.image.load("L8.png")]
walk_right = [pygame.image.load("R1.png"),pygame.image.load("R2.png"),
              pygame.image.load("R3.png"),pygame.image.load("R4.png"),
              pygame.image.load("R5.png"),pygame.image.load("R6.png"),
              pygame.image.load("R7.png"),pygame.image.load("R8.png")]
shoot_left = [pygame.image.load("AL2.png"),pygame.image.load("AL3.png")]
shoot_right = [pygame.image.load("AR2.png"),pygame.image.load("AR3.png")]
right_arrow = pygame.image.load("Arrow.png")
left_arrow = pygame.image.load("Arrow_L.png")
bg = pygame.image.load("bg.jpg")

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False 
        self.right = False
        self.jump = False
        self.jumpCount = 10 
        self.walkCount = 0
        self.stand = True
        self.shooting = False
        self.walking = False
        self.shootCount = 0
        self.facing = 0
        self.hitbox = (self.x+17,self.y+11,29,52)
        self.platform = False
        self.visible = True
        self.shoot = False
    def draw(self,win):
        if self.visible:
            if self.walking:
                if self.walkCount + 1 >= 24:
                    self.walkCount = 0
                if not(self.stand):
                    if self.left:
                        win.blit(walk_left[self.walkCount//3],(self.x,self.y))
                        self.walkCount += 1
                    if self.right:
                        win.blit(walk_right[self.walkCount//3],(self.x,self.y)) 
                        self.walkCount += 1
                if self.stand == True:
                    if self.right:
                        win.blit(walk_right[0], (self.x,self.y))
                    else:
                        win.blit(walk_left[0], (self.x,self.y))
            else:
                if self.right:
                    win.blit(walk_right[0], (self.x,self.y))
                if self.left:
                    win.blit(walk_left[0], (self.x,self.y))
            
        if self.shooting and self.stand:
            if self.shoot == False:
                if keys[pygame.K_SPACE]:
                    self.shoot = True
                    if self.facing == -1:
                        win.blit(shoot_left[0],(self.x,self.y))
                    if self.facing == 1:
                        win.blit(shoot_right[0],(self.x,self.y))

class projectile(object):
    def __init__(self,x,y,width,height,facing):
        self.x = x
        self.y = y             
        self.width = width 
        self.height = height                 
        self.facing = facing
        self.vel = 8 * facing
    def draw(self, win):
        if self.facing == 1:
            self.facing = 1
            win.blit(right_arrow,(self.x,self.y))
        elif self.facing == -1:
            self.facing = -1
            win.blit(left_arrow,(self.x,self.y))
      
def redrawWin():
    win.blit(bg,(0,0))
    man.draw(win)
    for bullet in m_bullets:
        bullet.draw(win)
    pygame.display.update()
    

#mainloop
man = player(128,768-128,64,64)
m_bullets = []

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(24)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in m_bullets:
        if bullet.x < win_x and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            m_bullets.pop(m_bullets.index(bullet))
        
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]: #and shootLoop == 0:    
        man.shooting = True
        man.stand = True
        man.inTension = True
        man.visible = False
        man.shoot_s += 1
        redrawWin()
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(m_bullets) < 20:
            #if shoot_right[0] or shoot_left[0]:
            if man.shoot_s == 2: 
                m_bullets.append(projectile(round(man.x+man.width//15),
                                            round(man.y+man.height//13),64,64,facing))
            #def fire():
            #    m_bullets.append(projectile(round(man.x+man.width//15),
            #                                round(man.y+man.height//13),64,64,facing))
            #timer.apply_after(800,fire)
    else:
        man.shooting = False
        man.shoot_s = 1
    if keys[pygame.K_LEFT] and man.x > 0:
        man.visible = True
        man.walking = True
        man.facing = -1
        man.x -= man.vel
        man.left = True
        man.right = False
        man.stand = False
        man.shooting = False
    if keys[pygame.K_RIGHT] and man.x < win_x-128:
        man.visible = True
        man.walking = True
        man.facing = 1
        man.x += man.vel
        man.left = False
        man.right = True
        man.shooting = False
        man.stand = False
    if not(keys[pygame.K_SPACE]) and not(keys[pygame.K_LEFT]) and not(keys[pygame.K_RIGHT]):
        man.visible = True
        man.stand = True
        man.walking = False
        man.shooting = False
        man.walkCount = 0
    redrawWin()


pygame.quit()

