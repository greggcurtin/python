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

Builder.load_file('MyScreenManagerBAK1004.kv')
user = None

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


def get_cancer_defaults():
    data_path = "C:\\Users\\gcurtin\\PycharmProjects\\RISKFINDER\\venv\\data\\CancerbyAge_Male_Death.csv"
    cancer_data = pd.read_csv(data_path)
    for index, row in cancer_data.iterrows():
        data_row = (row['Type'], row['35'])
        cancer_list.append(data_row)
    return cancer_list


class User(object):
    def __init__(self, state="USA", age=None, gender=None, user=None):
        self.state = state
        self.age = age
        self.gender = gender
        self.user = user
        user = (state, age, gender)

    def __str__(self):
        return "User is: %s, %s, %s" % (self.state, self.age, self.gender)


class MyScreenManager(ScreenManager):
    pass


# Branch Screen, takes you to S1, S2, or S3
class BRANCH(Screen):
    pass


class MAINGRID(Screen):
    pass


class INPUTDATA(Screen):
    user = ObjectProperty(None)

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
        User.user = self.user
        # print(self.user)
        print(User.user)


class S3(Screen):
    pass
class DEATH(Screen):
    pass


class INJURY(Screen):
    value_array = ObjectProperty(None)
    value_array = []

    def parse_csv(user):
        data_path = "C:\\Users\\gcurtin\\PycharmProjects\\RISKFINDER\\venv\\data\\injurybystate.csv"
        injury_data = pd.read_csv(data_path)

        choking_data = []
        falls_data = []
        motor_data = []
        poison_data = []
        fire_data = []
        occ_data = []
        heat_data = []
        blunt_data = []
        firearm_data = []
        drown_data = []

        st = User.user.state
        print("State is: ", st)

        def find_risk(val):
            if val < 0.01:
                val = 0.01
            risk_val = (val / 100000) * 100
            return risk_val

        ############INJURY DATA PARSE########################
        for index, row in injury_data.iterrows():
            choking_row = (row['State'], row['Choking'])
            choking_data.append(choking_row)

        for index, row in injury_data.iterrows():
            falls_row = (row['State'], row['Falls'])
            falls_data.append(falls_row)

        for index, row in injury_data.iterrows():
            motor_row = (row['State'], row['Vehicle'])
            motor_data.append(motor_row)

        for index, row in injury_data.iterrows():
            poison_row = (row['State'], row['Poisoning'])
            poison_data.append(poison_row)

        for index, row in injury_data.iterrows():
            fire_row = (row['State'], row['FireSmoke'])
            fire_data.append(fire_row)

        for index, row in injury_data.iterrows():
            occ_row = (row['State'], row['Occupational'])
            occ_data.append(occ_row)

        for index, row in injury_data.iterrows():
            heat_row = (row['State'], row['HeatCold'])
            heat_data.append(heat_row)

        for index, row in injury_data.iterrows():
            blunt_row = (row['State'], row['BluntForce'])
            blunt_data.append(blunt_row)

        for index, row in injury_data.iterrows():
            firearm_row = (row['State'], row['Firearm'])
            firearm_data.append(firearm_row)

        for index, row in injury_data.iterrows():
            drown_row = (row['State'], row['Drowning'])
            drown_data.append(drown_row)

        ChokingDict = dict(choking_data)
        FallsDict = dict(falls_data)
        MotorDict = dict(motor_data)
        PoisonDict = dict(poison_data)
        FireDict = dict(fire_data)
        OccDict = dict(occ_data)
        HeatDict = dict(heat_data)
        BluntDict = dict(blunt_data)
        FirearmDict = dict(firearm_data)
        DrownDict = dict(drown_data)

        choking_risk = round(find_risk(ChokingDict.get(st)), 6)
        falls_risk = round(find_risk(FallsDict.get(st)), 6)
        motor_risk = round(find_risk(MotorDict.get(st)), 6)
        poison_risk = round(find_risk(PoisonDict.get(st)), 6)
        fire_risk = round(find_risk(FireDict.get(st)), 6)
        occ_risk = round(find_risk(OccDict.get(st)), 6)
        heat_risk = round(find_risk(HeatDict.get(st)), 6)
        blunt_risk = round(find_risk(BluntDict.get(st)), 6)
        firearm_risk = round(find_risk(FirearmDict.get(st)), 6)
        drown_risk = round(find_risk(DrownDict.get(st)), 6)

        print("Choking Risk: ", choking_risk)
        print("Falls Risk: ", falls_risk)
        print("Motor Vehicle Risk: ", motor_risk)
        print("Poison Risk: ", poison_risk)
        print("Fire Risk: ", fire_risk)
        print("Occupation Risk: ", occ_risk)
        print("Heat/Cold Risk: ", heat_risk)
        print("Blunt Force Risk: ", blunt_risk)
        print("Firearm Risk: ", firearm_risk)
        print("Drowning Risk: ", drown_risk)

        value_array = [choking_risk, falls_risk, motor_risk, poison_risk, fire_risk, occ_risk, heat_risk, blunt_risk,
                       firearm_risk, drown_risk]
        return value_array

    def update(user):
        value_array = user.parse_csv()
        print(value_array)
        user.ids.choking.value = value_array[0]
        user.ids.falls.value = value_array[1]
        user.ids.motor.value = value_array[2]
        user.ids.poison.value = value_array[3]
        user.ids.fire.value = value_array[4]
        user.ids.occ.value = value_array[5]
        user.ids.heat.value = value_array[6]
        user.ids.blunt.value = value_array[7]
        user.ids.firearm.value = value_array[8]
        user.ids.drown.value = value_array[9]
    def default(user):
        user.ids.choking.value = 0.0016
        user.ids.falls.value = 0.0112
        user.ids.motor.value = 0.0124
        user.ids.poison.value = 0.0199
        user.ids.fire.value = 0.00112
        user.ids.occ.value = 0.0035
        user.ids.heat.value = 0.00039
        user.ids.blunt.value = 0.000176
        user.ids.firearm.value = 0.0118
        user.ids.drown.value = 0.00114


