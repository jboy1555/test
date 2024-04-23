import pygame
from var import *
from time import *

from textures import *
from RGB import *

from hitboxes import *

from tkinter import *
import json
from PIL import Image, ImageTk
pygame.init()
def varables_in_main_code():
	global items, name, left,playerx, playery, display_w, display_h, display, cam_not_in_radius,world_move,to_use_tel,dont_go, right
	cam_not_in_radius = True
	items = ['sword']
	name = ['jboy1555']
	display = pygame.display.Info()
	display_w = display.current_w
	display_h = display.current_h
	playerx = display_w / 2
	world_move = False
	right = False
	left = True
	playery = display_h / 2
	dont_go = False
	to_use_tel = False
varables_in_main_code()



world_rect = world.get_rect(top=550, bottom=3004, left=550, right=550)
world_rect.x = -700
world_rect.y = display_h - 450



def lobby_game():	
	global Rus, Eng,count,BACK
	root = Tk()
	Rus = False
	Eng = False
	count = 0
	
	# Получение размеров экрана
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	
	print
	
	
	
		
	






	# Вычисление координат для центрирования окна
	x = (screen_width - 1500) // 2  # 800 - ширина окна
	y = (screen_height - 800) // 2  # 1500 - высота окна
	play = Image.open("C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/play.png")
	lean = Image.open("C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/lang.png")
	# Задание геометрии окна (ширина x высота + смещение_x + смещение_y)
	sett = Image.open("C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/settings.png")
	root.geometry(f'1500x800+{x}+{y}')
	play_photo= ImageTk.PhotoImage(play)
	lean_photo= ImageTk.PhotoImage(lean)
	setting_photo= ImageTk.PhotoImage(sett)
	# mainloop() запускает главный цикл Tkinter
	BACK_test = Image.open("C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/BACK.png")
	BACK = ImageTk.PhotoImage(BACK_test)
	RU_test = Image.open("C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/RU.png")
	RU = ImageTk.PhotoImage(RU_test)
	ENG_test = Image.open("C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/ENG.png")
	ENG = ImageTk.PhotoImage(ENG_test)
	def animate(label, counter):	
		images = ['C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/tree_one.png', 
			'C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/tree_two.png', 'C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/tree_tree.png', 
			'C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/tree_four.png', 'C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/tree_five.png', 
			'C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/tree_six.png', 'C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/tree_seven.png',
			'C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/tree_eight.png', 'C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/tree_nine.png',
			'C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/tree_ten.png', 'C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/tree_eleven.png',
			'C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/tree_treete.png']  # Список путей к изображениям анимации
		image = Image.open(images[counter])  # Загружаем текущее изображение
		photo = ImageTk.PhotoImage(image)  # Преобразуем изображение в формат, понятный Tkinter
		label.config(image=photo)  # Обновляем изображение на метке
		label.image = photo  # Обновляем ссылку на изображение для предотвращения сбора мусора
		counter += 1
		if counter >= len(images):
			counter = 0  # Циклическая анимация
		root.after(1, animate, label, counter)
			
	label = Label(root)
	label.pack()

	# Вызываем функцию animate и передаем переменную label и начальное значение счетчика counter
	animate(label, 0)

	def Start():
		global Eng, Rus
		if Rus == False and Eng == False:
			Eng = True
			root.destroy()
	
	def language():
		global BACK
		
		Sett_B.place(x = 450, y=18100)
		Lean_P.place(x = 450, y=9300)
		Play_P.place(x = 450, y=5000)
		def back():
			Sett_B.place(x = 450, y=181)
			Lean_P.place(x = 450, y=93)
			Play_P.place(x = 450, y=5)
			Back.place(x=300, y=4400)
		def russian():
			global Rus
			Rus = True
			root.destroy()
		def english():
			global Eng
			
			Eng = True
			root.destroy()
			
		Back = Button(root, text='',image=BACK, command=back, borderwidth=0)
		Back.pack()
		Back.place(x=0, y=0)
		Rusi = Button(root, text='',image=RU, command=russian, borderwidth=0)
		Rusi.pack()
		Rusi.place(x=600, y=300)
		Englis = Button(root, text='',image=ENG, command=english, borderwidth=0)
		Englis.pack()
		Englis.place(x=600, y=350)

	def setting():
		pass
	Sett_B = Button(root,  height=88,image=setting_photo, width=596, command=setting, borderwidth=0)
	Sett_B.pack()
	Sett_B.place(x = 450, y=181)
	Lean_P = Button(root,  height=88,image=lean_photo, width=596, command=language,borderwidth=0)
	Lean_P.pack()
	Lean_P.place(x = 450, y=93)
	Play_P = Button(root,  height=88,image=play_photo, width=596, command=Start,borderwidth=0)
	Play_P.pack()
	Play_P.place(x = 450, y=5)
	
	root.mainloop()

