import enum

from .home import HomeScreen as Home
from .library import LibraryScreen as Library
from .player import PlayerScreen as Player
from .settings import SettingScreen as Settings


class ScreenType(enum.Enum):
    """ Enum contendo todas as opcoes de telas do applicativo.
        Ele é usado para a troca de telas de forma simples.
        Por exemplo, para executar a troca de telas para o Home,
        é só chamar self.app.goto(ScreenType.HOME)
    """
    HOME = Home
    LIBRARY = Library
    PLAYER = Player
    SETTINGS = Settings

    def screen(self, app, **kwargs):
        return self.value(app, **kwargs)
