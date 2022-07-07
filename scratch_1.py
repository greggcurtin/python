from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.boxlayout import BoxLayout
class ScrollButton(Button):
    pass

class CustLabel(Label):
    pass

class CustPBar(ProgressBar):
    pass

class CustBox(BoxLayout):
    pass

class ScrollApp(App):
    def build(self):
        super(ScrollApp, self).build()
        container = self.root.ids.container
        #box = self.root.ids.box
        #box2 = self.root.ids.box2
        for i in range(40):
            container.add_widget(CustLabel(text=str(40-i)))
            container.add_widget(CustPBar(value=40-i))
            #box.add_widget(CustLabel(text="Test2"))
            #box.add_widget(CustPBar(value=15))
        return self.root   # return root does not work

if __name__ == '__main__':
    ScrollApp().run()