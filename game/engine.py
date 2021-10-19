import config


def create_gameboard():
    """Crée un nouveau plateau de jeu."""
    return {'block': (0, 0)}


def move_right(board):
    """Déplace le block sur la droite."""
    x, y = board['block']
    board['block'] = min(x + 1, config.BOARD_SIZE - 1), y


def move_left(board):
    """Déplace le block sur la gauche."""
    x, y = board['block']
    board['block'] = max(0, x - 1), y


def move_down(board):
    """Déplace le block vers le bas."""
    x, y = board['block']
    board['block'] = x, min(y + 1, config.BOARD_SIZE - 1)


def move_up(board):
    """Déplace le block vers le haut."""
    x, y = board['block']
    board['block'] = x, max(0, y - 1)


def update(board, block_size):
    """Retourne le bloc déplacé par l'utilisateur."""
    x, y = board['block']
    return x * block_size, y * block_size
