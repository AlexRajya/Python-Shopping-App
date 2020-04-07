from APIs import *
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from tescoScreen import tescoWindow
from bbScreen import bbWindow

class Choose(Screen):
    def toTesco(self):
        self.manager.current = "tesco"
    def toBestBuy(self):
        self.manager.current = "bb"

class ShoppingApp(App):
    def build(self):
        manager = ScreenManager()
        
        manager.add_widget(Choose(name='choose'))
        manager.add_widget(tescoWindow(name='tesco'))
        manager.add_widget(bbWindow(name='bb'))
        return manager

    def get_application_config(self):
        if(not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        )

def main():
    kv = Builder.load_file("screens.kv")
    if __name__ == "__main__":
        ShoppingApp().run()
    
def test():
    bb = bbSearch(input("Enter search query(BestBuy): "))
    bb.display()
    tesco = tescoSearch(input("Enter search query(Tesco): "))
    tesco.display()
#start app
main()
choice = input('Enter "run" to start app or "test" to test APIs: ')

if choice == 'run':
    main()
else:
    test()