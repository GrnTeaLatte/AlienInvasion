import sys

import pygame
from pygame.sprite import Group

from raindrop_settings import Settings
import sys

import pygame
from pygame.sprite import Group

from raindrop_settings import Settings

import raindrop_game_functions as gf


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Raindrops Falling")

    # Make a ship, a group of bullets, and a group of aliens.
    raindrops = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, raindrops)

    # Start the main loop for the game.
    while True:
        gf.update_raindrops(ai_settings, screen, raindrops)
        gf.update_screen(ai_settings, screen, raindrops)


run_game() 
import raindrop_game_functions as gf


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Raindrops Falling")

    # Make a ship, a group of bullets, and a group of aliens.
    raindrops = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, raindrops)

    # Start the main loop for the game.
    while True:
        gf.update_raindrops(ai_settings, screen, raindrops)
        gf.update_screen(ai_settings, screen, raindrops)


run_game() 