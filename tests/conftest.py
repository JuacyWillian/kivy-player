import pytest

from kivy.clock import Clock


@pytest.fixture
def app():
    from player import PlayerApp
    app = PlayerApp()
    Clock.schedule_interval(lambda *x: app.stop(), 0.000001)
    app.run()

    yield app
