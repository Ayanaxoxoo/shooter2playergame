import pygame
from time import*
from pygame.locals import*
pygame.font.init()
pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((800,600))

border=pygame.Rect(800//2,0,10,600)
background = pygame.transform.scale(pygame.image.load("img/galaxy2bg.png"),(800,600))
player1 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load ("img/shooter1.png"),(55,40)),(270))
player2 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load ("img/shooter2.png"),(55,40)),(90))
red_bullets = []
yellow_bullets = []
health_red = 5
health_yellow = 5
font = pygame.font.SysFont("Times New Roman",90)


playing=True
yellow = pygame.Rect(100,300,55,40)
red = pygame.Rect(600,300,55,40) 

def yellow_move(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x > 10:
        yellow.x=yellow.x-5
    if keys_pressed[pygame.K_d] and yellow.x < 350:
        yellow.x=yellow.x+5
    if keys_pressed[pygame.K_w] and yellow.y > 0:
        yellow.y=yellow.y-5
    if keys_pressed[pygame.K_s] and yellow.y < 550:
        yellow.y=yellow.y+5

def red_move(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x > 430:
        red.x=red.x-5
    if keys_pressed[pygame.K_RIGHT] and red.x < 750:
        red.x=red.x+5    
    if keys_pressed[pygame.K_UP] and red.y > 0 :
        red.y=red.y-5  
    if keys_pressed[pygame.K_DOWN] and red.y < 550 :
        red.y=red.y+5

def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    global health_red, health_yellow
    for y in yellow_bullets: 
        y.x+=5
        if y.colliderect(red):
            health_red-=1
            yellow_bullets.remove(y)
    for r in red_bullets: 
        r.x-=5    
        if r.colliderect(yellow ):
            health_yellow-=1
            red_bullets.remove(r)
            
            
    

while playing: 
    clock=pygame.time.Clock()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                bullet= pygame.Rect(yellow.x,yellow.y+28,10,5)
                yellow_bullets.append(bullet)
            if event.key==pygame.K_SPACE:
                bullet= pygame.Rect(red.x,red.y+28,10,5)
                red_bullets.append(bullet)
        
        if event.type == pygame.QUIT:
            playing = False
        
    screen.blit(background, (0,0))
    screen.blit(player1,(yellow.x,yellow.y))
    screen.blit(player2,(red.x,red.y))
    pygame.draw.rect(screen,"black",border)
    
    keys_pressed=pygame.key.get_pressed()
    yellow_move(keys_pressed,yellow)
    red_move(keys_pressed,red)

    handle_bullets(yellow_bullets,red_bullets,yellow,red)
    for bullet in yellow_bullets:
        pygame.draw.rect(screen,("yellow"),bullet)
    for bullet in red_bullets:
        pygame.draw.rect(screen,("red"),bullet)
    
    print(health_red)
    print(health_yellow)

    yellow_score = font.render("Yellow Health"+str(health_yellow),True,"white")
    red_score = font.render("Red Health"+str(health_red), True, "white")
    screen.blit(yellow_score,(50,50))
    screen.blit(red_score,(90,80))
    
    pygame.display.update()