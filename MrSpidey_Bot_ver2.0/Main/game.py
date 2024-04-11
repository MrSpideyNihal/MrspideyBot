import pygame
import sys
import random
import pygame
import os
from define import *
pygame.init()
score = 0

font = pygame.font.Font('data\\font.ttf', 20)

damage_channel = pygame.mixer.Channel(1)
def display_score(s,window):
        score = int(s)
        score_text = font.render(f"Score: {s}", True, ORANGE)
        window.blit(score_text, (570, 10))
def Play_score(s):

    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.say(f"Your score is {s}")
    engine.runAndWait()


def Play_bg(music_file):
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
def Play_music(sound_file, channel):
    sound = pygame.mixer.Sound(sound_file)
    channel.play(sound)
def game(score):
    score =  score
    Play_bg(music)
    
    def show_hearts(heart):
         i = 1
         j = 10
         while i <= heart :
              Game_window.blit(hearts,(j, 5))
              i += 1
              j += 60
    def draw():
         
         pygame.draw.rect(Game_window,Black,(mxc,myc,25,25))
         pygame.draw.rect(Game_window,Black,(mxc1,myc1,25,25))
         pygame.draw.rect(Game_window,Black,(mxc2,myc2,25,25))
         pygame.draw.rect(Game_window,Black,(mxc3,myc3,25,25))
         pygame.draw.rect(Game_window,Black,(pc,py,72,100))
         Game_window.fill(BLUE)
         Game_window.blit(Player_Image, (px, py))
         Game_window.blit(metor_Image, (mx, my))
         Game_window.blit(metor_Image1, (mx1, my1))
         Game_window.blit(metor_Image2, (mx2, my2))
         Game_window.blit(metor_Image3, (mx3, my3))
         show_hearts(heart)
         display_score(int(score),Game_window)
         pygame.display.flip()
    running = False
    Game_window = pygame.display.set_mode((700, 500))
    game_run = True
    px = 300
    py = 400
    my = 10
    my1 = 3
    my2 = 6
    my3 = -10
    speed = 0.7
    font = font = pygame.font.Font(None, 36)
    mx = random.randint(130,250)
    mx1 = random.randint(150,350)
    mx2 = random.randint(350,450)
    mx3 = random.randint(3,100)
    pc = px + 14
    heart = 5
    mxc = mx + 17        
    myc = my + 40
    mxc1 = mx1 + 17
    myc1 = my1 + 37  
    mxc2 = mx2 + 17      
    myc2 = my2 + 37
    mxc3 = mx3 + 17
    myc3 = my3 + 37    
    
    
    while game_run:
       # Handle events
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               game_run = False
           elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    px = px - 50
                    if px <= -10:
                         px = px +50
                    draw()
                if event.key == pygame.K_RIGHT:
                    px = px + 50
                    if px >= 650:
                         px = px -50
                    draw()
        my = my + speed
        score = score + 0.001
        my1 = my1 + speed
        my2 = my2 + speed
        my3 = my3 + speed
        myc = myc + speed
        myc1 = myc1 + speed
        myc2 = myc2 + speed
        myc3 = myc3 + speed
        pc = (px+14)
        
        if my >= 430 :
             my = random.randint(0,10)
             mx = random.randint(3,270)
             mxc = mx + 17        
             myc = my + 37
        if my1 >= 430:
             mx1 = random.randint(290,450)
             my1 = random.randint(-10,10)
             mxc1 = mx1 + 17
             myc1 = my1 + 37
        if my2 >= 430:
             mx2 = random.randint(470,680)
             my2 = random.randint(-20,10)
             mxc2 = mx2 + 17
             myc2 = my2 + 37
        if my3 >= 430:
             mx3 = random.randint(1,100)
             my3 = random.randint(-20,10)
             mxc3 = mx3 + 17
             myc3 = my3 + 37
        player_rect = pygame.draw.rect(Game_window,Black,(pc,py,72,100))
        meteor_rect =  pygame.draw.rect(Game_window,Black,(mxc,myc,25,25))
        meteor_rect1 =  pygame.draw.rect(Game_window,Black,(mxc1,myc1,25,25))
        meteor_rect2 =  pygame.draw.rect(Game_window,Black,(mxc2,myc2,25,25))
        meteor_rect3 =  pygame.draw.rect(Game_window,Black,(mxc3,myc3,25,25))
        if player_rect.colliderect(meteor_rect) :
             my = random.randint(0,10)
             mx = random.randint(3,270)
             mxc = mx + 17        
             myc = my + 37
             heart = heart - 1
             Play_music(damage,damage_channel)
        elif player_rect.colliderect(meteor_rect1) :
             mx1 = random.randint(290,450)
             my1 = random.randint(-10,10)
             mxc1 = mx1 + 17
             myc1 = my1 + 37
             heart = heart - 1
             Play_music(damage,damage_channel)
            
        elif player_rect.colliderect(meteor_rect2) :
             mx2 = random.randint(470,680)
             my2 = random.randint(-20,10)
             mxc2 = mx2 + 17
             myc2 = my2 + 37
             heart = heart - 1
             Play_music(damage,damage_channel)

        elif player_rect.colliderect(meteor_rect3) :
             mx3 = random.randint(1,100)
             my3 = random.randint(-20,10)
             mxc3 = mx3 + 17
             myc3 = my3 + 37
             heart = heart - 1
             Play_music(damage,damage_channel)
        
        draw()
        if heart == 0:
             pygame.mixer.music.stop()
             pygame.mixer.quit()
             Play_score(int(score))
             main(score)
             pygame.quit()
             sys.exit()
        # Quit Pygame properly
    pygame.quit()
    sys.exit()
                       
def main(s):            
        
        width, height = 700, 500
        Menu_window = pygame.display.set_mode((width, height))
       
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # Check for mouse click on the image
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if image_play.collidepoint(mouse_pos):
                        print("Image clicked!")
                        running = game(s)
                    if image_exit.collidepoint(mouse_pos):
                        print("Image clicked!")
                        pygame.quit()
                        sys.exit()
                   
                   
            # Fill the window with a color (in this case, white)
            Menu_window.fill(BLUE)
            Menu_window.blit(Play_Image, (300, 150))
            Menu_window.blit(Exit_Image, (300, 250))
            display_score(int(s),Menu_window)
            
            pygame.display.flip()
       
        # Quit Pygame properly
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main(score)