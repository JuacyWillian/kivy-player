from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.storage.dictstore import DictStore
from kivy.properties import ObjectProperty
from kivy.uix.image import AsyncImage


class Manager(ScreenManager):
    store = DictStore({})

    def __init__(self, **kwargs):
        super(Manager, self).__init__(**kwargs)

        screen = Screen(name="Home")
        screen.add_widget(AsyncImage(source="assets/logo.png"))
        self.switch_to(screen)


class Player(App):
    title = "Music Player"
    manager = ObjectProperty(None)

    def build(self, ):
        self.manager = Manager()
        return self.manager

    def on_start(self, ): pass
    def on_pause(self, ): pass
    def on_resume(self, ): pass
    def on_stop(self, ): pass

    def goto(self, screen):
        self.manager.switch_to(screen)
