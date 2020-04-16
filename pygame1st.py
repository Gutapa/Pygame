import pygame
pygame.init()
win = pygame.display.set_mode((1800,1200))
pygame.display.set_caption("First Game")

x=50
y=50
width=40
height=60
vel=5

run=True
while run:
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run=False

pygame.quit()