import pygame

class Dino:
	def __init__(self, y):
		self.x = 30
		self.y = y
		self.ogY = self.y
		self.dino1 = pygame.image.load("Dino/img/Dino1.png")
		self.dino2 = pygame.image.load("Dino/img/Dino2.png")
		self.dino3 = pygame.image.load("Dino/img/Dino3.png")
		self.dinoDood = pygame.image.load("Dino/img/DinoDood.png")
		self.dinoDucking1 = pygame.image.load("Dino/img/DinoDucking1.png")
		self.dinoDucking2 = pygame.image.load("Dino/img/DinoDucking2.png")
		self.ani = 1
		self.isJumping = False
		self.hitbox = pygame.Rect(self.x + 5, self.y + 8, 45, 48)
		self.m = 1
		self.v = 13
		self.ogV = self.v
		self.alive = True 
		self.ducking = False
		self.falling = False

	def draw(self, win):
		if not self.ducking:
			self.hitbox = pygame.Rect(self.x + 15, self.y + 8, 25, 48)
		else:
			self.hitbox = pygame.Rect(self.x + 15, self.y + 32, 30, 25)
		aniMultiplier = 5
		if (not self.isJumping and self.alive and not self.ducking):
			if self.ani < (1 * aniMultiplier):
				win.blit(self.dino1, (self.x, self.y))
			elif self.ani < (2 *aniMultiplier):
				win.blit(self.dino2, (self.x, self.y))
			elif self.ani < (3 * aniMultiplier):
				win.blit(self.dino3, (self.x, self.y))
			self.ani += 1
			if self.ani >= (3 * aniMultiplier):
				self.ani = 1
		elif self.ducking:
			if self.ani < (1.5 * aniMultiplier):
				win.blit(self.dinoDucking1, (self.x, self.y))
			else:
				win.blit(self.dinoDucking2, (self.x, self.y))
			self.ani += 1
			if self.ani >= (3 * aniMultiplier):
				self.ani = 1
		elif not self.alive:
			win.blit(self.dinoDood, (self.x, self.y))
		else:
			win.blit(self.dino1, (self.x, self.y))
		#pygame.draw.rect(win, (255,0,0), self.hitbox,2)

	def jump(self):
		if self.isJumping and self.alive:
			F = (1/2)*self.m*(self.v)
			self.y -= F
			if self.falling:
				x = 0.5
			else:
				x = -0.5
			self.v = self.v + x
			if self.v == 0:
				self.falling = True
				self.m = -1
			if self.y >= self.ogY and self.m <= -1:
				self.y = self.ogY
				self.isJumping = False
				self.falling = False
				self.v = self.ogV
				self.m = 1