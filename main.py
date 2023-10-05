# # Ava Taylor
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

users = {
    "user": "pass"
}

Builder.load_file("LoginPage.kv")


class LoginPageApp(App):
    def build(self):
        return LoginManager()


class LoginManager(ScreenManager):
    pass


class LoginPage(Screen):
    def verify_creds(self, username, password):
        if password == users[username]:
            self.manager.current = "welcome"
        else:
            self.ids.invalid_creds_label.text = "Invalid Credentials"
            self.ids.invalid_creds_label.color = "red"

    def go_to_register(self):
        self.manager.current = "register"


class WelcomePage(Screen):
    def go2login(self):
        self.manager.current = "login"


class RegisterPage(Screen):
    def verify_new_user(self, username, password, password2):
        og_username = False
        same_passwords = False
        uppercase_in_pass = False
        lowercase_in_pass = False
        number_in_pass = False
        special_in_pass = False
        pass_len = False
        if username not in users:
            og_username = True
        if password == password2:
            same_passwords = True
        for i in "ABCDEFGHIJKLMNOPQRSTUVWXY":
            if i in password:
                uppercase_in_pass = True
                break
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i in password:
                lowercase_in_pass = True
                break
        for i in "1234567890":
            if i in password:
                number_in_pass = True
                break
        for i in "~!@#$%^&*()?":
            if i in password:
                special_in_pass = True
                break
        if len(password) >= 8:
            pass_len = True
        if og_username and same_passwords and uppercase_in_pass and lowercase_in_pass and number_in_pass and special_in_pass and pass_len:
            users[username] = password
            self.manager.current = "login"
        else:
            self.ids.lol_thing.text = "Username Already Taken\nor\nInvalid Password(s)"
            self.ids.lol_thing.color = "red"


LoginPageApp().run()
