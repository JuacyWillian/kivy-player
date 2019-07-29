

from kivy.lang import Builder

from .base import BaseScreen

Builder.load_string("""
<PlayerScreen>:
    FloatLayout:
""")


class PlayerScreen(BaseScreen):
    def __init__(self, app, **kwargs):
        super(PlayerScreen, self).__init__(app, **kwargs)

    def on_pre_enter(self, *args):
        # Deve carregar a musica e exibir os controles de
        # play, pause, avancar e retroceder
        pass
