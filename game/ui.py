"""Ce module contrôle la logique liée à l'interface utilisateur du jeu."""

import pygame

from . import engine
import config

pygame.init()

clock = pygame.time.Clock()

SCREEN_SIZE = config.BOARD_SIZE * config.BLOCK_SIZE

BACKGROUND_SURFACE = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE))
BACKGROUND_SURFACE.fill(config.BACKGROUND_COLOR)

BLOCK_SURFACE = pygame.Surface((config.BLOCK_SIZE, config.BLOCK_SIZE))
BLOCK_SURFACE.fill(config.BLOCK_COLOR)


def create_app():
    """Crée une nouvelle application."""
    pygame.display.set_caption(config.TITLE)
    pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

    return {
        'gameboard': engine.create_gameboard(),
        'block': BLOCK_SURFACE.get_rect(),
    }


def run(app):
    """Démarre l'interface graphique du jeu et gère la boucle événementielle."""
    app['running'] = True
    while app['running']:
        handle_events(app)
        refresh_screen(app)
    pygame.quit()


def handle_events(app):
    """Gère les événements reçu par l'application."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app['running'] = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                engine.move_left(app['gameboard'])
            elif event.key == pygame.K_RIGHT:
                engine.move_right(app['gameboard'])
            elif event.key == pygame.K_DOWN:
                engine.move_down(app['gameboard'])
            elif event.key == pygame.K_UP:
                engine.move_up(app['gameboard'])


def refresh_screen(app):
    """Mets à jour l'interface utilisation en fonction des mises à jour du back-end"""
    # On déplace le block manipulé par l'utilisateur
    app['block'].topleft = engine.update(app['gameboard'], config.BLOCK_SIZE)

    # On dessine le fond sur l'écran
    screen = pygame.display.get_surface()
    screen.blit(BACKGROUND_SURFACE, (0, 0))

    # On dessine le block
    screen.blit(BLOCK_SURFACE, app['block'])

    # On rafraîchit l'écran et contrôle la vitesse de la boucle de jeu
    pygame.display.update()
    clock.tick(40)
