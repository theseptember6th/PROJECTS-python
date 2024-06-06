"""
AUTHOR:KRISTAL SHRESTHA
DATE:6/6/2024
PURPOSE:DEMO FLAPPYBIRD
"""


import random

import sys
#general basic pygame imports
import pygame
from pygame.locals import * 

#GLOBAL VARIABLES FOR THE Gpng
FPS=32
SCREENWIDTH=289
SCREENHEIGHT=511
SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
#initializes a window or screen for display


GROUNDY=SCREENHEIGHT*0.8  #for ground to be bottom ,you know how graphics coordinates work right

GAME_SPRITES={}  #Game images
GAME_SOUNDS={}
PLAYER=r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 2\images\bird.png'
BACKGROUND=r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 2\images\bg.png'
PIPE=r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 2\images\pipe.png'

def welcomeScreen():
    """shows welcome images on the screen"""
    #trying to centralize bird in y axis but keeping left in x axis
    playerx=int(SCREENWIDTH/5) #birdx coordinate
    playery=int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2) #birdy coordinate , Remember we can get height from the images directly due to pygame

    #trying to centralize message in x axis and just kinda top in y axis
    messagex=int((SCREENWIDTH-GAME_SPRITES['message'].get_width())/2) #message x coordinate
    messagey=int(SCREENHEIGHT*0.13)
    #message y coordinate

    #for base ,base will be from left to right taking full width in x axis
    basex=0
   
    while True: #important part
        '''The list of Event objects returned from pygame. event. get() will be in the order that the events happened. If the user clicked the mouse and then pressed a keyboard key, the Event object for the mouse click would be the first item in the list and the Event object for the keyboard press would be second.'''
        for event in pygame.event.get(): #core core part for welcome screen

            #if user clicks cross button X ,close the game
                                            
            if event.type==QUIT or(event.type==KEYDOWN and event.key==K_ESCAPE):#if key is pressed and that key is escape key
                pygame.quit()
                sys.exit()

            #if the user presses space or up key,start the game for them
            elif event.type==KEYDOWN and(event.key==K_SPACE or event.key==K_UP):
                return #returns to main function and starts main function
            
            else: #if neither of them are done,just blit the images again and again
                SCREEN.blit(GAME_SPRITES['background'],(0,0))
                SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))
                SCREEN.blit(GAME_SPRITES['message'],(messagex,messagey))
                SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))

                #without pygame.display.update() screen wont change
                pygame.display.update()#so it is important

                #to control FPS
                FPSCLOCK.tick(FPS)
                #By calling Clock.tick(40) once per frame, the program will never run at more than 40 frames per second
                #tick ensures it will never run more than 40fps

