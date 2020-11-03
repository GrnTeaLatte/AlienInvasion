import sys

import pygame

from raindrop import Raindrop


def update_screen(ai_settings, screen, raindrops):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and raindrops.
    raindrops.draw(screen)
    # Make the most recently drown screen visible.
    pygame.display.flip()

def get_number_raindrops_x(ai_settings, raindrop_width):
    """Determine the number of raindrops that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * raindrop_width
    number_raindrops_x = int(available_space_x / (2 * raindrop_width))
    return number_raindrops_x

def get_number_rows(ai_settings, raindrop_height):
    """Determine the number of rows of raindrops that fit on the screen."""
    available_space_y = (ai_settings.screen_height - (2 * raindrop_height))
    number_rows = int(available_space_y / (2 * raindrop_height))
    return number_rows

def create_raindrop(ai_settings, screen, raindrops, raindrop_number, row_number):
    """Create an raindrop and place it in the row."""
    raindrop = Raindrop(ai_settings, screen)
    raindrop_width = raindrop.rect.width
    raindrop_height = raindrop.rect.height
    
    raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
    raindrop.y = raindrop_height + 2 * raindrop_height * row_number
    
    raindrop.rect.x = raindrop.x
    raindrop.rect.y = raindrop.y
    raindrops.add(raindrop)

def create_fleet(ai_settings, screen, raindrops):
    """Create a full fleet of raindrops."""
    # Create an raindrop and find the number of raindrops in a row. 
    raindrop = Raindrop(ai_settings, screen)
    number_raindrops_x = get_number_raindrops_x(ai_settings, raindrop.rect.width)
    number_rows = get_number_rows(ai_settings, raindrop.rect.height)

    # Create the fleet of raindrops.
    for row_number in range(number_rows):
        for raindrop_number in range(number_raindrops_x):
            create_raindrop(ai_settings, screen, raindrops, raindrop_number, row_number)

def check_fleet_edges(ai_settings, raindrops):
    """ Respond appropriately if any raindrops have reached an edge."""
    for raindrop in raindrops.sprites():
        if raindrop.check_edges():
            change_fleet_direction(ai_settings, raindrops)
            break

def change_fleet_direction(ai_settings, raindrops):
    """Drop the entire fleet and change the fleet's direction."""
    for raindrop in raindrops.sprites():
        raindrop.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_raindrops(ai_settings, screen, raindrops):
    """
    Check if the fleet is at an edge,
    then update the positions of all raindrops in the fleet.
    """
    check_fleet_edges(ai_settings, raindrops)
    raindrops.update()

    if len(raindrops) == 0:
        raindrops.empty()
        create_fleet(ai_settings, screen, raindrops)















