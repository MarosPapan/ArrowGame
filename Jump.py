import pygame
import timer3
pygame.init()

win = pygame.display.set_mode((500,500))

x = 128
y = 375
width = 64
height = 64
vel = 8
jump = False
jumpCount = 10
p_x = 200
p_y = 290
p_end = 400
p_ye = 290

run = True
clock = pygame.time.Clock()
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0 :
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += vel
    if not(jump):
        if keys[pygame.K_UP]:
            jump = True
            
    else:   
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -=(jumpCount ** 2) *0.5*neg
            jumpCount -= 1   
            if y >= p_y and x+32 >= p_x and x <= p_end-32:
                y = p_y - 64
                jumpCount = 0
                #if jump == True:
                #    if keys[pygame.K_UP]:
                #        jump = True
                #else:
                #    if jumpCount >= -10:
                #        neg = 1
                #        if jumpCount < 0:
                #            neg = -1
                #        y -=(jumpCount ** 2) //0.70*neg
                #        jumpCount -= 1

                            
            #y -=(jumpCount ** 2) *0.5*neg
            #jumpCount -= 1   
        else:
            jump = False
            jumpCount = 10
        
    win.fill((255,255,255))
    pygame.draw.rect(win,(100,100,255),(x,y,width,height))
    pygame.draw.line(win,(255,200,150),(p_x,p_y),(p_end,p_ye))
    pygame.display.update()

pygame.quit()