def mainGame():
    #after welcome screen
    score=0 #scores to count
    #trying to centralize bird in y axis but keeping left in x axis
    playerx=int(SCREENWIDTH/5) #birdx coordinate
    playery=int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2) #birdy coordinate
    basex=0

    #create 2 pipes for blitting on the screen by calling my userdefined getRandomPipe function

    newPipe1=getRandomPipe() #gets list of dictionary containing x,y coordinates of both upper and lower pipes
    newPipe2=getRandomPipe()
    #what i want to do is i want to generate two both upperandlower pipes in screen while playing
    #my list of upper pipes
    upperPipes=[                 #upperpipe's y
        {'x':SCREENWIDTH+200,'y':newPipe1[0]['y']},
        {'x':SCREENWIDTH+200+SCREENWIDTH/2,'y':newPipe2[0]['y']}
    ]
    #my list of lower pipes
    lowerPipes=[                 #upperpipe's y
        {'x':SCREENWIDTH+200,'y':newPipe1[1]['y']},
        {'x':SCREENWIDTH+200+SCREENWIDTH/2,'y':newPipe2[1]['y']}
    ]
    #moving pipe towards left
    pipeVelX=-4
    
    #note that player is not moving in x dirn but since pipe is moving towards left ,it feels illusion that player/bird is moving

    playerVelY=-9  #player falling down
    playerMaxVelY=10
    playerMinVelY=-8
    playerAccY=1

    #when bird/player is flapping,we want to change the velocity of the bird/player
    playerFlapAccv=-8
    playerFlapped=False #it will be true when bird is flapping

    #now i will run the main game loop
    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type==KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                if playery >0 : #if my player is in the screen
                    playerVelY=playerFlapAccv
                    playerFlapped=True
                GAME_SOUNDS['wing'].play()

        #now we will check if there is crash or not using isCollide function
        #isCollide function will return true if you crashed
        crashTest=isCollide(playerx,playery,upperPipes,lowerPipes)
        if crashTest:
            return  
        #check for score
        playerMidpos=playerx+GAME_SPRITES['player'].get_width()/2
        #dont get confused player is not moving,we are just determining the checkpoint(playerMidpos) such that the pipe which is moving if crossed that checkpoint will get you points
        #if my pipe cross the playerMidpos then we will get points 

        for pipe in upperPipes:
            pipeMidpos=pipe['x']+GAME_SPRITES['pipe'][0].get_width()/2
            if pipeMidpos <= playerMidpos < pipeMidpos+4:
                score+=1
                print(f"your score is {score}")
                GAME_SOUNDS['point'].play()

        #for movement of players    
        #if playervely is less than playermaxy and player is not flapping
        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY+=playerAccY #so he will start to fall
        
        #if player was flapping
        if playerFlapped:
            playerFlapped =False

        #now we want player y to not go below the base for this we do following things
        playerHeight=GAME_SPRITES['player'].get_height()
        playery=playery+ min(playerVelY,GROUNDY-playery-playerHeight)


        #now for the pipes to move left
        for upperPipe,lowerPipe in zip(upperPipes,lowerPipes):
            upperPipe['x']+=pipeVelX
            lowerPipe['x']+=pipeVelX


    
        #Add a new pipe when the first is about to cross the leftmost part of the screen

        if 0 < upperPipes[0]['x']<5: #almost if pipe is going out
            newpipe=getRandomPipe() #get a new pipes(lower&upper)
            upperPipes.append(newpipe[0]) #and add upperpipe to the upperpipes
            lowerPipes.append(newpipe[1])#and add lowerpipe to lowerpipes
        
        #if the pipe is out of screen,remove it
        if upperPipes[0]['x'] <- GAME_SPRITES['pipe'][0].get_width():
            #if my pipe gets to -width of its own in x direction from screen then we wil remove it
            upperPipes.pop(0) #remove current first upper pipe
            lowerPipes.pop(0) #remove current first lower pipe
            #since both are in moving similarly in x so we pop both
        

        #lets blit our sprites now,we are displaying images on screen

        SCREEN.blit(GAME_SPRITES['background'],(0,0))
        for upperPipe,lowerPipe in zip(upperPipes,lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0],(upperPipe['x'],upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1],(lowerPipe['x'],lowerPipe['y']))
            
        SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))

        #for blitting scores

        myDigits=[int(x) for x in list(str(score))]
        width=0
        for digit in myDigits:
            width+=GAME_SPRITES['numbers'][digit].get_width()
        Xoffset=(SCREENWIDTH-width)/2 #to centralize digits

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit],(Xoffset,SCREENHEIGHT*0.12))
            Xoffset+=GAME_SPRITES['numbers'][digit].get_width()

        pygame.display.update()
        FPSCLOCK.tick(FPS)   

        
        
def isCollide(playerx,playery,upperPipes,lowerPipes):
    if playery >GROUNDY or playery < 0: #if it hits top or ceiling
        GAME_SOUNDS['hit'].play()
        return True
    
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUNDS['hit'].play()
            return True
    
    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
            GAME_SOUNDS['hit'].play()
            return True

    return False
        




