import sys

import pygame
from pygame.sprite import Group

from settings import Settings

import star_game_functions as gf


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Star Invasion")

    stars = Group()

    # Create the fleet of aliens.
    gf.create_stars(ai_settings, screen, stars)

    # Start the main loop for the game.
    while True:
        gf.update_screen(ai_settings, screen, stars)


run_game() 