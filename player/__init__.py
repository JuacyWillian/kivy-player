from kivy import Logger
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivymd.theming import ThemeManager

from player.classes.library import Library
from player.screens import ScreenType


class PlayerApp(App):
    title = "Music Player"
    theme_cls = ThemeManager()
    theme_cls.primary_palette = "Indigo"

    library = Library()
    music_root_directory = StringProperty("")

    manager = ObjectProperty(None)
    toolbar = ObjectProperty(None)

    def build(self, ):
        self.manager = self.root.ids.manager
        self.toolbar = self.root.ids.toolbar
        return self.root

    def on_start(self, ):
        """Ação executada quando o app é iniciado."""
        self.goto(ScreenType.HOME)

    def on_pause(self, ):
        """Ação executada quando o app é paudado."""
        pass

    def on_resume(self, ):
        """Ação executada quando o app é retomado."""
        pass

    def on_stop(self, ):
        """Ação executada quando o app é finalizado."""
        pass

    def goto(self, screen_type, **kwargs):
        self.manager.switch_to(screen_type.screen(self, **kwargs))

    def update_library(self):
        pass

    def choose_root_directory(self, ):
        """Exibe o dialogo para escolha dos diretórios de musicas."""
        # TODO: show popup for choose music_root_directory
        Logger.info("APP: choose_root_directory")
