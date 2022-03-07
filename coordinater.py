#how to find certain positions on a window in pygame
#By vivid acorn
#language = python

import pygame


pygame.font.init() 
myFont = pygame.font.SysFont(None, 24)

coordinate_history = []

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#ignore:
'''
try:
    file1 = open("myfile.txt","w")
    file1.writelines(mx)
except:
    print('Data transfer failed.')
    mfdecode = False
'''

pygame.init()
 
size = (1450,1002)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Window")
 
done = False
clock = pygame.time.Clock()

def txt():
    dis = myFont.render(str(pos), 1, BLACK)
    #img = font.render(str(mx,my), True, (0,0,0))
    screen.blit(dis, (20, 20))
 
while not done:

    mx,my = pygame.mouse.get_pos()
    mx = pygame.mouse.get_pos()
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            print(mx, my)
            pos = mx, my
            txt()
            mfdecode = True

    pos = mx,my
    dis = myFont.render(str(pos), 1, BLACK)
    textencode = myFont.render('Click a position to save.', 1, BLACK)
    #img = font.render(str(mx,my), True, (0,0,0))
    screen.blit(dis, (20, 20))
    screen.blit(textencode, (20, 50))

    
 
    
    
 
  
    pygame.display.flip()
 
   
    clock.tick(60)

pygame.quit()
file1.close()
