import kivy

from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.lang import Builder

Builder.load_string('''
# a template Butt of type Button
[Butt@Button]
    # ctx.'attribute_name' is used to access the 
    # attributes defined in the instance of Butt.
    text: ctx.text
    # below vars are constant for every instance of Butt
    size_hint_x: None
    width: 100

<CalcApp>:
    cols: 3
    row_force_default: True
    row_default_height: 50
    pos_hint: {'center_x':.5}
    size_hint: (None, None)
    # size is updated whenever minimum_size is.
    size: self.minimum_size
    # top is updated whenever height is.
    top: self.height
    Label:
        text: "Gender:"
        size_hint_x: None
        width: 100
    Label:
        text: 'Male'
        size_hint_x: None
        width: 100
    CheckBox:
        id: box_male
        active: True
        color: .294, .761, .623
        group: 'g2'
        size_hint_x: None
        width: 100
    Label:
        text: ''
        size_hint_x: None
        width: 100
    Label:
        text: 'Female'
        size_hint_x: None
        width: 100
    CheckBox:
        id: box_female
        active: True
        color: .294, .761, .623
        group: 'g2'
        size_hint_x: None
        width: 100
    Label:
        text: ''
        size_hint_x: None
        width: 100
    Label:
        text: 'Other'
        size_hint_x: None
        width: 100
    CheckBox:
        id: box_other
        active: True
        color: .294, .761, .623
        group: 'g2'
        size_hint_x: None
        width: 100
''')

class CalcApp(App, GridLayout):

    def build(self):
        return self

CalcApp().run()