from kivy.app import App
from APIs import *
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, SlideTransition

class bbWindow(Screen):
    resultArea = ObjectProperty(None)
    searchBar = ObjectProperty(None)
    
    def search(self):
        bb = bbSearch(self.searchBar.text)
        self.resultArea.text = bb.formatted
        
    def back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "choose"