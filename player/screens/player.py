from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.properties import ListProperty

from .base import BaseScreen

Builder.load_string("""
#:import MDLabel kivymd.label
#:import MDIconButton kivymd.button.MDIconButton


<PlayerScreen>:
    BoxLayout
        orientation: "vertical"
        BoxLayout
            MDLabel
                text: "Imagem da Capa do CD"
                halign: 'center'
        BoxLayout
            orientation: "vertical"
            size_hint_y: .3
            MDLabel
                text: "Nothing else matters"
                halign: 'center'
            MDLabel
                text: "Metallica"
                halign: 'center'
        BoxLayout
            size_hint_y: .3
            size_hint_x: None
            width: self.minimum_width
            padding: 10, 10
            spacing: 5, 5
            pos_hint: {'center_x': .5}
            MDIconButton:
                icon: "rewind"
                on_release: root.retroceder()
                size: (dp(48), dp(48))
            MDIconButton:
                icon: "pause" if root.playing else "play"
                size: (dp(64), dp(64))
                on_release: root.tocar_pausar()
            MDIconButton:
                icon: "fast-forward"
                on_release: root.avancar()
                size: (dp(48), dp(48))
""")


class PlayerScreen(BaseScreen):
    playlist = ListProperty([])
    playing = BooleanProperty(False)

    def __init__(self, app, **kwargs):
        self.plalist = kwargs.pop('playlist')
        super(PlayerScreen, self).__init__(app, **kwargs)

    def on_pre_enter(self, *args):
        # Deve carregar a musica e exibir os controles de
        # play, pause, avancar e retroceder
        pass

    def tocar_pausar(self, *args):
        if self.playing:
            pass
        else:
            pass

        self.playing = not self.playing

    def avancar(self, *args):
        pass

    def retroceder(self, *args):
        pass
