import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

class RootWidget(BoxLayout):

     def __init__(self, **kwargs):
         super(RootWidget, self).__init__(**kwargs)
         self.add_widget(Button(text='btn 1'))
         cb = CustomBtn()
         cb.bind(pressed=self.btn_pressed)
         self.add_widget(cb)
         self.add_widget(Button(text='btn 2'))

     def btn_pressed(self, instance, pos):
         print('pos: printed from root widget: {pos}'.format(pos=pos))

class CustomBtn(Widget):

     pressed = ListProperty([0, 0])

     def on_touch_down(self, touch):
         if self.collide_point(*touch.pos):
             self.pressed = touch.pos
             # we consumed the touch. return False here to propagate
             # the touch further to the children.
             return True
         return super(CustomBtn, self).on_touch_down(touch)

     def on_pressed(self, instance, pos):
         print('pressed at {pos}'.format(pos=pos))

class TestApp(App):

     def build(self):
         return RootWidget()


if __name__ == '__main__':
     TestApp().run()


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)



    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()