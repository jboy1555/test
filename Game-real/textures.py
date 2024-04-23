import pygame



world =  pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/world.png')

sword = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/sword.png')
tree2 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/tree2.png')
tree3 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/tree3.png')
bggame = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/gambg.png')
tree4 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/tree4.png')
class player_text:
	player_falling_right = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/falling_player_right.png')
	player_falling_left = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/falling_player_left.png')
	player_l = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_left.png')
	player1 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_left1.25.png')
	player2 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_left1.50.png')
	player3 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_left1.75.png')
	player4 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_left2.25.png')
	player5 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_left2.50.png')
	player6 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_left2.png')
	player7 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_left3.25.png')
	player8 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_left3.50.png')
	player9 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_left3.75.png')
	player10 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_left3.png')
	player_r = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_right.png')
	player11 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_right1.25.png')
	player12 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_right1.50.png')
	player13 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_right1.75.png')
	player14 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_right2.25.png')
	player15 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_right2.50.png')
	player16 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_right2.png')
	player17 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_right3.25.png')
	player18 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_right3.50.png')
	player19 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_right3.75.png')
	player20 = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_right3.png')




inventory = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/inventory_no_use.png')
inventory_use = pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/inventory_use.png')









walkleft = [pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_left.png'),
pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_left1.25.png'),
pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_left1.50.png'),
pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_left1.75.png'),
pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_left2.25.png'),
pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_left2.50.png'),
pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_left2.png'),
pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_left3.25.png'),
pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_left3.50.png'),
pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_left3.75.png'),
pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_left3.png')]
walkright = [pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_right.png'),
pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_right1.25.png'),
pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_right1.50.png'),
pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_right1.75.png'),
pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_right2.25.png'),
pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_right2.50.png'),
pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_right2.png'),
pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_right3.25.png'),
pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_right3.50.png'),
pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_right3.75.png'),
pygame.image.load('C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/player_right3.png')]

