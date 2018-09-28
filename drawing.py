#import libraries
import pygame, sys, random
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS

#initialise the pygame class
pygame.init()

clock = pygame.time.Clock()

windowwidth = 500
windowheight = 400

rectX = 220
rectY = 190
rectendX = 30.0
rectendY = 20.0
rectXmv = 1
rectYmv = 1
colour_1 = 102
colour_2 = 224
colour_3 = 71
windowbuffer = 50

def quitgame():
	pygame.quit()
	sys.exit()



#create size of the window to 500 by 400 pixels
window = pygame.display.set_mode((windowwidth,windowheight))

# To keep window open indefinitely
while True:
	
	window.fill((0,0,0))
	
	# draw shapes (R,G,B) (distance from left, distance from top, width, height)
	#pygame.draw.rect(window, (3,60,153),(10, 10, 200, 100))
	#pygame.draw.rect(window, (99,4,4),(300, 10, 50, 75))
	#pygame.draw.rect(window, (3,60,153),(10, 10, 200, 100))
	#pygame.draw.rect(window, (3,60,153),(10, 10, 200, 100))
	
	#pygame.draw.lines(window, (3,60,153), False, [(10,10),(10,150),(60,50),(110,150),(110,10)], 4)
	#pygame.draw.lines(window, (99,4,4), False, [(150,150),(150,10),(200,100),(250,10),(250,150)], 4)

	pygame.draw.rect(window, (colour_1,colour_2,colour_3), (rectX,rectY,rectendX,rectendY))
	
	rectX += random.randint(-10,10)
	rectY += random.randint(-10,10)
	#rectendX += random.randint(1,5)
	#rectendY += random.randint(1,5)
	colour_1 = random.randint(1,255)
	colour_2 = random.randint(1,255)
	colour_3 = random.randint(1,255)
	
	if rectX > (windowwidth - windowbuffer):
		rectX = random.randint(0,windowwidth)
		
	if rectX < (windowbuffer):
		rectX = random.randint(0,windowwidth)
		
	if rectY > (windowheight - windowbuffer):
		rectY = random.randint(0,windowheight)
		
	if rectY < (windowbuffer):
		rectY = random.randint(0,windowheight)
	
	#Close/Quit code when pressing the X button in corner of window or hitting the escape key
	for event in GAME_EVENTS.get():
		if event.type == GAME_GLOBALS.QUIT:
			quitgame()
			
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				quitgame()
			
		
	clock.tick(30)
	pygame.display.update()
	

	
	