import pygame
clock = pygame.time.Clock()
from PIL import Image, ImageGrab
run = True
while run:
    clock.tick(19)
    img = ImageGrab.grab((0,0,526,526))
    img.save("C:/Users/Dedus/OneDrive/Рабочий стол/testn17/screen.jpg", "BMP")
    clock.tick(8)
