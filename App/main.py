from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager

sm = ScreenManager()

class MainBox(Screen):
    pass

class LeftMenu(Screen):
    pass

sm.add_widget(MainBox())
sm.add_widget(LeftMenu())

class GTeacherApp(App):
    def build(self):
        return sm

GTeacherApp().run()
