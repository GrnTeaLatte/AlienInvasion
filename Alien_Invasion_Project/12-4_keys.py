import sys

import pygame

from keys_settings import Settings

import game_functions as gf

def run_game():
	# Initialize pygame, settings, and screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Print KEYDOWN")

	# Start the main loop for the game.
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				print(pygame.KEYDOWN)

run_game()