def getRandomPipe():
    """
    generating positions of upper and lower pipes for blitting on the screen
    """
    #setting pipe height as its original image height
    pipeHeight=GAME_SPRITES['pipe'][0].get_height()
    #for offset ,assuming as screensheight/3 so that there will be gaps
    offset=SCREENHEIGHT/3
    #here y2 represents lowerpipe's y coordinates
    #we will change y2 and then its effect will change y coordinate of upper
    y2=offset+random.randrange(0,int(SCREENHEIGHT-GAME_SPRITES['base'].get_height()-1.2*offset))#on solving you will get that maxm random value as 0.6SH-B that is nearly 0.3SH
    #so y2's maximum value will be 0.6SH
    #pipe X logic is simple,you just want it to be outside the screen by 10
    pipeX=SCREENWIDTH+10
    #if i wrote only pipeheight-y2 there will be no gap in pipes to play
    y1=pipeHeight-y2+offset

    #creating a list of dictionary to help choosing x and y coordinates of upper and lower pipe
    pipe=[  
        {'x':pipeX,'y':-y1}, #upper pipe
        {'x':pipeX,'y':y2} #lower pipe
        
    ]
    return pipe




if __name__ == "__main__":
    pygame.init() #initializes all pygame modules

    FPSCLOCK=pygame.time.Clock() #to control fps of the game
    #pygame.time.Clock() creates an object to help time

    pygame.display.set_caption("FLAPPY BIRD BY KRISTAL")#caption

    GAME_SPRITES['numbers']= (
        pygame.image.load(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 2\images\0.png').convert_alpha(),
        pygame.image.load(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 2\images\1.png').convert_alpha(),
        pygame.image.load(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 2\images\2.png').convert_alpha(),
        pygame.image.load(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 2\images\3.png').convert_alpha(),
        pygame.image.load(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 2\images\4.png').convert_alpha(),
        pygame.image.load(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 2\images\5.png').convert_alpha(),
        pygame.image.load(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 2\images\6.png').convert_alpha(),
        pygame.image.load(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 2\images\7.png').convert_alpha(),
        pygame.image.load(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 2\images\8.png').convert_alpha(),
        pygame.image.load(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 2\images\9.png').convert_alpha(),
    )

    GAME_SPRITES['background']=pygame.image.load(BACKGROUND).convert()
    #for quick blitting
    #Pygame blit() The Pygame blit() method is one of the methods to place an image onto the screens of pygame applications. It intends to put an image on the screen. It just copies the pixels of an image from one surface to another surface just like that
    GAME_SPRITES['player']=pygame.image.load(PLAYER).convert_alpha()
    # blitting + transparent effect so little slower than convert()
    GAME_SPRITES['message']=pygame.image.load(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 2\images\message.png').convert_alpha()
    GAME_SPRITES['base']=pygame.image.load(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 2\images\base.png').convert_alpha()
    #needs two pipe,one top pipe and another bottom pipe
    GAME_SPRITES['pipe']=(
        pygame.image.load(PIPE).convert_alpha(),
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180)
    )

    #GAME SOUNDS
    GAME_SOUNDS['die']=pygame.mixer.Sound(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 2\sounds\die.wav')
    GAME_SOUNDS['point']=pygame.mixer.Sound(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 2\sounds\point.wav')
    GAME_SOUNDS['wing']=pygame.mixer.Sound(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 2\sounds\wing.wav')
    GAME_SOUNDS['hit']=pygame.mixer.Sound(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 2\sounds\hit.wav')
    GAME_SOUNDS['swoosh']=pygame.mixer.Sound(r'C:\Users\Kristal\Desktop\PROJECTS-python\PROJECT 2\sounds\swoosh.wav')
    #the sound of a bird flying past  can be described as a "swoosh".



    while True:
        welcomeScreen() #shows welcome screen to the user until user presses any key
        mainGame() #this is the main game function