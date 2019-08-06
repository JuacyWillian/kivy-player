import threading

from kivy import Logger
from kivymd.button import MDIconButton
from kivymd.label import MDLabel
from kivymd.list import *

from player.screens.base import BaseScreen

Builder.load_string("""
#:import MDLabel kivymd.label.MDLabel

<MusicItem>:
    text: self.item[0].capitalize()
    secondary_text: self.item[1].capitalize()
    
    on_release: app.goto(ScreenType.PLAYER, playlist=[self.item])
    
    ItemOptions:
        icon: 'dots-vertical'
        on_release: root.show_options()

<LibraryScreen>:
    ScrollView:
        do_scroll_x: False
        MDList:
            id: music_list
""")


class ItemOptions(IRightBodyTouch, MDIconButton):
    pass


class ItemAvatar(ILeftBody, MDLabel):
    pass


class MusicItem(TwoLineRightIconListItem):
    item = ObjectProperty(None)

    def __init__(self, item, **kwargs):
        self.item = item
        super(MusicItem, self).__init__(**kwargs)

    @property
    def sign(self):
        words = self.item[0].split(" ")
        if len(words) > 1:
            return "".join([l[0] for l in words]).upper()
        return words[0:2].upper()

    def show_options(self):
        Logger.info(f"TODO: show item options")


class LibraryScreen(BaseScreen):
    library = ObjectProperty(None)
    music_list = ObjectProperty(None)

    def __init__(self, app, **kwargs):
        self.library = app.library
        super(LibraryScreen, self).__init__(app, **kwargs)

    def on_pre_enter(self, *args):
        self.music_list = self.ids.music_list

    def on_enter(self, *args):
        self.load_library()

    def on_pre_leave(self, *args): pass

    def on_leave(self, *args): pass

    def load_library(self):
        def add_tracks():
            for track in self.library.load_musics():
                self.music_list.add_widget(MusicItem(track))

        # Clock.schedule_once(add_tracks)
        threading.Thread(target=add_tracks).start()
