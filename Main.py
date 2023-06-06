import pygame
from Dino.Dino import Dino
from Obstacle.Obstacle import Obstacle
from Classes.Button import Button
from Draw import *
from random import uniform

pygame.init()

speed = 5

score = 0
score2 = 0
scoreCooldown = 6

multiplePlayers = False

screenWidth = 600
screenHeight = 400

if not multiplePlayers:
	screenHeight = 200

window = (screenWidth, screenHeight)
win = pygame.display.set_mode(window)
background = pygame.Surface(window)

pygame.display.set_caption("Dino Game")
clock = pygame.time.Clock()
ticks_per_second = 60

dino = Dino(130)
dino2 = Dino(330)


obstacles = []
obstacles2 = []

obstacleCooldown = 60

running = True

title = True
dino.alive = False
dino2.alive = False

spacebar = False

buttons = []
#if not multiplePlayers:
buttons.append(Button("StartButton", 50, 50, 225, 100, (0,0,255), "Start 1P"))
buttons.append(Button("StartButton2P", 325, 50, 225, 100, (0,0,255), "Start 2P"))
buttons.append(Button("RestartButton", 175, 70, 250, 60, (0,0,255), "Restart?" ))

def generateObstacle():
	global obstacleCooldown
	if not running:
		return

	if obstacleCooldown > 0:
		obstacleCooldown -= 1
		return

	randomType = uniform(0,4)
	if randomType < 1:
		obstacles.append(Obstacle("smallCactus", 140))
	elif randomType < 2:
		obstacles.append(Obstacle("longCactus", 140))
	elif randomType < 3:
		obstacles.append(Obstacle("tallCactus", 115))
	else:
		randomType = uniform(0,3)
		if randomType < 1:
			obstacles.append(Obstacle("lowBird", 145))
		elif randomType < 2:
			obstacles.append(Obstacle("mediumBird", 130))
		else:
			obstacles.append(Obstacle("highBird", 90))

	randomType = uniform(0,4)
	if randomType < 1:
		obstacles2.append(Obstacle("smallCactus", 340))
	elif randomType < 2:
		obstacles2.append(Obstacle("longCactus", 340))
	elif randomType < 3:
		obstacles2.append(Obstacle("tallCactus", 315))
	else:
		randomType = uniform(0,3)
		if randomType < 1:
			obstacles2.append(Obstacle("lowBird", 345))
		elif randomType < 2:
			obstacles2.append(Obstacle("mediumBird", 330))
		else:
			obstacles2.append(Obstacle("highBird", 290))
	interval = uniform(75 - speed * 3, 190 - speed * 4)
	obstacleCooldown = interval

def checkForClicks():
	global window
	global win
	global title
	global dino
	global multiplePlayers
	pos = pygame.mouse.get_pos()
	pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
	if pressed1:
		for b in buttons:
			if b.name == "StartButton" and title:
				if b.rec.collidepoint(pos):
					title = False
					dino.alive = True
					break
			if b.name == "StartButton2P" and title:
				if b.rec.collidepoint(pos):
					multiplePlayers = True
					title = False
					dino.alive = True
					dino2.alive = True
					window = (600, 400)
					win = pygame.display.set_mode(window)
					break
			elif b.name == "RestartButton" and not title and not dino.alive:
				if b.rec.collidepoint(pos):
					reset()

 
def addScore():
	global score
	global score2
	global scoreCooldown
	global speed
	global dino
	global dino2
	speed = 5 + score / 200
	if scoreCooldown <= 0:
		if dino.alive:
			score += 1
			score += round(speed / 7)
		if multiplePlayers:
			if dino2.alive:
				score2 += 1
				score2 += round(speed / 7)
		scoreCooldown = 6	
	else:
		scoreCooldown -= 1

def reset():
	global score
	global score2
	global scoreCooldown
	global dino
	global dino2
	global obstacles
	global obstacles2
	global obstacleCooldown
	global speed
	score = 0
	score2 = 0
	scoreCooldown = 6
	dino = Dino(130)
	for o in obstacles:
		obstacles.pop(obstacles.index(o))
	if multiplePlayers:
		dino2 = Dino(330)
	for o in obstacles2:
		obstacles2.pop(obstacles2.index(o))
	obstacleCooldown = 120
	speed = 5

while running:
	clock.tick(ticks_per_second)
	checkForClicks()
	keys = pygame.key.get_pressed()
	if not title:
		# OBSTAKELS BEWEGEN
		for o in obstacles:
			if dino.alive:
				o.move(speed)
				if o.x < -100:
					obstacles.pop(obstacles.index(o))
				if o.hitbox.colliderect(dino.hitbox):
					dino.alive = False
		if multiplePlayers:
			for o in obstacles2:
				if dino2.alive:
					o.move(speed)
					if o.x < -100:
						obstacles2.pop(obstacles2.index(o))
					if o.hitbox.colliderect(dino2.hitbox):
						dino2.alive = False

		# JUMP
		if not dino.isJumping and dino.alive:
			if keys[pygame.K_UP]:
				dino.isJumping = True
		dino.jump()
		if multiplePlayers:
			if not dino2.isJumping and dino2.alive:
				if keys[pygame.K_SPACE]:
					dino2.isJumping = True
			dino2.jump()

		# BUKKEN
		if keys[pygame.K_DOWN] and dino.alive:
			dino.ducking = True
			if dino.m < 1:
				dino.m *= 1.15
			elif dino.m < 1:
				dino.m = 1
		else:
			dino.ducking = False

		if multiplePlayers:
			if keys[pygame.K_LCTRL] and dino2.alive:
				dino2.ducking = True
				if dino2.m < 1:
					dino2.m *= 1.15
				elif dino2.m < 1:
					dino2.m = 1
			else:
				dino2.ducking = False
		if not multiplePlayers and not dino.alive and not title:
			if keys[pygame.K_RETURN]:
				reset()
		elif multiplePlayers and not dino.alive and not dino2.alive and not title:
			if keys[pygame.K_RETURN]:
				reset()
		if keys[pygame.K_ESCAPE]:
			running = False

		if multiplePlayers and dino.alive or dino2.alive:
			generateObstacle()
			addScore()
		elif dino.alive :
			generateObstacle()
			addScore()
	else:
		if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
			title = False
			dino.alive = True
			if multiplePlayers:
				dino2.alive = True

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	drawAll(win, score, score2, dino, dino2, obstacles, obstacles2, running, title, buttons, multiplePlayers)
pygame.quit()