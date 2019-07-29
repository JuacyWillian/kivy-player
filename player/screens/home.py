from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import AsyncImage
from kivymd.list import MDList

from .base import BaseScreen

Builder.load_string("""
<ImageButton>:

<HomeScreen>:
    ScrollView:
        id: scroll
        do_scroll_x: False
""")


class ImageButton(ButtonBehavior, AsyncImage):
    pass


class HomeScreen(BaseScreen):
    scroll = ObjectProperty(None)

    def __init__(self, app, **kwargs):
        super(HomeScreen, self).__init__(app, **kwargs)

    def on_pre_enter(self, *args):
        # Deve carregar todas as musicas do banco de dados
        pass
