from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen


class BaseScreen(Screen):
    app = ObjectProperty(None)

    def __init__(self, app, **kwargs):
        super(BaseScreen, self).__init__(**kwargs)
        self.app = app
