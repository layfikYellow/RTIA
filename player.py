import pygame

sc = pygame.display.set_mode((526,526),pygame.RESIZABLE)
clock = pygame.time.Clock()
bg = pygame.image.load("screen.jpg")

run = True

while run:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()

    clock.tick(19)
    bg = pygame.image.load("screen.jpg")
    pygame.display.update()
    sc.blit(bg,(0,0))
    bg = 1
    clock.tick(8)
