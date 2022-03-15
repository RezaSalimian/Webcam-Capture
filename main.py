from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,screen
from kivy.lang import Builder
Builder.load_file('frontend.kv')

class RootWidge(ScreenManager):
    pass
class MainApp(App):
    def build(self):
        return RootWidget()

MainApp().run()