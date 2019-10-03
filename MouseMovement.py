import pygame

pygame.init()

screenWidth = 500
screenHeight = screenWidth

win = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("LERP")
clock = pygame.time.Clock()


class Square(object):

	def __init__(self,x,y,h,w,c):
		self.x = x
		self.y = y
		self.h = h
		self.w = w
		self.c = c

	def Draw(self,win):
		pygame.draw.rect(win,self.c,(self.x,self.y,self.w,self.h))

	def Move(self):
		pass
	# update position by 20% of the distance between position and target position
		

def QuitGame():
	pygame.quit()
	quit()

Sq = Square(30,50,60,60,(0,0,255))


def DisplayUpdate():

	win.fill((255,255,255))
	
	Move()
	Sq.Draw(win)

	pygame.display.update()

def Move():
	
	mouse = pygame.mouse.get_pos()
	m1 = 0
	m2 = 0
	Pressed = False

	for events in pygame.event.get():
		if events.type == pygame.MOUSEBUTTONDOWN:
			m1 = mouse[0]
			m2 = mouse[1]
			Pressed = True

	
			print("x : ("+str(Sq.x)+") += ("+str(m1)+" - "+str(Sq.x)+")*0,3")
			print("y : ("+str(Sq.y)+") += ("+str(m2)+" - "+str(Sq.y)+")*0,3")
			Sq.x += (m1 - Sq.x)*0.1
			Sq.y += (m2 - Sq.y)*0.1
		

	


def MainLoop():

	run = True
	
	x = Sq.x
	y = Sq.y
	
	while run:

		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()	

		clock.tick(120)
		DisplayUpdate()

		
	
	return


MainLoop()
QuitGame()



