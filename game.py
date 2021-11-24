import pygame

# Initialisation de pygame
pygame.init()

pygame.display.set_caption("BoxedMotion")  # titre de la fenêtre
screen = pygame.display.set_mode((500, 500))  # taille de la fenêtre


# Initialisation des éléments du jeu exemple
background_surface = pygame.Surface((500, 500))
background_surface.fill((10, 10, 10))

block_surface = pygame.Surface((50, 50))
block_surface.fill('Gold')
block_rect = block_surface.get_rect()

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
                x, y = block_rect.topleft
                block_rect.topleft = max(0, x - 50), y
            elif event.key == pygame.K_RIGHT:
                x, y = block_rect.topleft
                block_rect.topleft = min(x + 50, 450), y
            elif event.key == pygame.K_DOWN:
                x, y = block_rect.topleft
                block_rect.topleft = x, min(y + 50, 450)
            elif event.key == pygame.K_UP:
                x, y = block_rect.topleft
                block_rect.topleft = x, max(0, y - 50)

    # Mise à jour de la position du block
    # Rien à faire ici, on a directement modifié cette position ci-dessous

    # On dessine le fond sur l'écran
    screen.blit(background_surface, (0, 0))

    # On dessine le block à la position désirée
    screen.blit(block_surface, block_rect)

    # On rafraîchit l'écran et contrôle la vitesse de la boucle de jeu
    pygame.display.update()
    clock.tick(40)

pygame.quit()
