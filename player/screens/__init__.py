import enum

from .home import HomeScreen as Home


class ScreenType(enum.Enum):
    HOME = Home

    def screen(self, app, **kwargs):
        return self.value(app, **kwargs)
