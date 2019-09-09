import pygame
import random

pygame.init()

screenWidth = 1280
screenHeight = 720

buttonW = 90
buttonH = 30



red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)





clock = pygame.time.Clock()

win = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Clicker")

class ClickObj(object):
	
	def __init__(self,h):
		self.h = h
		self.w = self.h
		self.x = random.randint(1,screenWidth-self.w)
		self.y = random.randint(1,screenHeight-self.h)
		self.visible = True

	def Draw(self,win):
		if self.visible:
			mouse = pygame.mouse.get_pos()
			
			if (mouse[0] >= self.x and mouse[0] <= self.x + self.w) and (mouse[1] >= self.y and mouse[1] <= self.y + self.h):
				pygame.draw.rect(win,red,(self.x,self.y,self.w,self.h))
			else:
				pygame.draw.rect(win,green,(self.x,self.y,self.w,self.h))





class Button(object):

	def __init__(self,x,y,w,h,color):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.color = color
		self.hitbox = (self.x,self.y,self.w,self.h)

	def Draw(self,win):
		mouse = pygame.mouse.get_pos()

		if (mouse[0] >= self.x and mouse[0] <= self.x + self.w) and (mouse[1] >= self.y and mouse[1] <= self.y + self.h):
			pygame.draw.rect(win,red,(self.x,self.y,self.w,self.h))
		else:
			pygame.draw.rect(win,green,(self.x,self.y,self.w,self.h))




def Redrawgamewindow():

	win.fill(white)
	reaction_text = font.render("your last reaction time was : " + str(reaction_time),1,black)
	average_text = font.render("average : " + str(average),1,black)
	
	for Click in Clicks:
		Click.Draw(win)
	
	win.blit(reaction_text,(screenWidth/2,screenHeight/2))
	win.blit(average_text,(screenWidth/2,screenHeight/2-30))
	pygame.display.update()

def quitgame():
	pygame.quit()
	quit()

def Scoreboard():

	scoreBoard = True
	
	while scoreBoard:
		
		win.fill(white)
		
		Avg = end_font.render("YOUR AVERAGE REACTION TIME WAS : " + str(average) + "s",1,red)
		press = font.render("PRESS [SPACE] FOR NEW GAME OR [ESC] FOR MAIN MENU",2,black)
		missed_text = end_font.render("MISSED SQUARES : " +str(missed_all),2,black)

		win.blit(Avg,(screenWidth/2-300,screenHeight/2))
		win.blit(press,(screenWidth/2-300,screenHeight/2+120))
		win.blit(missed_text,(screenWidth/2-300,screenHeight/2+60))
		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_SPACE]:
			return
			scoreBoard = False

		elif keys[pygame.K_ESCAPE]:
			Menu()

		for event in pygame.event.get():

	            	if event.type == pygame.QUIT:
	                	pygame.quit()
	                	quit()
		pygame.display.update()
		clock.tick(30)


def Collison(x,y,w,h,action = None):
	coll = False
	mouse = pygame.mouse.get_pos()

	while not coll:
		if (mouse[0] >= x and mouse[0] <= x + w) and (mouse[1] >= y and mouse[1] <= y + h) and pygame.mouse.get_pressed()[0] and (action):
			coll = True
	action()		



def Menu():

	intro = True

	while intro:

		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		for event in pygame.event.get():
		#print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		win.fill(white)
		# New Game text
		new_game_text = font.render("New Game",1,(0,0,0))
		# Quit text
		quit_text = font.render("Quit",1,(0,0,0))
		# MISSED TEXT

		# button1 = pygame.draw.rect(win,red,(screenWidth/2-buttonW/2,screenHeight/2-30,buttonW,buttonH))
		button1 = Button(screenWidth/2-buttonW/2,screenHeight/2-30,buttonW,buttonH,red)
		button2 = Button(screenWidth/2-buttonW/2,screenHeight/2+10,buttonW,buttonH,red)
		
		button1.Draw(win)
		button2.Draw(win)

		win.blit(new_game_text,(button1.x+7,button1.y+7))
		win.blit(quit_text,(button2.x+26,button2.y+7))

		if (mouse[0] >= screenWidth/2 - buttonW/2 and mouse[0] <= screenWidth/2 + buttonW/2) and (mouse[1] >= screenHeight/2-30 and mouse[1] <= screenHeight/2-30 + buttonH) and pygame.mouse.get_pressed()[0]:
			return
		elif (mouse[0] >= screenWidth/2 - buttonW/2 and mouse[0] <= screenWidth/2 + buttonW/2) and (mouse[1] >= screenHeight/2+10 and mouse[1] <= screenHeight/2 + buttonH) and pygame.mouse.get_pressed()[0]:
			quitgame()

		pygame.display.update()
		clock.tick(30)



run = True
spawned = 0
max_spawned = 1
clicked = 0
spawn_time = 0
reaction_time = 0
average = 0
missed = 0
missed_all = 0


Clicks = []
times = []
pos = []

game_length = 5

font = pygame.font.SysFont('mono',15)
end_font = pygame.font.SysFont('mono',40)




Menu()

while run:


	clock.tick(60)
	


	mouse = pygame.mouse.get_pos()
	all_events = pygame.event.get()


	# SPAWNING
	if spawned < max_spawned:
		Clicks.append(ClickObj(random.randint(20,60)))
		spawn_time = pygame.time.get_ticks()
		spawned += 1


		


	# COLLISON DETECT
	for Click in Clicks:

		for events in all_events:
			if events.type == pygame.MOUSEBUTTONDOWN:
				if ((mouse[0] >= Click.x and mouse[0] <= Click.x + Click.w) and (mouse[1] >= Click.y and mouse[1] <= Click.y + Click.h)):
					Click.visible = False
					Clicks.pop(Clicks.index(Click))
					spawned -= 1
					clicked += 1
					reaction_time = round(pygame.time.get_ticks() - spawn_time)/1000
					times.append(reaction_time)
				else:
					Clicks.pop(Clicks.index(Click))
					missed += 1
					spawned -=1
					# pos.append(abs(Click.x+Click.w - mouse[0]) + abs(Click.y+Click.h - mouse[1]))
					# print(abs(Click.x - mouse[0]) + abs(Click.y - mouse[1]))
				

	for events in all_events:
		if events.type == pygame.QUIT:
			run = False
	
	# CALCULATING AVERAGE
	if clicked >= game_length:
		for time in times:
			average += time
		average = round((average / len(times)),2)
		clicked = 0
		missed_all = missed
		missed = 0
		times.clear()
		# for p in pos:
		# 	print(p)
		# 	print(str(pos.index(p)) + ". position : ")
		Scoreboard()


	Redrawgamewindow()




quitgame()










	#for event in pygame.event.get():
	#	print(event)