class CANCER(Screen):
    cancer_list = ObjectProperty(None)
    cancer_list = []
    user = User()
    title = ObjectProperty(Label)
    version = ObjectProperty(StringProperty)
    customflag = ObjectProperty(StringProperty)

    ############CANCER DATA PARSE########################
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.user = User()
        self.user = User(state="USA", age=35, gender="M")
        self.version = 0
        self.customflag = 0
        print("Default Cancer User: ", self.user.state, self.user.age, self.user.gender)
        CANCER.cancer_list = cancer_list

    @classmethod
    def parse_csv(user, version, customflag):
        if version==0:
            if (User.user.gender == "M" or User.user.gender == "X"):
                data_path = "C:\\Users\\gcurtin\\PycharmProjects\\RISKFINDER\\venv\\data\\CancerbyAge_Male_Death.csv"
            if (User.user.gender == "F"):
                data_path = "C:\\Users\\gcurtin\\PycharmProjects\\RISKFINDER\\venv\\data\\CancerbyAge_Female_Death.csv"
        if version==1:
            if (User.user.gender == "M" or User.user.gender == "X"):
                data_path = "C:\\Users\\gcurtin\\PycharmProjects\\RISKFINDER\\venv\\data\\CancerbyAge_Male_Diagnosis.csv"
            if (User.user.gender == "F"):
                data_path = "C:\\Users\\gcurtin\\PycharmProjects\\RISKFINDER\\venv\\data\\CancerbyAge_Female_Diagnosis.csv"

        cancer_data = pd.read_csv(data_path)

        cancer_rows = {}
        cancer_rows.clear()
        cancer_tuples = []

        if customflag == 0:
            st = "USA"
            age = 35
        if customflag == 1:
            st = User.user.state
            age = User.user.age
        print("State is: ", st)
        print("Age is: ", age)

        def myround(x, base=5):
            if x < 20:
                x = 20
            if x > 75:
                x = 75
            return int(base * round(float(x) / base))

        rounded_age = myround(age)
        print("age is ", age, "rounded to ", myround(age))

        for index, row in cancer_data.iterrows():
            data_row = (row['Type'], row[str(rounded_age)])
            cancer_rows[str(rounded_age)] = data_row
            cancer_tuples.append(cancer_rows[str(rounded_age)])

        #print("CSV Cancer Tuples: ", cancer_tuples)
        cancer_list = [[i for i, j in cancer_tuples], [j for i, j in cancer_tuples]]
        print("CSV Cancer List: ", cancer_list)

        return cancer_list

    @classmethod
    def update(user, version, customflag, *args):
        print("Average" if customflag==0 else "Custom")
        print("Death Rate" if version==0 else "Diagnosis Rate")
        if version == 0:
            user.cancer_list2 = user.parse_csv(version=0, customflag=customflag)
            print("Death Update:", user.cancer_list2[1])
        if version==1:
            user.cancer_list2 = user.parse_csv(version=1, customflag=customflag)
            print("Diagnosis Update:", user.cancer_list2[1])


class MyWidget(GridLayout, Label): #BoxLayout, Label):
    box = ObjectProperty(None)
    cancer_list = ListProperty(None)
    pb = ObjectProperty(None)
    calc = ObjectProperty(Button)

    def __init__(self, *args, **kwargs):
        super(MyWidget, self).__init__(*args, **kwargs)
        self.cancer_list = cancer_list


Factory.register('MyWidget', cls=MyWidget)


class FINAL_SCREEN(Screen):
    previous = StringProperty()
    def update(user, *args):
        user.pbval = 20
    def default(user, *args):
        user.pbval = 50


class CustLabel(Widget):
    lb = ObjectProperty()
    texture = ObjectProperty(Label)

    def __init__(self, *kwargs):
        super(CustLabel, self).__init__(**kwargs)
        self.lb = Label()
        self.size = self.texture_size
        self.font_size: 12
        self.color = [1, 1, 1, 1]


class CustPBar(Widget):
    pb = ObjectProperty()

    def __init__(self, *kwargs):
        super(CustPBar, self).__init__(**kwargs)
        self.pb = ProgressBar()
        self.size_hint_x = .9
        self.height = '48dp'
        self.max: 100


class MAINApp(App):
    def build(self):
        get_cancer_defaults()
        return MyScreenManager()


if __name__ == '__main__':
    MAINApp().run()