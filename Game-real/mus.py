import pygame
pygame.init()
for i in range(3):   
    

    

    # Загрузите звуковой файл
    sound = pygame.mixer.Sound('smove.mp3')

    # Установите громкость (от 0.0 до 1.0)
    sound.set_volume(0.20)  # например, установим громкость на 50%

    # Воспроизведение звука
    sound.play()

    # Пауза для воспроизведения звука (для корректного воспроизведения)
    pygame.time.delay(3000) # пять секунд

pygame.quit()
