"""Lancement du jeu."""

from . import ui


def main():
    """Point d'entrée principal du jeu."""
    app = ui.create_app()
    ui.run(app)


if __name__ == "__main__":
    main()
