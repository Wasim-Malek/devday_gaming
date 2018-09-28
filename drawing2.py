#import libraries
import pygame, sys, random
import pygame.event as GAME_EVENTS
import pygame.locals as GAME_GLOBALS

#initialise the pygame class
pygame.init()

clock = pygame.time.Clock()

blob = pygame.image.load('images/trump.jpg')

windowWidth = 500
windowHeight = 400

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

playerSize = 10
playerX = (windowWidth / 2) - (playerSize / 2)
playerY = windowHeight - playerSize  - 100
playerVX = 1.0
playerVY = 0.0
jumpHeight = 35.0
moveSpeed = 1.0
maxSpeed = 10.0
gravity = 1.0

# Keyboard Variables
leftDown = False
rightDown = False
haveJumped = False


def quitgame():
	pygame.quit()
	sys.exit()

	
def move():

	global playerX, playerY, playerVX, playerVY, haveJumped, gravity

	# Move left 
	if leftDown:
		#If we're already moving to the right, reset the moving speed and invert the direction
		if playerVX > 0.0:
			playerVX = moveSpeed
			playerVX = -playerVX	
		# Make sure our square doesn't leave our window to the left
		if playerX > 0:
			playerX += playerVX	

	# Move right
	if rightDown:
		# If we're already moving to the left reset the moving speed again
		if playerVX < 0.0:
			playerVX = moveSpeed
		# Make sure our square doesn't leave our window to the right
		if playerX + playerSize < windowWidth:
			playerX += playerVX

	if playerVY > 1.0:
		playerVY = playerVY * 0.9
	else :
		playerVY = 0.0
		haveJumped = False

	# Is our square in the air? Better add some gravity to bring it back down!
	if playerY < windowHeight - playerSize:
		playerY += gravity
		gravity = gravity * 1.1
	else :
		playerY = windowHeight - playerSize
		gravity = 1.0

	playerY -= playerVY

	if playerVX > 0.0 and playerVX < maxSpeed or playerVX < 0.0 and playerVX > -maxSpeed:
		if haveJumped == False:
			playerVX = playerVX * 1.1
			


	#window.fill((0,0,0))

	

	# Get a list of all events that happened since the last redraw


#create size of the window to 500 by 400 pixels
window = pygame.display.set_mode((windowWidth,windowHeight))

# To keep window open indefinitely
while True:
	
	window.fill((255,255,255))
	
	# draw shapes (R,G,B) (distance from left, distance from top, width, height)
	#pygame.draw.rect(window, (3,60,153),(10, 10, 200, 100))
	#pygame.draw.rect(window, (99,4,4),(300, 10, 50, 75))
	#pygame.draw.rect(window, (3,60,153),(10, 10, 200, 100))
	#pygame.draw.rect(window, (3,60,153),(10, 10, 200, 100))
	
	#pygame.draw.lines(window, (3,60,153), False, [(10,10),(10,150),(60,50),(110,150),(110,10)], 4)
	#pygame.draw.lines(window, (99,4,4), False, [(150,150),(150,10),(200,100),(250,10),(250,150)], 4)

	pygame.draw.rect(window, (colour_1,colour_2,colour_3), (rectX,rectY,rectendX,rectendY))
	pygame.draw.rect(window, (255,0,0), (playerX, playerY, playerSize, playerSize))
	window.blit(blob, (playerX, playerY, playerSize, playerSize))
	
	
	rectX += random.randint(-10,10)
	rectY += random.randint(-10,10)
	#rectendX += random.randint(1,5)
	#rectendY += random.randint(1,5)
	colour_1 = random.randint(1,255)
	colour_2 = random.randint(1,255)
	colour_3 = random.randint(1,255)
	
	if rectX > (windowWidth - windowbuffer):
		rectX = random.randint(0,windowWidth)
		
	if rectX < (windowbuffer):
		rectX = random.randint(0,windowWidth)
		
	if rectY > (windowHeight - windowbuffer):
		rectY = random.randint(0,windowHeight)
		
	if rectY < (windowbuffer):
		rectY = random.randint(0,windowHeight)
	
	#Close/Quit code when pressing the X button in corner of window or hitting the escape key
	for event in GAME_EVENTS.get():
		if event.type == GAME_GLOBALS.QUIT:
			quitgame()
			
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				quitgame()
		
		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_LEFT:
				leftDown = True
			if event.key == pygame.K_RIGHT:
				rightDown = True
			if event.key == pygame.K_UP:
				if not haveJumped:
					haveJumped = True
					playerVY += jumpHeight
			if event.key == pygame.K_ESCAPE:
				quitGame()

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				leftDown = False
				playerVX = moveSpeed
			if event.key == pygame.K_RIGHT:
				rightDown = False
				playerVX = moveSpeed
		
	move()	
	
	clock.tick(30)
	pygame.display.update()
	

	
	