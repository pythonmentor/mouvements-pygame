import pygame

# Initialisation de pygame
pygame.init()

pygame.display.set_caption("BoxedMotion")
screen = pygame.display.set_mode((500, 500))


# Initialisation des éléments du jeu exemple
background_surface = pygame.Surface((500, 500))
background_surface.fill((10, 10, 10))

block_surface = pygame.Surface((500, 500))
block_surface.fill('Gold')
block_rect = block_surface.get_rect()
block_position = (0, 0)

clock = pygame.time.Clock()


# Démarrage de la boucle de jeu
running = True
while running:

    # Gestion des événements clavier et on réagit aux appuis sur les flèches
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x, y = block_position
                block_position = max(0, x - 1), y
            elif event.key == pygame.K_RIGHT:
                x, y = block_position
                block_position = min(x + 1, 49), y
            elif event.key == pygame.K_DOWN:
                x, y = block_position
                block_position = x, min(y + 1, 49)
            elif event.key == pygame.K_UP:
                x, y = block_position
                block_position = x, max(0, y - 1)

    # On déplace le block manipulé par l'utilisateur
    x, y = block_position
    block_rect.topleft = x * 50, y * 50

    # On dessine le fond sur l'écran
    screen.blit(background_surface, (0, 0))

    # On dessine le block à la position désirée
    screen.blit(block_surface, block_rect)

    # On rafraîchit l'écran et contrôle la vitesse de la boucle de jeu
    pygame.display.update()
    clock.tick(40)

pygame.quit()