from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MyApp(App):

  def build(self):
    layout = BoxLayout(orientation='vertical')
    
    label_1 = Label(text='Hello World')
    label_2 = Label(text='This is never Hellow World')

    button = Button(text='Press Me')

    layout.add_widget(label_1)
    layout.add_widget(label_2)
    layout.add_widget(button)
    
    return layout;

if __name__ == '__main__':
  MyApp().run()

