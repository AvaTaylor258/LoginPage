# # Ava Taylor !
#
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

#
# # load the kv file
# Builder.load_file("QuizPage.kv")
#
# class LoginPageApp(App):
#     def build(self):
#         return QuizManager()
#
# class QuizManager(ScreenManager):
#     pass
#
# class Question1Screen(Screen):
#     def answer_question(self, bool):
#         if bool:
#             self.manager.current = "correct"
#         else:
#             self.manager.current = "error"
#
# class CorrectScreen(Screen):
#     def answer_question(self):
#         self.manager.current = "text input"
#
# class ErrorScreen(Screen):
#     pass
#
# class TextInputScreen(Screen):
#     def answer_question(self, text):
#         if text.lower() == "deep in the heart of texas":
#             self.manager.current = "correct"
#         else:
#             self.ids.invalid_guess.text = "Invalid guess.\nTry again!"
#             self.ids.invalid_guess.color = "red"
#
#
#
# LoginPageApp().run()

creds_dict: {}

Builder.load_file("LoginPage.kv")

class LoginPageApp(App):
    def build(self):
        return LoginManager()

class LoginManager(ScreenManager):
    pass


class LoginPage(Screen):
    def verify_creds(self, username, password):
        if username in creds_dict and password == creds_dict["username"]:
            self.manager.current = "welcome"
        else:
            self.ids.invalid_creds_label.text = "Invalid Credentials"
            # make text red


class WelcomePage(Screen):
    pass


LoginPageApp().run()