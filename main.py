from __future__ import unicode_literals
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import youtube_dl

def idk(instance):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([text.text])





text =TextInput(text="paste your link and wait for about 10 seconds and then search .mp4 in your computer and you should have it and also dont forget to delete this text before pasting")
btn = Button(text="convert to MP4")
btn.bind(on_press=idk)

class youtump4(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        screen = Screen()
        screen.add_widget(box)
        box.add_widget(text)
        box.add_widget(btn)
        return screen


youtump4().run()
