import pygame

running = True
title = True

def drawTitleScreen(win, score, dino, buttons):
	win.fill((255,255,255))
	for b in buttons:
		if b.name == "StartButton":
			b.draw(win)
		elif b.name == "StartButton2P":
			b.draw(win)
	pygame.display.update()

def drawGame(win ,score, score2, dino, dino2, obstacles, obstacles2, multiplePlayers):
		win.fill((255,255,255))
		floor = pygame.Rect(0, 170, 600, 3)
		pygame.draw.rect(win, (50,50,50), floor)
		for o in obstacles:
			o.draw(win)
		dino.draw(win)
		font = pygame.font.SysFont('arial', 30, True)
		if score < 10:
			textScore = font.render("Score : 0000" + str(score), 1, (0,0,0))
		elif score < 100:
			textScore = font.render("Score : 000" + str(score), 1, (0,0,0))
		elif score < 1000:
			textScore = font.render("Score : 00" + str(score), 1, (0,0,0))
		elif score < 10000:
			textScore = font.render("Score : 0" + str(score), 1, (0,0,0))
		else:
			textScore = font.render("Score : " + str(score), 1, (0,0,0))
		win.blit(textScore, (420, 0))
		if multiplePlayers:
			floor = pygame.Rect(0, 370, 600, 3)
			pygame.draw.rect(win, (50,50,50), floor)
			for o in obstacles2:
				o.draw(win)
			dino2.draw(win)
			if dino2.alive:
				font = pygame.font.SysFont('arial', 30, True)
				if score2 < 10:
					textScore = font.render("Score : 0000" + str(score2), 1, (0,0,0))
				elif score2 < 100:
					textScore = font.render("Score : 000" + str(score2), 1, (0,0,0))
				elif score2 < 1000:
					textScore = font.render("Score : 00" + str(score2), 1, (0,0,0))
				elif score2 < 10000:
					textScore = font.render("Score : 0" + str(score2), 1, (0,0,0))
				else:
					textScore = font.render("Score : " + str(score2), 1, (0,0,0))
				win.blit(textScore, (420, 200))
		pygame.display.update()

def drawDeathScreen(win, score, score2, dino, dino2, obstacles, obstacles2, buttons, multiplePlayers):
	win.fill((255,255,255))
	font = pygame.font.SysFont('arial', 30, True)
	if score < 10:
		textScore = font.render("0000" + str(score), 1, (0,0,0))
	elif score < 100:
		textScore = font.render("000" + str(score), 1, (0,0,0))
	elif score < 1000:
		textScore = font.render("00" + str(score), 1, (0,0,0))
	elif score < 10000:
		textScore = font.render("0" + str(score), 1, (0,0,0))
	else:
		textScore = font.render("" + str(score), 1, (0,0,0))
	win.blit(textScore, (260, 20))
	floor = pygame.Rect(0, 170, 600, 3)
	pygame.draw.rect(win, (50,50,50), floor)
	for o in obstacles:
		o.draw(win)
	dino.draw(win)
	for b in buttons:
		if b.name == "RestartButton":
			b.draw(win)
	if multiplePlayers:
		if score2 < 10:
			textScore = font.render("0000" + str(score2), 1, (0,0,0))
		elif score2 < 100:
			textScore = font.render("000" + str(score2), 1, (0,0,0))
		elif score2 < 1000:
			textScore = font.render("00" + str(score2), 1, (0,0,0))
		elif score2 < 10000:
			textScore = font.render("0" + str(score2), 1, (0,0,0))
		else:
			textScore = font.render("" + str(score2), 1, (0,0,0))
		win.blit(textScore, (260, 220))
		floor = pygame.Rect(0, 370, 600, 3)
		pygame.draw.rect(win, (50,50,50), floor)
		for o in obstacles2:
			o.draw(win)
		dino2.draw(win)
	pygame.display.update()

def drawAll(win, score, score2, dino, dino2, obstacles, obstacles2, running, title, buttons, players):
	if not players:
		if dino.alive:
			drawGame(win, score, score2, dino, dino2, obstacles, obstacles2, players)
		elif not title:
			drawDeathScreen(win, score,score2, dino, dino2, obstacles, obstacles2, buttons, players)
		else:
			drawTitleScreen(win, score, dino, buttons)
	else:
		if dino.alive or dino2.alive:
			drawGame(win, score, score2, dino, dino2, obstacles, obstacles2, players)
		elif not title:
			drawDeathScreen(win, score,score2, dino, dino2, obstacles, obstacles2, buttons, players)
		else:
			drawTitleScreen(win, score, dino, buttons)
	running = running
	title = title