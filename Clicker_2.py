import pygame
import math
import random

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()


# SCREEN DIMENSIONS
screenWidth = 1280
screenHeight = 720

# BASE BUTTON DIMENSIONS
buttonW = 90
buttonH = 30


# COLORS
red = (255,0,0)
green = (0,190,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
light_green = (80,190,80)

# SOUNDS
hitSound = pygame.mixer.Sound('hit.wav')
missSound = pygame.mixer.Sound('miss.wav')
countSound = pygame.mixer.Sound('count_sound.wav')
goSound = pygame.mixer.Sound('go.wav')
clickSound = pygame.mixer.Sound('buttonClick.wav')

# MUSIC
music = pygame.mixer.music.load('music.mp3')



# FONTS
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
	
	REACTION_TEXT = Text(screenWidth/2-50,screenHeight/2,"mono",100,str(round(reaction_time,2)),white)
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

def Scoreboard(average,missed_all,distance,size_of_targets):

	scoreBoard = True
	
	while scoreBoard:
		
		win.fill(white)
		
		AVG_TEXT = Text(screenWidth/2-400,screenHeight/2+60,'mono',30,"Your average reaction time was : " + str(average)+ "s",red)
		PRESS_TEXT = Text(screenWidth/2-400,screenHeight/2+60*2,'mono',20,"Press [SPACE] for New Game or [ESC] for Main Menu",black)
		MISSED_TEXT = Text(screenWidth/2-400,screenHeight/2+60*3,'mono',20,"MISSED SQUARES : " + str(missed_all),black)
		# MISSED_DISTANCE_TEXT = Text(screenWidth/2-400,screenHeight/2+60*4,'mono',20,"TOTAL MISSED DISTANCE : "+str(distance)+" pixels",black)
		
		# Avg = end_font.render("YOUR AVERAGE REACTION TIME WAS : " + str(average) + "s",1,red)
		# press = font.render("PRESS [SPACE] FOR NEW GAME OR [ESC] FOR MAIN MENU",2,black)
		# missed_text = end_font.render("MISSED SQUARES : " +str(missed_all),2,black)

		AVG_TEXT.Draw(win)
		PRESS_TEXT.Draw(win)
		MISSED_TEXT.Draw(win)
		# MISSED_DISTANCE_TEXT.Draw(win)


		# win.blit(Avg,(screenWidth/2-300,screenHeight/2))
		
		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_SPACE]:
			GameLoop(game_length,size_of_targets)
			scoreBoard = False

		elif keys[pygame.K_ESCAPE]:
			Menu(size_of_targets)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		pygame.display.update()
		clock.tick(30)


# def Collision(x,y,w,h):
# 	mouse = pygame.mouse.get_pos()
# 	events = pygame.event.get()
# 	for ev in events:
# 		if ev.type == pygame.MOUSEBUTTONDOWN:
# 					
# 					if (mouse[0] >= x and mouse[0] <= x + w) and (mouse[1] >= y and mouse[1] <= y + h):
# 						Coll = True
# 					else:
# 						Coll = False

def CountDown():
	pygame.mixer.music.stop()
	for x in range(4,0,-1):
		
		win.fill(black)
		if x > 1:
			CountDownText = Text(screenWidth/2-50,screenHeight/2-50,'mono',100,str(x-1),white) 
			CountDownText.Draw(win)
			countSound.play()
		elif x <= 1:
			GoText = Text(screenWidth/2-80,screenHeight/2-50,'mono',100,"GO",green)
			GoText.Draw(win)
			goSound.play()

		pygame.display.update()
		clock.tick(120)
		pygame.time.wait(1000)
		

	
	
	pygame.display.update()
	clock.tick(120)
	


