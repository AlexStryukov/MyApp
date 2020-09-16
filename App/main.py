from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Main_Box(BoxLayout):
    pass

class GTeacherApp(App):
    def build(self):
        return Main_Box()

GTeacherApp().run()
