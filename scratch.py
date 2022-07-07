import kivy

kivy.require("1.9.0")
import importlib

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.uix.widget import Widget
from datetime import datetime
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.behaviors.togglebutton import ToggleButtonBehavior
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
import pandas as pd

Builder.load_file('MyScreenManagerTest.kv')
############################ define global variables and lists ##########################
states = ListProperty()
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC",
          "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA",
          "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN",
          "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM",
          "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI",
          "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA",
          "WV", "WI", "WY"]

cancer_list = ObjectProperty(None)
cancer_list = []
InjuryDict = dict()
InjuryRisk = dict()

########################## define global classes ########################################
class User(object):
    def __init__(self, state="USA", age=None, gender=None, user=None):
        self.state = state
        self.age = age
        self.gender = gender
        self.user = user
        user = (self.state, self.age, self.gender)

    def __str__(self):
        return "User is: %s, %s, %s" % (self.state, self.age, self.gender)


class MyScreenManager(ScreenManager):
    pass

class BRANCH(Screen):
    pass

class MAINGRID(Screen):
    pass

############################# user input data screen ########################################
class INPUTDATA(Screen):
    input_data = ObjectProperty(User)

    def display_state(self):
        self.states = states
        return states

    class CustomWidget(Widget):
        state_spinner = ObjectProperty(None)
        age_input = ObjectProperty(None)
        box_male = ObjectProperty(None)
        box_female = ObjectProperty(None)
        pass

    def send_data(self):
        self.age = 0
        self.user = []
        if self.age_input.text:
            print("Year Born:", self.age_input.text)
            self.age = datetime.now().year - int(self.age_input.text)
        print("Assign age: {}".format(self.age))
        self.gender = ""
        if self.box_male.active:
            print("Gender: Male")
            self.gender = "M"
        elif self.box_female.active:
            print("Gender: Female")
            self.gender = "F"
        else:
            print("No gender selected")
            self.gender = "X"
        if self.state_spinner.text == "Select":
            self.state = "USA"
        else:
            self.state = self.state_spinner.text
        print("State:", self.state)

        self.user = User(self.state, self.age, self.gender)
        input_data = User()
        input_data.state = self.state
        input_data.age = self.age
        input_data.gender = self.gender
        print(input_data)
        return input_data


####################### Injury Class Screen ##########################################

class INJURY(Screen):
    input_data = ObjectProperty(User)

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.user = User()
        self.default_data = User(state="USA", age=35, gender="M")
        print("Default Injury Data: ", self.user.state, self.user.age, self.user.gender)


    def parse_csv(user):
        input_state = INPUTDATA.input_data.state
        print(input_state)
        data_path = "C:\\Users\\gcurtin\\PycharmProjects\\RISKFINDER\\venv\\data\\injurybystate.csv"
        injury_data = pd.read_csv(data_path, names = ['State', 'Choking','Falls','Vehicle','Poisoning','Drowning','Occupational','Firearm','Blunt Force'])
        injuries = list(injury_data)
        injuries.remove('State')

        for row in injury_data.itertuples(index=False, name='Injury'):
            InjuryDict[row[0]] = row

        states = list(InjuryDict.keys())
        states.remove('State')


        def find_risk(val):
            if val < 0.001:
                val = 0.001
            risk_val = (val / 100000)*100
            return round(risk_val,6)

        for i,v in InjuryDict.items():
            print(InjuryDict[i])
            print(find_risk(InjuryDict[i].Choking))
            #print('key:', i, '--> ','value:', v)

        def get_risk():







