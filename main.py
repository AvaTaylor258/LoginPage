# Ava Taylor

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# load the kv file
Builder.load_file("LoginPage.kv")

class LoginPageApp(App):
    def build(self):
        return QuizManager()

class QuizManager(ScreenManager):
    pass

class Question1Screen(Screen):
    def answer_question(self, bool):
        if bool:
            self.manager.current = "correct"
        else:
            self.manager.current = "error"

class CorrectScreen(Screen):
    def answer_question(self):
        self.manager.current = "text input"

class ErrorScreen(Screen):
    pass

class TextInputScreen(Screen):
    def answer_question(self, thing):
        self.manager.current = thing



LoginPageApp().run()