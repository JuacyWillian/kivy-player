from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import AsyncImage

from .base import BaseScreen

Builder.load_string("""
<ImageButton>:

<SettingScreen>:
    ScrollView:
        id: scroll
        do_scroll_x: False
""")


class ImageButton(ButtonBehavior, AsyncImage):
    pass


class SettingScreen(BaseScreen):
    scroll = ObjectProperty(None)

    def __init__(self, app, **kwargs):
        super(SettingScreen, self).__init__(app, **kwargs)
