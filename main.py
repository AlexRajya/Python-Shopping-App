from APIs import *
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

def test():
    bb = bbSearch(input("Enter search query(BestBuy): "))
    bb.display()
    tesco = tescoSearch(input("Enter search query(Tesco): "))
    tesco.display()

class MainWindow(Screen):
    resultArea = ObjectProperty(None)
    searchBar = ObjectProperty(None)
    
    def search(self):
        tesco = tescoSearch(self.searchBar.text)
        self.resultArea.text = tesco.formatted

class WindowManager(ScreenManager):
    pass

def main():
    class MyMainApp(App):
        def build(self):
            return sm
    kv = Builder.load_file("my.kv")
    sm = WindowManager()
    
    screens = [MainWindow(name="main")]
    for screen in screens:
        sm.add_widget(screen)
    
    sm.current = "main"
    if __name__ == "__main__":
        MyMainApp().run()

#start app
choice = input('Enter "run" to start app or "test" to test APIs: ')
if choice == 'run':
    main()
else:
    test()