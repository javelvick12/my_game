import pygame as pg 
from sys import exit
import os

class Character:
    def __init__(self):
        character.color = "red"
        character.size = "regular"
        character.speed = "fast"



def main():
    #Screen Parameters
    SCREEN_WIDTH = 800 
    SCREEN_HEIGHT = 600
    pg.init()
    run = True
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption('Color Man')
    clock = pg.time.Clock()
    my_font = pg.font.Font('assets/Minecraft.ttf', 48)
    sky_image = pg.image.load('assets/sky.jpg')
    ground_image = pg.image.load('assets/ground.jpg')
    sky_height = SCREEN_HEIGHT * 3 // 4
    sky_scaled = pg.transform.scale(sky_image, (SCREEN_WIDTH, sky_height))
    ground_height = SCREEN_HEIGHT - sky_height
    ground_scaled = pg.transform.scale(ground_image, (SCREEN_WIDTH, ground_height))
    title_object = my_font.render('Color Man!', False, 'Orange')
    start_object = my_font.render('Start', False, 'Orange')
    options_object  = my_font.render('Options', False, 'Orange')
    exit_object = my_font.render('Exit', False, 'Orange')
    snail_object = pg.image.load('Documents/python_games/my_game/assets/snail/snail1.png')
    snail_move = pg.image.load('Documents/python_games/my_game/')
    snail_x_pos = 600
    #test_surface.fill('Red')
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
        if snail_x_pos <= -90:
            snail_x_pos = 765
        snail_x_pos -= 1
        screen.blit(snail_object, (snail_x_pos, 420))
    pg.quit()
    exit()











if __name__ == "__main__":
    main()