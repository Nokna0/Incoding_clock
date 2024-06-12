import pygame
pygame.init()

width = 1000
height = 1000

screen = pygame.display.set_mode((width, height))

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

running = True
while running:
    # 게임 로직 업데이트
    # 그래픽 업데이트
