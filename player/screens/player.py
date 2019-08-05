from kivy.lang import Builder

from .base import BaseScreen

Builder.load_string("""
#:import MDLabel kivymd.label

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
            Button
                text: "Voltar"
            Button
                text: "Play/Pause"
            Button
                text: "Avançar"
""")


class PlayerScreen(BaseScreen):
    def __init__(self, app, **kwargs):
        super(PlayerScreen, self).__init__(app, **kwargs)

    def on_pre_enter(self, *args):
        # Deve carregar a musica e exibir os controles de
        # play, pause, avancar e retroceder
        pass