lobby_game()
if Eng == True:
	
	
	win = pygame.display.set_mode((display_w + 1, display_h - 55))
	pygame.display.set_caption('game')	
	count = 0
	def background_game():
		win.blit(bggame, (world_rect.x, 185))
	
	i = 0
	Game_cikl = True
	animcount = 0
	xx_value = []
	with open('x.json', 'r')as cordx:
			
		cords = json.load(cordx)
		world_rect.x = cords
	with open('y.json', 'r')as cordy:
		cordy = json.load(cordy)
		playery = cordy
	def random_place():
			
			global count
			if count is 0:
				for i in range(100):
					xx = randint(-2245, 756)
					
					xx_value.append(xx)
				count += 1
	  		
	def treee():
		global count, xx_value
		with open('trees.json', 'w') as trees:
			json.dump(xx_value, trees)
		with open('trees_count.json', 'w') as counts:
			json.dump(count, counts)
		with open('trees.json', 'r') as trees:
			
			
			xx_value.append(json.load(trees))
		with open('trees_count.json', 'r') as counts:
			count = json.load(counts)
	
	if Game_cikl == True:
		for i in range(10**10):
			
			
			fps = int(clock.get_fps())
			font = pygame.font.SysFont(None, 30)
			FPS = font.render(f"FPS: {fps}", True, FPS_COLOR)
			def GAME_FPS():
				win.blit(FPS,(1800,0))
			
			# Очистка экрана
			win.fill(BLACK)
			background_game()
			win.blit(world, (world_rect.x, world_rect.y))
			
			for event in pygame.event.get():
				if event.type is pygame.QUIT:
					Game_cikl = False
			
			if animcount + 1 >= 12:
				animcount = 0
				animcount += 1
			player_hitbox = pygame.Rect(playerx, playery, 30, 58)
			key = pygame.key.get_pressed()
			
			

			
				
			def move():
				global player_hitbox,world_x,world_y, world_rect, player_speed,walkleft,move_count_x_minus,move_count_x_plus,walkright,animcount,playerx, playery, gravity_on, cam
				

				if key[pygame.K_a]:
					if player_hitbox.colliderect(world_rect):
						
						if cam == False:		
							world_rect.x += player_speed
							world_x += player_speed
						move_count_x_minus = False
						move_count_x_plus = True
						if player_jump_power == False:
							win.blit(walkleft[animcount % len(walkleft)], (playerx, playery))
						animcount += 1
					elif not player_hitbox.colliderect(world_rect) and player_jump_power == False:
						win.blit(player_text.player_l, (playerx, playery))
						
						move_count_x_minus = False
						move_count_x_plus = True
					elif not player_hitbox.colliderect(world_rect):
						if cam == False:
							world_rect.x += player_speed
							world_x += player_speed	
				elif key[pygame.K_d]:
					if player_hitbox.colliderect(world_rect):
						if cam == False:
							world_x -= player_speed
							world_rect.x -= player_speed
						move_count_x_minus = True
						move_count_x_plus = False
						if player_jump_power == False:
							win.blit(walkright[animcount % len(walkright)], (playerx, playery))
						animcount += 1
					elif not player_hitbox.colliderect(world_rect) and player_jump_power == False:
						win.blit(player_text.player_r, (playerx, playery))
						
						move_count_x_minus = True
						move_count_x_plus = False
					elif not player_hitbox.colliderect(world_rect):
						if cam == False:	
							world_rect.x -= player_speed
							world_x -= player_speed
							
				
				elif move_count_x_minus == True and move_count_x_plus == False and player_jump_power == False: # right
					win.blit(player_text.player_r, (playerx, playery))
				elif move_count_x_minus == False and move_count_x_plus == True and player_jump_power == False: # left
					win.blit(player_text.player_l, (playerx, playery))
				elif move_count_x_minus == False and move_count_x_plus == False and player_jump_power == False:
					win.blit(player_text.player_r, (playerx, playery))
			def Items():
				if swordT == True:
					win.blit(sword, (27, 3))
			Items()
			def chat():
				def text_chat():
					text = chat_text.get()
					if f'/give jboy1555 sword':
						global swordT
						swordT = True
					
					if '/tp' in text:
						def chat_return():
							codes = Label(root, text='if you want a teleport please write [/tp] dont write a semicolon', bg='black', fg='green')
							codes.pack()
							codes.place(x=0, y=460)
							chat_text = Entry(root, foreground='green', width=750, background='black')
							chat_text.pack()
							chat_text.place(x=0, y=480)
							codes_new.place(x=0, y=4400)
							chat_tpx.place(x=0, y=4800)
							chat_tpy.place(x=0, y=4600)
							chat_back.place(x=2000, y=0)
						def chat_tp():
							global playerx, playery
							text2 = chat_tpx.get()
							text3 = chat_tpy.get()
							
							
							try:	 
								playery = int(text2)
								world_rect.x = int(text3)
								root.destroy()
							except ValueError:
								
								text2 = chat_tpx.delete(0, 'end')
								text3 = chat_tpy.delete(0, 'end')
								
								Error = Label(root, text='ERROR: VE(please write in x and y only numbers)', bg='black', fg='red')
								Error.pack()
								Error.place(x=0, y=400)
								
								
								


					
						
						codes.place(x=0, y=4600)
						chat_text.place(x=0, y=4800)
						text_2 = 'please write cord (first line - x)'
						codes_new = Label(root, text='', bg='black', fg='green')
						codes_new.pack()
						codes_new.place(x=0, y=440)
						def text_22(text_2, speed=50):
							if text_2:
								codes_new.config(text=codes_new.cget('text') + text_2[0])
								root.after(speed, lambda: text_22(text_2[1:], speed))
						text_22(text_2, speed=50)
						
						chat_tpx = Entry(root, foreground='green', width=750, background='black')
						chat_tpx.pack()
						chat_tpx.place(x=0, y=480)
						chat_tpy = Entry(root, foreground='green', width=750, background='black')
						chat_tpy.pack()
						
						chat_Use = Button(root, text="USE-->", foreground='green', bg='black', width=10, height=1, command=chat_tp, font=10)
						chat_Use.pack()
						chat_Use.place(x=380, y=0)
						

						chat_tpy.place(x=0, y=460)
						
						chat_back = Button(root, text="<--BACK", foreground='green', bg='black', width=10, height=1, command=chat_return, font=10)
						chat_back.pack()
						chat_back.place(x=20, y=0)
						chat_enter.place(x=3800, y=0)
					

				

				root = Tk()
				root.geometry('500x500+500+200')
				root.title('admin-chat')
				root.config(bg='black')
				hello_text = "hello it's a admin-chat, in this chat you can a teleport transfo/nrm and e.t.c please use this chat as your wish and good use."
				hello_code = Label(root, text='', bg='black', fg='green')
				hello_code.pack()
				hello_code.place(x=0, y=100)
				def hello(hello_text, speed=75):
					if hello_text:
						hello_code.config(text=hello_code.cget("text")  +  hello_text[0])
						root.after(speed, lambda: hello(hello_text[1:], speed))
				hello(hello_text, speed=75)
				text_codes = 'if you want a teleport please write [/tp] dont write a semicolon'
				codes = Label(root, text='', bg='black', fg='green')
				codes.pack()
				codes.place(x=0, y=460)
				def label_start(text_codes, speed=50):
					if text_codes:
						codes.config(text=codes.cget("text") + text_codes[0])
						root.after(speed, lambda: label_start(text_codes[1:], speed))

				
				
					
				
				label_start(text_codes, speed=50)
				chat_text = Entry(root, foreground='green', width=750, background='black')
				chat_text.pack()
				chat_text.place(x=0, y=480)
				
				
				chat_enter = Button(root, text="OK-->", foreground='green', bg='black', width=10, height=1, command=text_chat, font=10)
				chat_enter.pack()
				chat_enter.place(x=380, y=0)
				



				root.mainloop()
			if key[pygame.K_g]:
				chat()

			def gravity():
				global player_hitbox, world_rect, player_speed, walkleft, move_count_x_minus, move_count_x_plus, walkright, animcount, playerx, playery, gravity_on
				if player_jump_power == False:
					# Проверяем, находится ли нижняя граница игрока ниже верхней границы мира
					if player_hitbox.colliderect(world_rect):
						gravity_on = 0
						playery += gravity_on
						
					else:
						# Если нет, сбрасываем гравитацию
						gravity_on = 20
						playery += gravity_on
				
			def jump():
				global player_jump_power, playerx, playery, player_jump, player_speed, count
				if not player_jump_power:
					player_speed = 5
					if key[pygame.K_SPACE]:
						player_jump_power = True
				elif player_jump_power == True and move_count_x_minus == False and move_count_x_plus == True:
					win.blit(player_text.player_falling_right, (playerx, playery))
					player_speed = 7
					if player_jump >= -player_jump_count:
						if player_jump < 0:
							playery += (player_jump ** 2) / 2
							
						else:
							playery -= (player_jump ** 2) / 2
						player_jump -= 1
					else:
						player_jump_power = False
						player_jump = player_jump_count

				elif player_jump_power == True and move_count_x_minus == True and move_count_x_plus == False:
					win.blit(player_text.player_falling_left, (playerx, playery))
					player_speed = 7
					if player_jump >= -player_jump_count:
						if player_jump < 0:
							playery += (player_jump ** 2) / 2
						
						else:
							playery -= (player_jump ** 2) / 2
						player_jump -= 1
					else:
						player_jump_power = False
						player_jump = player_jump_count
				elif player_jump_power == True and move_count_x_minus == False and move_count_x_plus == False:
					win.blit(player_text.player_falling_left, (playerx, playery))
					player_speed = 7
					if player_jump >= -player_jump_count:
						if player_jump < 0:
							playery += (player_jump ** 2) / 2
							
						else:
							playery -= (player_jump ** 2) / 2
						player_jump -= 1
					else:
						player_jump_power = False
						player_jump = player_jump_count# Отрисовка мира
			
			
			def iny():
				global playerx_inventory, inventory, inventory_use
				win.blit(inventory,(playerx_inventory,0))
				if key[pygame.K_1]:
					win.blit(inventory_use, (25, 0))
				elif key[pygame.K_2]:
					win.blit(inventory_use, (51, 0))
				elif key[pygame.K_3]:
					win.blit(inventory_use, (77, 0))
				elif key[pygame.K_4]:
					win.blit(inventory_use, (103, 0))
				elif key[pygame.K_5]:
					win.blit(inventory_use, (129, 0))
				elif key[pygame.K_6]:
					win.blit(inventory_use, (155, 0))
				elif key[pygame.K_7]:
					win.blit(inventory_use, (181, 0))
				elif key[pygame.K_8]:
					win.blit(inventory_use, (207, 0))
				elif key[pygame.K_9]:
					win.blit(inventory_use, (233, 0))
			
			
			def cam_stop():
				global playerx,right, cam, cam_not_in_radius,world_move,to_use_tel,dont_go,player_speed,left	
				if world_rect.x > -10 or world_rect.x < -1080 and cam_not_in_radius == True:
					
					if key[pygame.K_d]:
						playerx += player_speed
						
					cam = True
				if  world_rect.x < -1080 or world_rect.x > -10 and cam_not_in_radius == True:
					if key[pygame.K_a]:	
						
						playerx -= player_speed
					cam = True
				if world_rect.x > -10:	
					if world_rect.x > -10:
						cam_not_in_radius = True
						cam = True
					
					if playerx > 960:
						cam = False
						cam_not_in_radius = False
						
						playerx = 960
					if  playerx < -6:
						cam_not_in_radius = False
						
					if world_rect.x < -1080:
						
						cam = True
						cam_not_in_radius = True
				if world_rect.x <-1080:
					if world_rect.x <-1080:
						cam_not_in_radius = True
						cam = True
					if playerx < 960:
						cam = False
						cam_not_in_radius =False
						playerx = 960
					if playerx > 1899:
						cam_not_in_radius = False

				
				


				
					

					
					
			iny()
			move()
			jump()
			gravity()
			cam_stop()
			

			with open('x.json', 'w') as cordx:
				json.dump(world_rect.x,cordx)
			with open('y.json', 'w') as cordy:
				json.dump(playery,cordy)
			# pygame.draw.rect(win, (247, 64, 82), world_rect)
			# pygame.draw.rect(win, (247, 64, 82), player_hitbox)
			GAME_FPS()	
			clock.tick(60)
			pygame.display.flip()
			
			

		pygame.quit()
# Создание экземпляра окна Tkinter