def Menu(size_of_targets):
	pygame.mixer.music.play(-1)
	NumberOfObjects = 5
	ObjSizeList = ['random','10','20','30','40','50','60']
	ObjSizeListIndex=ObjSizeList.index(str(size_of_targets))
	intro = True


	while intro:

		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				QuitGame()

		win.fill(white)
		

		# NewGameButton = pygame.draw.rect(win,red,(screenWidth/2-buttonW/2,screenHeight/2-30,buttonW,buttonH))

		
		# Declaring buttons
		NewGameButton = Button(screenWidth/2-buttonW/2,screenHeight/2-30,buttonW,buttonH,light_green,green)
		QuitGameButton = Button(screenWidth/2-buttonW/2,screenHeight/2+10,buttonW,buttonH,light_green,green)
		IncreaseNumberOfObj = Button(screenWidth/5,screenHeight/5,30,30,light_green,green)
		DecreaseNumberOfObj = Button(screenWidth/5,screenHeight/5+IncreaseNumberOfObj.h+30,30,30,light_green,green)
		IncreaseSizeOfObj = Button(screenWidth/5,screenHeight/5+200,30,30,light_green,green)
		DecreaseSizeOfObj = Button(screenWidth/5,screenHeight/5+IncreaseNumberOfObj.h+30+200,30,30,light_green,green)
		

		

		# Declaring Texts
		NUMBEROFOBJECTS_TEXT = Text(screenWidth/5-170,screenHeight/5+40,'mono',15,"Targets to click :  "+str(NumberOfObjects),black)
		SIZEOFTARGETS_TEXT = Text(screenWidth/5-170,screenHeight/5+240,'mono',15,"Size of Targets :  "+ObjSizeList[ObjSizeListIndex],black)
		
		# Drawing buttons
		NewGameButton.DrawWithText(win,"New Game",black,small_font)
		QuitGameButton.DrawWithText(win,"Quit",black,small_font)
		IncreaseNumberOfObj.DrawWithText(win,"+",black,big_font)
		DecreaseNumberOfObj.DrawWithText(win,"-",black,big_font)
		IncreaseSizeOfObj.DrawWithText(win,"+",black,big_font)
		DecreaseSizeOfObj.DrawWithText(win,"-",black,big_font)
		# Drawing texts
		NUMBEROFOBJECTS_TEXT.Draw(win)
		SIZEOFTARGETS_TEXT.Draw(win)



		# if Collision(IncreaseNumberOfObj.x,IncreaseNumberOfObj.y,IncreaseNumberOfObj.w,IncreaseNumberOfObj.h):
		# 	NumberOfObjects += 1
		# elif Collision(DecreaseNumberOfObj.x,DecreaseNumberOfObj.y,DecreaseNumberOfObj.w,DecreaseNumberOfObj.h):
		# 	NumberOfObjects -= 1

		# def Increase(nr):
		# 	print('NEM HIVODIK')
		# 	return nr + 1

		event = pygame.event.wait()
		
		if event.type == pygame.MOUSEBUTTONDOWN:
			if (mouse[0] >= IncreaseNumberOfObj.x and mouse[0] <= IncreaseNumberOfObj.x + IncreaseNumberOfObj.w) and (mouse[1] >= IncreaseNumberOfObj.y and mouse[1] <= IncreaseNumberOfObj.y + IncreaseNumberOfObj.h):
				clickSound.play()
				if NumberOfObjects >= 5:
					NumberOfObjects += 1
			elif (mouse[0] >= DecreaseNumberOfObj.x and mouse[0] <= DecreaseNumberOfObj.x + DecreaseNumberOfObj.w) and (mouse[1] >= DecreaseNumberOfObj.y and mouse[1] <= DecreaseNumberOfObj.y + DecreaseNumberOfObj.h):
				clickSound.play()
				if NumberOfObjects > 5:
					NumberOfObjects-=1
			elif (mouse[0] >= IncreaseSizeOfObj.x and mouse[0] <= IncreaseSizeOfObj.x + IncreaseSizeOfObj.w) and (mouse[1] >= IncreaseSizeOfObj.y and mouse[1] <= IncreaseSizeOfObj.y + IncreaseSizeOfObj.h):
				clickSound.play()
				if ObjSizeListIndex < len(ObjSizeList)-1:
					ObjSizeListIndex+=1
			elif (mouse[0] >= DecreaseSizeOfObj.x and mouse[0] <= DecreaseSizeOfObj.x + DecreaseSizeOfObj.w) and (mouse[1] >= DecreaseSizeOfObj.y and mouse[1] <= DecreaseSizeOfObj.y + DecreaseSizeOfObj.h):
				clickSound.play()
				if ObjSizeListIndex > 0:
					ObjSizeListIndex-=1

			

			elif (mouse[0] >= NewGameButton.x and mouse[0] <= NewGameButton.x + NewGameButton.w) and (mouse[1] >= NewGameButton.y and mouse[1] <= NewGameButton.y + NewGameButton.h):
				clickSound.play()
				GameLoop(NumberOfObjects,ObjSizeList[ObjSizeListIndex])
			elif (mouse[0] >= QuitGameButton.x and mouse[0] <= QuitGameButton.x + QuitGameButton.w) and (mouse[1] >= QuitGameButton.y and mouse[1] <= QuitGameButton.y + QuitGameButton.h):
				clickSound.play()
				QuitGame()
			
			size_of_targets = ObjSizeList[ObjSizeListIndex]


		
		pygame.display.update()
		clock.tick(120)

size_of_targets = 10
game_length = 5


def GameLoop(game_length,size_of_targets):

	CountDown()
	pygame.mixer.music.stop()
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
			if size_of_targets == 'random':
				Clicks.append(ClickObj(random.randint(20,60),white,green))
			else:
				Clicks.append(ClickObj(int(size_of_targets),white,green))
			spawn_time = pygame.time.get_ticks()
			spawned += 1	


			


		# COLLISON DETECT
		for Click in Clicks:

			for events in all_events:
				if events.type == pygame.MOUSEBUTTONDOWN:
					spawned_all+=1
					if ((mouse[0] >= Click.x and mouse[0] <= Click.x + Click.w) and (mouse[1] >= Click.y and mouse[1] <= Click.y + Click.h)):
						hitSound.play()
						Click.visible = False
						Clicks.pop(Clicks.index(Click))
						spawned -= 1
						clicked += 1
						reaction_time = round(pygame.time.get_ticks() - spawn_time)/1000
						times.append(reaction_time)
					else:
						missSound.play()
						Clicks.pop(Clicks.index(Click))
						# distance += round(math.sqrt((Click.x+Click.w/2) + (Click.y+Click.h/2)),2)			
						missed += 1
						spawned -= 1
						# pos.append(abs(Click.x+Click.w - mouse[0]) + abs(Click.y+Click.h - mouse[1]))
						# print(abs(Click.x - mouse[0]) + abs(Click.y - mouse[1]))
		
		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_SPACE]:
			GameLoop(game_length)
			scoreBoard = False

		elif keys[pygame.K_ESCAPE]:
			Menu(size_of_targets)

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
			times = []
			
			# for p in pos:
			# 	print(p)
			# 	print(str(pos.index(p)) + ". position : ")
			Scoreboard(average,missed_all,distance,size_of_targets)

		distance = 0
		average = 0

		Redrawgamewindow(reaction_time,average,Clicks)

Menu(size_of_targets)
GameLoop(game_length,size_of_targets)
QuitGame()