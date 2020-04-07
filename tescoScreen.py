from kivy.app import App
from APIs import *
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, SlideTransition

class tescoWindow(Screen):
    resultArea = ObjectProperty(None)
    searchBar = ObjectProperty(None)
    
    def search(self):
        tesco = tescoSearch(self.searchBar.text)
        self.resultArea.text = tesco.formatted