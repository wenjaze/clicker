import pygame
import math
import random

pygame.init()

screenWidth = 1280
screenHeight = 720

buttonW = 90
buttonH = 30



red = (255,0,0)
green = (0,190,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
light_green = (80,190,80)


small_font = pygame.font.SysFont('mono',15)
big_font = pygame.font.SysFont('mono',40)


clock = pygame.time.Clock()

win = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Clicker")

class ClickObj(object):
	
	def __init__(self,h,ac,nac):
		self.h = h
		self.w = self.h
		self.x = random.randint(1,screenWidth-self.w)
		self.y = random.randint(1,screenHeight-self.h)
		self.visible = True
		self.ac = ac
		self.nac = nac

	def Draw(self,win):
		if self.visible:
			mouse = pygame.mouse.get_pos()
			
			if (mouse[0] >= self.x and mouse[0] <= self.x + self.w) and (mouse[1] >= self.y and mouse[1] <= self.y + self.h):
				pygame.draw.rect(win,self.ac,(self.x,self.y,self.w,self.h))
			else:
				pygame.draw.rect(win,self.nac,(self.x,self.y,self.w,self.h))

class Text(object):

	def __init__(self,x,y,fonttype,size,content,color):
		self.x = x
		self.y = y
		self.fonttype = fonttype
		self.size = size
		self.content = content
		self.color = color
		self.fnt = pygame.font.SysFont(str(self.fonttype),self.size)
		self.txt = self.fnt.render(self.content,True,self.color)

	def Draw(self,win):
		win.blit(self.txt,(self.x,self.y))

class Button(object):

	#AC = Active Color
	#NAC = Not Active Color
	def __init__(self,x,y,w,h,ac,nac):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.ac = ac
		self.nac = nac
		self.hitbox = (self.x,self.y,self.w,self.h)

	def Draw(self,win):
		mouse = pygame.mouse.get_pos()

		if (mouse[0] >= self.x and mouse[0] <= self.x + self.w) and (mouse[1] >= self.y and mouse[1] <= self.y + self.h):
			pygame.draw.rect(win,self.ac,(self.x,self.y,self.w,self.h))
		else:
			pygame.draw.rect(win,self.nac,(self.x,self.y,self.w,self.h))

	def DrawWithText(self,win,text,textcolor,font):
		mouse = pygame.mouse.get_pos()

		def DrawText(text,textcolor):
			text = small_font.render(str(text), True, textcolor)
			text_rect = text.get_rect(center = (self.x+self.w/2,self.y+self.h/2))
			win.blit(text,text_rect)

		if (mouse[0] >= self.x and mouse[0] <= self.x + self.w) and (mouse[1] >= self.y and mouse[1] <= self.y + self.h):
			pygame.draw.rect(win,self.ac,(self.x,self.y,self.w,self.h))
			DrawText(text,textcolor)
		else:
			pygame.draw.rect(win,self.nac,(self.x,self.y,self.w,self.h))
			DrawText(text,textcolor)








def Redrawgamewindow(reaction_time,average,Clicks):

	win.fill(black)
	# reaction_text = small_font.render("your last reaction time was : " + str(reaction_time),1,black)
	
	REACTION_TEXT = Text(screenWidth/2,screenHeight/2,"mono",20,"Your reaction time was : "+str(reaction_time),black)
	REACTION_TEXT.Draw(win)

	for Click in Clicks:
		Click.Draw(win)
	
	# win.blit(reaction_text,(screenWidth/2,screenHeight/2))
	# win.blit(average_text,(screenWidth/2,screenHeight/2-30))
	pygame.display.update()

def QuitGame():
	pygame.quit()
	quit()

def Miss():
	pass


def Scoreboard(average,missed_all,distance,accuracy):

	scoreBoard = True
	
	while scoreBoard:
		
		win.fill(white)
		
		AVG_TEXT = Text(screenWidth/2-300,screenHeight/2+60,'mono',30,"Your average reaction time was : " + str(average)+ "s",red)
		PRESS_TEXT = Text(screenWidth/2-300,screenHeight/2+60*2,'mono',20,"Press [SPACE] for New Game or [ESC] for Main Menu",black)
		MISSED_TEXT = Text(screenWidth/2-300,screenHeight/2+60*3,'mono',20,"MISSED SQUARES : " + str(missed_all),black)
		ACCURACY_TEXT = Text(screenWidth/2-300,screenHeight/2+60*4,'mono',20,"ACCURACY : " + str(accuracy)+"%",black)
		MISSED_DISTANCE_TEXT = Text(screenWidth/2-300,screenHeight/2+60*5,'mono',20,"TOTAL MISSED DISTANCE : "+str(distance)+" pixels",black)
		
		# Avg = end_font.render("YOUR AVERAGE REACTION TIME WAS : " + str(average) + "s",1,red)
		# press = font.render("PRESS [SPACE] FOR NEW GAME OR [ESC] FOR MAIN MENU",2,black)
		# missed_text = end_font.render("MISSED SQUARES : " +str(missed_all),2,black)

		AVG_TEXT.Draw(win)
		PRESS_TEXT.Draw(win)
		MISSED_TEXT.Draw(win)
		ACCURACY_TEXT.Draw(win)
		MISSED_DISTANCE_TEXT.Draw(win)


		a# win.blit(Avg,(screenWidth/2-300,screenHeight/2))
		
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


def Collision(x,y,w,h):
	mouse = pygame.mouse.get_pos()
	events = pygame.event.get()
	for ev in events:
		if ev.type == pygame.MOUSEBUTTONDOWN:
					print("fasz")
					if (mouse[0] >= x and mouse[0] <= x + w) and (mouse[1] >= y and mouse[1] <= y + h):
						Coll = True
					else:
						Coll = False



def Menu():

	intro = True

	while intro:

		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		win.fill(white)
		

		# button1 = pygame.draw.rect(win,red,(screenWidth/2-buttonW/2,screenHeight/2-30,buttonW,buttonH))

		
		# Declaring buttons
		button1 = Button(screenWidth/2-buttonW/2,screenHeight/2-30,buttonW,buttonH,light_green,green)
		button2 = Button(screenWidth/2-buttonW/2,screenHeight/2+10,buttonW,buttonH,light_green,green)
		button_increase = Button(screenWidth/5,screenHeight/5,30,30,light_green,green)
		button_decrease = Button(screenWidth/5,screenHeight/5+button_increase.h+30,30,30,light_green,green)
		# Declaring Texts
		# NUMBEROFOBJECTS_TEXT = Text(screenWidth/5-170,screenHeight/5+40,'mono',15,"Number of Objects : "+str(NumberOfObjects),black)

		
		# Drawing buttons
		button1.DrawWithText(win,"New Game",black,small_font)
		button2.DrawWithText(win,"Quit",black,small_font)
		button_increase.DrawWithText(win,"+",black,big_font)
		button_decrease.DrawWithText(win,"-",black,big_font)
		# Drawing texts
		# NUMBEROFOBJECTS_TEXT.Draw(win)



		# if Collision(button_increase.x,button_increase.y,button_increase.w,button_increase.h):
		# 	NumberOfObjects += 1
		# elif Collision(button_decrease.x,button_decrease.y,button_decrease.w,button_decrease.h):
		# 	NumberOfObjects -= 1

		def Increase(nr):
			print('NEM HIVODIK')
			return nr + 1

		event = pygame.event.get()
		if pygame.mouse.get_pressed()[0]:
			c = True
			if (mouse[0] >= button1.x and mouse[0] <= button1.x + button1.w) and (mouse[1] >= button1.y and mouse[1] <= button1.y + button1.h):
				GameLoop(game_length)
			elif (mouse[0] >= button_increase.x and mouse[0] <= button_increase.x + button_increase.w) and (mouse[1] >= button_increase.y and mouse[1] <= button_increase.y + button_increase.h):
				Increase(NumberOfObjects)
			elif (mouse[0] >= button2.x and mouse[0] <= button2.x + button2.w) and (mouse[1] >= button2.y and mouse[1] <= button2.y + button2.h):
				QuitGame()
			elif (mouse[0] >= button_decrease.x and mouse[0] <= button_decrease.x + button_decrease.w) and (mouse[1] >= button_decrease.y and mouse[1] <= button_decrease.y + button_decrease.h):
				NumberOfObjects-=1
		# if Collision(button1.x,button1.y,button1.w,button1.h):
		# 	GameLoop(game_length)
		# elif Collision(button2.x,button2.y,button2.w,button2.h):
		# 	QuitGame()

		# if (mouse[0] >= screenWidth/2 - buttonW/2 and mouse[0] <= screenWidth/2 + buttonW/2) and (mouse[1] >= screenHeight/2-30 and mouse[1] <= screenHeight/2-30 + buttonH) and pygame.mouse.get_pressed()[0]:
		#  	GameLoop()
		# elif (mouse[0] >= screenWidth/2 - buttonW/2 and mouse[0] <= screenWidth/2 + buttonW/2) and (mouse[1] >= screenHeight/2+10 and mouse[1] <= screenHeight/2 + buttonH) and pygame.mouse.get_pressed()[0]:
		# 	QuitGame()

		pygame.display.update()
		clock.tick(60)


game_length = 5


def GameLoop(game_length):

	spawned_all = 0
	hit_all = 0
	accuracy = 0
	distance = 0
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




	while run:


		clock.tick(60)
		


		mouse = pygame.mouse.get_pos()
		all_events = pygame.event.get()


		# SPAWNING
		if spawned < max_spawned:
			Clicks.append(ClickObj(random.randint(20,60),light_green,green))
			spawn_time = pygame.time.get_ticks()
			spawned += 1


			


		# COLLISON DETECT
		for Click in Clicks:

			for events in all_events:
				if events.type == pygame.MOUSEBUTTONDOWN:
					spawned_all+=1
					if ((mouse[0] >= Click.x and mouse[0] <= Click.x + Click.w) and (mouse[1] >= Click.y and mouse[1] <= Click.y + Click.h)):
						Click.visible = False
						Clicks.pop(Clicks.index(Click))
						spawned -= 1
						clicked += 1
						reaction_time = round(pygame.time.get_ticks() - spawn_time)/1000
						times.append(reaction_time)
					else:
						Clicks.pop(Clicks.index(Click))
						distance += round(math.sqrt((Click.x+Click.w/2) + (Click.y+Click.h/2)),2)			
						missed += 1
						spawned -= 1
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
			accuracy = round(clicked/spawned_all*100,2)
			clicked = 0
			missed_all = missed
			missed = 0
			times = []
			
			# for p in pos:
			# 	print(p)
			# 	print(str(pos.index(p)) + ". position : ")
			Scoreboard(average,missed_all,distance,accuracy)


		Redrawgamewindow(reaction_time,average,Clicks)

Menu()
GameLoop(game_length,distance)
QuitGame()










	#for event in pygame.event.get():
	#	print(event)
