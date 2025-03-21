import pygame

print('setup Start')
pygame.init()
window = pygame.display.set_mode(size = (600, 480))
print('setup End')

print('Loop Start')
while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('quiti...')
            pygame.quit() # Clse windom
            quit() # End pygame
