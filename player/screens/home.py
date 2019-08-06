from kivy.lang import Builder
from kivy.properties import ObjectProperty

from .base import BaseScreen

Builder.load_string("""
#:import MDRectangleFlatIconButton kivymd.button.MDRectangleFlatIconButton


<HomeScreen>:
    ScrollView:
        id: scroll
        do_scroll_x: False

        GridLayout:
            cols: 2
            padding: 10, 10
            # size_hint: 1, None
            # height: self.minimum_height
            spacing: 5, 5
            pos_hint: {"center_x": .5, "center_y": .5}

            MDRectangleFlatIconButton:
                icon: 'home'
                text: 'Home'
                on_release: app.goto(ScreenType.HOME)

            MDRectangleFlatIconButton:
                icon: 'library-music'
                text: 'Library'
                on_release: app.goto(ScreenType.LIBRARY)

            MDRectangleFlatIconButton:
                icon: 'playlist-music'
                text: 'Playlists'
                # on_release: app.goto(ScreenType.PLAYLISTS)

            MDRectangleFlatIconButton:
                icon: 'heart'
                text: 'Favourites'
                # on_release: app.goto(ScreenType.FAVOURITES)

            MDRectangleFlatIconButton:
                icon: 'settings'
                text: 'Preferences'
                on_release: app.goto(ScreenType.SETTINGS)  

            MDRectangleFlatIconButton:
                icon: 'exit-to-app'
                text: 'Exit'
                on_release: app.stop()
""")


class HomeScreen(BaseScreen):
    scroll = ObjectProperty(None)

    def __init__(self, app, **kwargs):
        super(HomeScreen, self).__init__(app, **kwargs)

    def on_pre_enter(self, *args):
        # Deve carregar todas as musicas do banco de dados
        pass

    def on_enter(self, *args):
        # Evento chamado quando a tela está abrindo.
        pass
