import pygame
from constants import *

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		pygame.display.flip()

		# Set frame rate to 60 - tick returns how longs since last time it was called
		dt = clock.tick(60) 

if __name__ == "__main__":
	main()