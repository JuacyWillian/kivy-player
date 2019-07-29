from kivy import Logger
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager
from kivymd.theming import ThemeManager

from player.screens import ScreenType


class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super(Manager, self).__init__(**kwargs)


class Player(App):
    title = "Music Player"
    manager = ObjectProperty(None)
    theme_cls = ThemeManager()
    theme_cls.primary_palette = "Indigo"

    music_root_directory = StringProperty("")

    def build(self, ):
        self.manager = Manager()
        return self.manager

    def on_start(self, ):
        self.goto(ScreenType.HOME)

    def on_pause(self, ): pass

    def on_resume(self, ): pass

    def on_stop(self, ): pass

    def goto(self, screen_type, **kwargs):
        self.manager.switch_to(screen_type.screen(self, **kwargs))

    def update_library(self): pass

    def choose_root_directory(self, ):
        # TODO: show popup for choose music_root_directory
        Logger.info("APP: choose_root_directory")
