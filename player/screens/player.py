from random import randint

from kivy import Logger
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.properties import ListProperty
from kivy.properties import NumericProperty
from kivy.properties import OptionProperty
from kivymd.toolbar import MDToolbar

from .base import BaseScreen

Builder.load_string("""
#:import MDLabel kivymd.label
#:import MDIconButton kivymd.button.MDIconButton
#:import MDCard kivymd.cards.MDCard

<ControlBar@BoxLayout>:
    orientation: 'horizontal'
    size_hint_y: .3
    size_hint_x: None
    width: self.minimum_width
    padding: 10, 10
    spacing: 10
    pos_hint: {'center_x': .5}

<PlayerScreen>:
    MDCard:
        size_hint: .98, .98
        pos_hint: {'center_x': .5, 'center_y': .5}
        BoxLayout:
            orientation: "vertical"
            BoxLayout:
                AsyncImage:
                    source: 'assets/cover.jpg'
            BoxLayout:
                orientation: "vertical"
                size_hint_y: .3
                MDLabel:
                    text: root.playlist[root.current][0]
                    halign: 'center'
                MDLabel:
                    text: root.playlist[root.current][1]
                    halign: 'center'
            ControlBar:
                MDIconButton:
                    icon: root.repeat
                    font_size: 16
                    on_release: root.choice_repeat()
                    size: (dp(44), dp(44))
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
                MDIconButton:
                    icon: "shuffle" if root._shuffle else "shuffle-disabled"
                    on_release: root.on_shuffle()
                    size: (dp(44), dp(44))
""")


class PlayerScreen(BaseScreen):
    playlist = ListProperty([])
    playing = BooleanProperty(False)
    current = NumericProperty(0)
    _shuffle = BooleanProperty(False)
    repeat = OptionProperty(
        "repeat-off", options=["repeat-off", "repeat-once", "repeat"])

    def __init__(self, app, **kwargs):
        self.playlist = kwargs.pop('playlist')
        super(PlayerScreen, self).__init__(app, **kwargs)

    def on_pre_enter(self, *args):
        # Deve carregar a musica e exibir os controles de
        # play, pause, avancar e retroceder
        self.update_toolbar()

    def update_toolbar(self, ):
        """Atualiza a toolbar."""
        tb: MDToolbar = self.app.toolbar
        tb.right_action_items = [
            ['heart-outline', self.set_favourite],
        ]

    def set_favourite(self, *args):
        """Marca a musica como favorita."""
        Logger.info("Player: set favorite")

    def tocar_pausar(self, track=None):
        """Toca ou pausa a musica atual."""
        if track: pass

        if self.playing:
            pass
        else:
            pass
        self.playing = not self.playing

    def avancar(self):
        """Avanca pra proxima musica da lista de reprodução."""
        if self.repeat == "repeat":
            if self._shuffle:
                self.current = randint(0, len(self.playlist))
            else:
                self.current += 1

            if self.current == len(self.playlist):
                if self.repeat == "repeat-all":
                    self.current = 0

        self.tocar_pausar(self.current)

    def retroceder(self, *args):
        """Toca a musica anterior, da lista de reprodução."""
        pass

    def choice_repeat(self, *args):
        """Muda a forma de repetição."""
        if self.repeat == "repeat-off":
            self.repeat = "repeat-once"
        elif self.repeat == "repeat-once":
            self.repeat = "repeat"
        else:
            self.repeat = "repeat-off"

    def on_shuffle(self, *args):
        self._shuffle = not self._shuffle
