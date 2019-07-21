import pytest

from kivy.clock import Clock


@pytest.fixture
def app():
    from player import Player
    app = Player()
    Clock.schedule_interval(lambda *x: app.stop(), 0.000001)
    app.run()

    yield app
