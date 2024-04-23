import pygame

# Инициализация Pygame
pygame.init()

# Создание экрана
screen = pygame.display.set_mode((800, 600))

# Загрузка изображения с прозрачным фоном
image = pygame.image.load("C:/Users/gagas/OneDrive/Рабочий стол/Game/photo/sun.png").convert_alpha()

# Получение прямоугольника, описывающего изображение
image_rect = image.get_rect()

# Создание поверхности с прозрачным фоном и теми же размерами, что и изображение
transparent_surface = pygame.Surface(image_rect.size, pygame.SRCALPHA)

# Рисование изображения на прозрачной поверхности
transparent_surface.blit(image, (0, 0))

# Создание круглого изображения
radius = min(image_rect.width, image_rect.height) // 2
pygame.draw.circle(transparent_surface, (0, 0, 0, 0), (radius, radius), radius)

# Отображение круглого изображения на экране
screen.blit(transparent_surface, (0, 0))

# Обновление экрана
pygame.display.flip()

# Главный цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Выход из Pygame
pygame.quit()
