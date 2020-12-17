import pygame

pygame.init()

win = pygame.display.set_mode((500,500))
win.fill((0,0,250))

class platforms(object):
    def __init__(self,x,y,ex,ey,color):
        self.x = x
        self.y = y
        self.ex = ex
        self.ey = ey
        self.color = color
    def draw(self,win):
        pygame.draw.lines(win,(self.color),[(self.x,self.y),(self.x+30,self.y+15)]
                          [self.ex)

def redraw():
    win.fill((0,0,250))
    plat_s.draw(win)
    pygame.display.update

plat_s = platforms(10,350,80,350,(255,0,0))
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()




    redraw()

#pygame.quit()
