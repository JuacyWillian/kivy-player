import enum

from .home import HomeScreen as Home
from .library import LibraryScreen as Library


class ScreenType(enum.Enum):
    HOME = Home
    LIBRARY = Library

    def screen(self, app, **kwargs):
        return self.value(app, **kwargs)
