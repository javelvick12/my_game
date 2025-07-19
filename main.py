import pygame as pg 
from sys import exit
import os

class Character:
    def __init__(self, character):
        character.color = "red"
        character.size = "regular"
        character.speed = "fast"



def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    #Screen Parameters
    SCREEN_WIDTH = 800 
    SCREEN_HEIGHT = 600
    pg.init()
    run = True
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption('Color Man')
    clock = pg.time.Clock()
    my_font = pg.font.Font(os.path.join(current_dir, 'assets/Minecraft.ttf'), 48)
    sky_image = pg.image.load('assets/sky.jpg').convert()
    ground_image = pg.image.load('assets/ground.jpg').convert()
    sky_height = SCREEN_HEIGHT * 3 // 4
    sky_scaled = pg.transform.scale(sky_image, (SCREEN_WIDTH, sky_height))
    ground_height = SCREEN_HEIGHT - sky_height
    ground_scaled = pg.transform.scale(ground_image, (SCREEN_WIDTH, ground_height))
    title_object = my_font.render('Color Man!', False, 'Orange')
    start_object = my_font.render('Start', False, 'Orange')
    options_object  = my_font.render('Options', False, 'Orange')
    exit_object = my_font.render('Exit', False, 'Orange')
    snail_object = pg.image.load(os.path.join(current_dir, 'assets/snail/snail1.png')).convert_alpha() #snail frame 1
    snail_move = pg.image.load(os.path.join(current_dir, 'assets/snail/snail2.png')).convert_alpha() #snail frame 2
    player_surface = pg.image.load(os.path.join(current_dir, 'assets/player/player_walk_1.png')).convert_alpha()
    player_rect = player_surface.get_rect(midbottom = (100, sky_height)) #get rekt
    snail_rect = snail_object.get_rect(midbottom = (600, sky_height))  #get rekt
    #snail_rect2 = snail_move.get_rect(midbottom = (600, sky_height))
    #The main run loop for the game
    while run:
        pg.display.update()
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        screen.blit(sky_scaled,(0,0))
        screen.blit(ground_scaled,(0,sky_height))
        screen.blit(title_object,(275, 50))
        screen.blit(start_object, (275, 100))
        snail_rect.x -= 1
        if snail_rect.left <= -90:
            snail_rect.x = 750
        if snail_rect.x % 50 == 0:
            screen.blit(snail_object, snail_rect)
        else:
            screen.blit(snail_move, snail_rect)
        screen.blit(player_surface, player_rect)
    pg.quit()
    exit()











if __name__ == "__main__":
    main()