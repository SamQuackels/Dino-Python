import pygame

class Obstacle:
	def __init__(self, t, y):
		self.x = 800
		self.type = t
		self.y = y
		if self.type == "smallCactus":
			self.width = 20
			self.height = 40
			self.image = pygame.image.load("Obstacle/img/smallCactus.png")
		elif self.type == "longCactus":
			self.width = 80
			self.height = 30
			self.image = pygame.image.load("Obstacle/img/longCactus.png")
		elif self.type == "tallCactus":
			self.width = 20
			self.height = 60
			self.image = pygame.image.load("Obstacle/img/tallCactus.png")
		elif self.type == "lowBird":
			self.width = 40
			self.height = 20
		elif self.type == "mediumBird":
			self.width = 40
			self.height = 20
		elif self.type == "highBird":
			self.width = 20
			self.height = 50
		self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

	def draw(self, win):
		self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
		if self.type == "smallCactus" or self.type == "longCactus" or self.type == "tallCactus":
			win.blit(self.image, (self.x, self.y))
		else:
			pygame.draw.rect(win, (0,0,0), self.hitbox)

	def move(self, speed):
		self.x -= speed