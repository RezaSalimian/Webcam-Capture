from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
import time
from fileShare import FileSharer
from kivy.core.clipboard import Clipboard
import webbrowser
Builder.load_file('frontend.kv')

class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.camera_button.text ='Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture
    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = 'Start Camera'
        self.ids.camera.texture =None
    def capture(self):
        strtime = time.strftime('%Y%m%d-%H%M%S')
        self.filename = "files/"+strtime + ".png"
        self.ids.camera.export_to_png(self.filename)
        self.manager.current='image_screen'
        self.manager.current_screen.ids.img.source=self.filename

class ImageScreen(Screen):
    def create_link(self):
        file_path=App.get_running_app().root.ids.camera_screen.filename
        filesharer=FileSharer(filepath=file_path)
        self.url=filesharer.share()
        self.ids.link.text=self.url
    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text="Create a link first"

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text="Create a link first"



class RootWidget(ScreenManager):
    pass
class MainApp(App):
    def build(self):
        return RootWidget()

MainApp().run()