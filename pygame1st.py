import pygame
pygame.init()
win = pygame.display.set_mode((1855,1025))
pygame.display.set_caption("First Game")

x=50
y=50
width=40
height=60
radius=20
vel=5

run=True
while run:
	pygame.time.delay(10)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run=False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT]:
		x-=vel

	if keys[pygame.K_RIGHT]:
		x+=vel

	if keys[pygame.K_UP]:
		y-=vel

	if keys[pygame.K_DOWN]:
		y+=vel
 
	if x>1855:
		x=-40
		print("X=:",x)

	if y>1025:
		y= -50
		print("Y=:",y)
	if x<-41:
	 	x=1854

	if y<-51:
		y=1024	 

	win.fill((0,0,0))

	pygame.draw.rect(win,(255,0,0),(x,y,width,height))
	#pygame.draw.circle(win,(0,255,0),(x,y),radius)
	pygame.display.update()

pygame.quit()