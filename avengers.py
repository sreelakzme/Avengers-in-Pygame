import pygame
import random
from pygame.locals import *
import time

#change background
def changeBackground(img):
    # Change the background 
    background = pygame.image.load(img)
    #set its size
    bg = pygame.transform.scale(background, (screen_width,screen_height))
    screen.blit(bg,(0,0))
    
 

# Initialize Pygame
pygame.init()
pygame.display.set_caption('Grab the stones')
# Set the height and width of the screen
screen_width=900
screen_height=700
screen = pygame.display.set_mode([screen_width,screen_height])

#Glove sprite
class Thanos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('glove.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,70))
        self.rect = self.image.get_rect()

#Stone sprite
class Stone(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('stone.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (20,30))
        self.rect = self.image.get_rect()

#Avenger sprite
class Avenger(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()

#List of images for Avenger class
images=["mask.png","shield.png","hammer.png"]
bImages=["b1.jpg","b2.jpg","b3.png","b4.jpg","b5.jpg"]
  

#create sprite groups
stone_list = pygame.sprite.Group()
allsprites= pygame.sprite.Group()
avenger_list=pygame.sprite.Group()

#create stone sprites
for i in range(100):
    stone = Stone() 
    # Set a random location for the stone
    stone.rect.x = random.randrange(screen_width)
    stone.rect.y = random.randrange(screen_height)
    # Add to stone list
    stone_list.add(stone)
    allsprites.add(stone)

#create avenger
for i in range(20):
    avenger=Avenger(random.choice(images))
    # Set a random location for the avenger
    avenger.rect.x = random.randrange(screen_width)
    avenger.rect.y = random.randrange(screen_height)
    # Add to avenger list
    avenger_list.add(avenger)
    allsprites.add(avenger)
    
    
 
# Create thanos
thanos = Thanos()
allsprites.add(thanos)

#initialize essential variables
# Define colour
WHITE = (255, 255, 255)
RED=(255,0,0)

playing=True
score = 0
#clock 
clock = pygame.time.Clock()
#start time
start_time = time.time()
#font to print score on screen 
myFont=pygame.font.SysFont("Times New Roman",40)
timingFont=pygame.font.SysFont("Times New Roman",70)
text=myFont.render("Score ="+str(0),True,WHITE)


# -------- Main Program Loop -----------
while playing:
    #refresh 60 times in a second
    #can be used to control speed
    clock.tick(30)
        
    #quit the game
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            playing=False
    
    #check if time>30 secs
    timeElapsed=time.time()-start_time
    if timeElapsed >=30:        
        if score>60:
            text=myFont.render("    Avengers...Try Again    ",True,WHITE)
            # Change the background 
            changeBackground("ThanosWins.jpg")
        else:
            text=myFont.render("Thanos..better luck next time",True,WHITE)
            # Change the background 
            changeBackground("b1.jpg")
        screen.blit(text,(230,40))        
    else:
               
        # Change the background 
        changeBackground(random.choice(bImages))
        countDown=timingFont.render(str(30-int(timeElapsed)),True,RED)
        screen.blit(countDown,(800,10))
        
        
        #move the glove as per key pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]: # UP
            if thanos.rect.y> 0:     
                 thanos.rect.y -= 5
        if keys[pygame.K_DOWN] : # DOWN
            if thanos.rect.y <630:
                thanos.rect.y += 5 
        
        if keys[pygame.K_LEFT] : # LEFT
            if thanos.rect.x> 0:    
                 thanos.rect.x -= 5 
        
        if keys[pygame.K_RIGHT] : # RIGHT
             if thanos.rect.x <850:
                 thanos.rect.x += 5  
         
        
     
        # See if stone and glove has collided
        stone_hit_list = pygame.sprite.spritecollide(thanos, stone_list, True)
        avenger_hit_list=pygame.sprite.spritecollide(thanos, avenger_list, True)
     
        # Check the list of collisions.
        for stone in stone_hit_list:
            score += 1
            #print(score)
            text=myFont.render("Score ="+str(score),True,WHITE)
        for avenger in avenger_hit_list:
            score -= 5
            #print(score)
            text=myFont.render("Score ="+str(score),True,WHITE)

        # print the score on screen
        screen.blit(text,(730,80))

             
        # Draw all the spites
        allsprites.draw(screen)
     
        
    pygame.display.update()
     
        
pygame.quit()
