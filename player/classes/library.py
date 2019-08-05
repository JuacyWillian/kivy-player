from kivy.app import App
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.properties import ListProperty

musics = [
    ("ATRASADINHA  FEAT. FERRUGEM", "Felipe Araújo"),
    ("ZÉ DA RECAÍDA", "Gusttavo Lima"),
    ("SÓ PRA CASTIGAR", "Wesley Safadão"),
    ("SOFAZINHO  PT. JORGE E MATEUS", "Luan Santana"),
    ("NÃO FALA NÃO PRA MIM  FEAT. JERRY SMITH", "Humberto e Ronaldo"),
    ("NOTIFICAÇÃO PREFERIDA", "Zé Neto e Cristiano"),
    ("QUEM PEGOU, PEGOU", "Henrique e Julian"),
    ("QUEM ME DERA  FEAT. JERRY SMITH", "Márcia Fellipe"),
    ("OLHA ELA AÍ", "Eduardo Costa"),
    ("CIUMEIRA", "Marília Mendonça"),
    ("BEIJO DE VARANDA", "Bruno e Marrone"),
]


class Library(EventDispatcher):
    """Responsavel pelo gerenciamento das midias de audio."""
    musics = ListProperty([])
    playlists = ListProperty([])
    artists = ListProperty([])
    albuns = ListProperty([])

    def __init__(self, **kwargs):
        super(Library, self).__init__(**kwargs)
        self.load_musics()

    def load_musics(self):
        """Carrega os arquivos de audio."""
        for m in musics:
            self.musics.append(m)

    def load_artists(self):
        """Carrega os artistas."""
        pass

    def load_playlists(self):
        """Carrega as listas de repodução salvas."""
        pass

    def load_albuns(self):
        """Carrega os albuns."""
        pass

    def sync_library(self):
        """Sincroniza os arquivos de audio com a biblioteca."""
        Clock.shedule_once(self.verify_dirs, 0)

    def scan_directories(self):
        """Escaneia os diretorios de audio, em busca de mudancas."""
        dirs = App.get_running_app().settings.music_root_dirs
        for dir in dirs:
            pass
