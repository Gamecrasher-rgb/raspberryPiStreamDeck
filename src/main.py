from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '1080')

class MainWindow(Widget):
    pass


class streamApp(App):
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    streamApp().run()