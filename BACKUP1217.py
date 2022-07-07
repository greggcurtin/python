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
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.behaviors.togglebutton import ToggleButtonBehavior
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
import pandas as pd
import math

Builder.load_file('MyScreenManagerTest.kv')
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
disease_list = ObjectProperty(None)
disease_list = []
cause_list = ObjectProperty(None)
cause_list = []


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
        self.age = 999
        self.user = []
        if self.age_input.text.isdigit():
            print("Year Born:", self.age_input.text)
            self.age = datetime.now().year - int(self.age_input.text)
        else:
            print("Not a valid age. Using Average.")
            self.age = 999
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
        age = User.user.age
        print("State is: ", st)
        print("Age is: ", age)


        def find_lifetime(val):
            age = User.user.age
            if (User.user.age > 78) and (User.user.age < 999):
                age = 78
            if User.user.age < 1:
                age = 1
            exp = (0-((val/100000)*(78.6-age)))
            lifetime_risk = (1-math.exp(exp))*100
            return lifetime_risk

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


        choking_lifetime = round(find_lifetime(ChokingDict.get(st)), 3)
        falls_lifetime = round(find_lifetime(FallsDict.get(st)), 3)
        motor_lifetime = round(find_lifetime(MotorDict.get(st)), 3)
        poison_lifetime = round(find_lifetime(PoisonDict.get(st)), 3)
        fire_lifetime = round(find_lifetime(FireDict.get(st)), 3)
        occ_lifetime = round(find_lifetime(OccDict.get(st)), 3)
        heat_lifetime = round(find_lifetime(HeatDict.get(st)), 3)
        blunt_lifetime = round(find_lifetime(BluntDict.get(st)), 3)
        firearm_lifetime = round(find_lifetime(FirearmDict.get(st)), 3)
        drown_lifetime = round(find_lifetime(DrownDict.get(st)), 3)

        lifetime_array = [choking_lifetime, falls_lifetime, motor_lifetime, poison_lifetime, fire_lifetime, occ_lifetime, heat_lifetime, blunt_lifetime,
                       firearm_lifetime, drown_lifetime]

        return lifetime_array

    def update(user):
        print("user", str(user))
        lifetime_array = user.parse_csv()
        print(lifetime_array)
        user.ids.choking.value = lifetime_array[0]
        user.ids.falls.value = lifetime_array[1]
        user.ids.motor.value = lifetime_array[2]
        user.ids.poison.value = lifetime_array[3]
        user.ids.fire.value = lifetime_array[4]
        user.ids.occ.value = lifetime_array[5]
        user.ids.heat.value = lifetime_array[6]
        user.ids.blunt.value = lifetime_array[7]
        user.ids.firearm.value = lifetime_array[8]
        user.ids.drown.value = lifetime_array[9]
    def default(user):
        user.ids.choking.value = 0.0559
        user.ids.falls.value = 0.3912
        user.ids.motor.value = 0.433
        user.ids.poison.value = 0.6940
        user.ids.fire.value = 0.0392
        user.ids.occ.value = 0.1224
        user.ids.heat.value = 0.0136
        user.ids.blunt.value = 0.0062
        user.ids.firearm.value = 0.412
        user.ids.drown.value = 0.0399


class CANCER(Screen):
    cancer_list = ObjectProperty(None)
    cancer_list = []
    user = User()
    title = ObjectProperty(Label)
    version = ObjectProperty(StringProperty)
    customflag = ObjectProperty(StringProperty)


    ############CANCER DATA PARSE########################
    def __init__(self, *args, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.user = User()
        self.user = User(state="USA", age=999, gender="M")
        self.version = 0
        self.customflag = 0
        print("Default Cancer User: ", self.user.state, self.user.age, self.user.gender)
        self.cancer_list = cancer_list

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
        rounded_age = 999

        def myround(x, base=5):
            if x < 20:
                x = 20
            elif (x > 75) and (x < 999):
                x = 75
            return int(base * round(float(x) / base))

        if customflag == 0:
            st = "USA"
            age = 999 #average column
            rounded_age = 999

        if customflag == 1:
            st = User.user.state
            age = User.user.age
            print("State is: ", st)
            print("Age is: ", age)
            if age != 999:
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


class CancerWidget(BoxLayout, Label, Widget):
    box = ObjectProperty(None)
    cancer_list = ListProperty(None)

    def __init__(self, *args, **kwargs):
        super(CancerWidget, self).__init__(*args, **kwargs)
        self.cancer_list = cancer_list


    def update(user, version, customflag, *args):
        print("Average" if customflag == 0 else "Custom")
        print("Death Rate" if version == 0 else "Diagnosis Rate")
        if version == 0:
            user.cancer_list2 = CANCER.parse_csv(version=0, customflag=customflag)
            print("Death Update:", user.cancer_list2[1])
        if version == 1:
            user.cancer_list2 = CANCER.parse_csv(version=1, customflag=customflag)
            print("Diagnosis Update:", user.cancer_list2[1])

        user.pb.value = round(user.cancer_list2[1][0]*100,8)
        user.pb1.value = round(user.cancer_list2[1][1]*100,8)
        user.pb2.value = round(user.cancer_list2[1][2] * 100, 8)
        user.pb3.value = round(user.cancer_list2[1][3]*100,8)
        user.pb4.value = round(user.cancer_list2[1][4]*100,8)
        user.pb5.value = round(user.cancer_list2[1][5]*100,8)
        user.pb6.value = round(user.cancer_list2[1][6]*100,8)
        user.pb7.value = round(user.cancer_list2[1][7]*100,8)
        user.pb8.value = round(user.cancer_list2[1][8] * 100, 8)
        user.pb9.value = round(user.cancer_list2[1][9]*100,8)
        user.pb10.value = round(user.cancer_list2[1][10]*100,8)
        user.pb11.value = round(user.cancer_list2[1][11]*100,8)
        user.pb12.value = round(user.cancer_list2[1][12]*100,8)
        user.pb13.value = round(user.cancer_list2[1][13]*100,8)
        user.pb14.value = round(user.cancer_list2[1][14] * 100, 8)
        user.pb15.value = round(user.cancer_list2[1][15]*100,8)
        user.pb16.value = round(user.cancer_list2[1][16]*100,8)
        user.pb17.value = round(user.cancer_list2[1][17]*100,8)
        user.pb18.value = round(user.cancer_list2[1][18]*100,8)
        user.pb19.value = round(user.cancer_list2[1][19]*100,8)
        user.pb20.value = round(user.cancer_list2[1][20]*100,8)
        user.pb21.value = round(user.cancer_list2[1][21] * 100, 8)
        user.pb22.value = round(user.cancer_list2[1][22]*100,8)
        user.pb23.value = round(user.cancer_list2[1][23]*100,8)
        user.pb24.value = round(user.cancer_list2[1][24]*100,8)
        user.pb25.value = round(user.cancer_list2[1][25] * 100, 8)
        user.pb26.value = round(user.cancer_list2[1][26]*100,8)
        user.lb.text = '{}: {}%'.format(user.cancer_list2[0][0], float(user.pb.value))
        user.lb1.text = '{}: {}%'.format(user.cancer_list2[0][1], float(user.pb1.value))
        user.lb2.text = '{}: {}%'.format(user.cancer_list2[0][2], float(user.pb2.value))
        user.lb3.text = '{}: {}%'.format(user.cancer_list2[0][3], float(user.pb3.value))
        user.lb4.text = '{}: {}%'.format(user.cancer_list2[0][4], float(user.pb4.value))
        user.lb5.text = '{}: {}%'.format(user.cancer_list2[0][5], float(user.pb5.value))
        user.lb6.text = '{}: {}%'.format(user.cancer_list2[0][6], float(user.pb6.value))
        user.lb7.text = '{}: {}%'.format(user.cancer_list2[0][7], float(user.pb7.value))
        user.lb8.text = '{}: {}%'.format(user.cancer_list2[0][8], float(user.pb8.value))
        user.lb9.text = '{}: {}%'.format(user.cancer_list2[0][9], float(user.pb9.value))
        user.lb10.text = '{}: {}%'.format(user.cancer_list2[0][10], float(user.pb10.value))
        user.lb11.text = '{}: {}%'.format(user.cancer_list2[0][11], float(user.pb11.value))
        user.lb12.text = '{}: {}%'.format(user.cancer_list2[0][12], float(user.pb12.value))
        user.lb13.text = '{}: {}%'.format(user.cancer_list2[0][13], float(user.pb13.value))
        user.lb14.text = '{}: {}%'.format(user.cancer_list2[0][14], float(user.pb14.value))
        user.lb15.text = '{}: {}%'.format(user.cancer_list2[0][15], float(user.pb15.value))
        user.lb16.text = '{}: {}%'.format(user.cancer_list2[0][16], float(user.pb16.value))
        user.lb17.text = '{}: {}%'.format(user.cancer_list2[0][17], float(user.pb17.value))
        user.lb18.text = '{}: {}%'.format(user.cancer_list2[0][18], float(user.pb18.value))
        user.lb19.text = '{}: {}%'.format(user.cancer_list2[0][19], float(user.pb19.value))
        user.lb20.text = '{}: {}%'.format(user.cancer_list2[0][20], float(user.pb20.value))
        user.lb21.text = '{}: {}%'.format(user.cancer_list2[0][21], float(user.pb21.value))
        user.lb22.text = '{}: {}%'.format(user.cancer_list2[0][22], float(user.pb22.value))
        user.lb23.text = '{}: {}%'.format(user.cancer_list2[0][23], float(user.pb23.value))
        user.lb24.text = '{}: {}%'.format(user.cancer_list2[0][24], float(user.pb24.value))
        user.lb25.text = '{}: {}%'.format(user.cancer_list2[0][25], float(user.pb25.value))
        user.lb26.text = '{}: {}%'.format(user.cancer_list2[0][26], float(user.pb26.value))

Factory.register('CancerWidget', cls=CancerWidget)

class DISEASE(Screen):
    disease_list = ObjectProperty(None)
    disease_list = []
    user = User()
    title = ObjectProperty(Label)
    version = ObjectProperty(StringProperty)
    customflag = ObjectProperty(StringProperty)


    ############CANCER DATA PARSE########################
    def __init__(self, *args, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.user = User()
        self.user = User(state="USA", age=999, gender="M")
        self.customflag = 0
        print("Default Disease User: ", self.user.state, self.user.age, self.user.gender)
        self.disease_list = disease_list

    @classmethod
    def parse_csv(user, customflag):
        data_path = "C:\\Users\\gcurtin\\PycharmProjects\\RISKFINDER\\venv\\data\\diseaseriskbyage.csv"

        disease_data = pd.read_csv(data_path, encoding = 'latin1')

        disease_rows = {}
        disease_rows.clear()
        disease_tuples = []
        rounded_age = 999
        def myround(x):
            if x < 3:
                x = 1
            elif (x >= 3) and (x < 10):
                x = 4
            elif (x >= 10) and (x < 20):
                x = 14
            elif (x >= 20) and (x < 30):
                x = 24
            elif (x >= 30) and (x < 50):
                x = 39
            elif (x >= 50) and (x < 70):
                x = 64
            elif (x >= 70) and (x < 999):
                x = 78
            elif (x == 999):
                x = 999
            return x

        if customflag == 0:
            st = "USA"
            age = 999 #average column
            rounded_age = 999

        if customflag == 1:
            age = User.user.age
            print("Age is: ", age)
            rounded_age = myround(age)
            print("age is ", age, "rounded to ", myround(age))

        for index, row in disease_data.iterrows():
            data_row = (row['Type'], row[str(rounded_age)])
            disease_rows[str(rounded_age)] = data_row
            disease_tuples.append(disease_rows[str(rounded_age)])

        disease_list = [[i for i, j in disease_tuples], [j for i, j in disease_tuples]]
        print("CSV Disease List: ", disease_list)

        return disease_list

class DiseaseWidget(BoxLayout, Label, Widget):
    def __init__(self, *args, **kwargs):
        super(DiseaseWidget, self).__init__(*args, **kwargs)
        self.disease_list = disease_list

    def update(user, customflag, *args):
        print("Average" if customflag == 0 else "Custom")
        print("Diagnosis Rate")
        user.disease_list = DISEASE.parse_csv(customflag=customflag)
        print("Disease Diagnosis Update:", user.disease_list)
        user.pb.value = round(user.disease_list[1][0],4)
        user.pb1.value = round(user.disease_list[1][1],4)
        user.pb2.value = round(user.disease_list[1][2],4)
        user.pb3.value = round(user.disease_list[1][3],4)
        user.pb4.value = round(user.disease_list[1][4],4)
        user.pb5.value = round(user.disease_list[1][5],4)
        user.pb6.value = round(user.disease_list[1][6],4)
        user.pb7.value = round(user.disease_list[1][7],4)
        user.pb8.value = round(user.disease_list[1][8],4)
        user.pb9.value = round(user.disease_list[1][9],4)
        user.pb10.value = round(user.disease_list[1][10],4)
        user.pb11.value = round(user.disease_list[1][11],4)
        user.pb12.value = round(user.disease_list[1][12],4)
        user.pb13.value = round(user.disease_list[1][13],4)
        user.pb14.value = round(user.disease_list[1][14],4)
        user.pb15.value = round(user.disease_list[1][15],4)
        user.pb16.value = round(user.disease_list[1][16],4)
        user.pb17.value = round(user.disease_list[1][17],4)
        user.pb18.value = round(user.disease_list[1][18],4)
        user.pb19.value = round(user.disease_list[1][19],4)
        user.pb20.value = round(user.disease_list[1][20],4)
        user.pb21.value = round(user.disease_list[1][21],4)
        user.pb22.value = round(user.disease_list[1][22],4)
        user.pb23.value = round(user.disease_list[1][23],4)
        user.pb24.value = round(user.disease_list[1][24],4)
        user.pb25.value = round(user.disease_list[1][25],4)
        user.pb26.value = round(user.disease_list[1][26],4)
        user.pb27.value = round(user.disease_list[1][27],4)
        user.pb28.value = round(user.disease_list[1][28],4)
        user.pb29.value = round(user.disease_list[1][29],4)
        user.pb30.value = round(user.disease_list[1][30],4)
        user.pb31.value = round(user.disease_list[1][31],4)
        user.pb32.value = round(user.disease_list[1][32],4)
        user.pb33.value = round(user.disease_list[1][33],4)
        user.pb34.value = round(user.disease_list[1][34],4)
        user.pb35.value = round(user.disease_list[1][35],4)
        user.pb36.value = round(user.disease_list[1][36],4)
        user.lb.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][0], pb=float(user.pb.value) if user.pb.value != 0 else "NA")
        user.lb1.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][1], pb=float(user.pb1.value) if user.pb1.value != 0 else "NA")
        user.lb2.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][2], pb=float(user.pb2.value) if user.pb2.value != 0 else "NA")
        user.lb3.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][3], pb=float(user.pb3.value) if user.pb3.value != 0 else "NA")
        user.lb4.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][4], pb=float(user.pb4.value) if user.pb4.value != 0 else "NA")
        user.lb5.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][5], pb=float(user.pb5.value) if user.pb5.value != 0 else "NA")
        user.lb6.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][6], pb=float(user.pb6.value) if user.pb6.value != 0 else "NA")
        user.lb7.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][7], pb=float(user.pb7.value) if user.pb7.value != 0 else "NA")
        user.lb8.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][8], pb=float(user.pb8.value) if user.pb8.value != 0 else "NA")
        user.lb9.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][9], pb=float(user.pb9.value) if user.pb9.value != 0 else "NA")
        user.lb10.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][10], pb=float(user.pb10.value) if user.pb10.value != 0 else "NA")
        user.lb11.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][11], pb=float(user.pb11.value) if user.pb11.value != 0 else "NA")
        user.lb12.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][12], pb=float(user.pb12.value) if user.pb12.value != 0 else "NA")
        user.lb13.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][13], pb=float(user.pb13.value) if user.pb13.value != 0 else "NA")
        user.lb14.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][14], pb=float(user.pb14.value) if user.pb14.value != 0 else "NA")
        user.lb15.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][15], pb=float(user.pb15.value) if user.pb15.value != 0 else "NA")
        user.lb16.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][16], pb=float(user.pb16.value) if user.pb16.value != 0 else "NA")
        user.lb17.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][17], pb=float(user.pb17.value) if user.pb17.value != 0 else "NA")
        user.lb18.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][18], pb=float(user.pb18.value) if user.pb18.value != 0 else "NA")
        user.lb19.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][19], pb=float(user.pb19.value) if user.pb19.value != 0 else "NA")
        user.lb20.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][20], pb=float(user.pb20.value) if user.pb20.value != 0 else "NA")
        user.lb21.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][21], pb=float(user.pb21.value) if user.pb21.value != 0 else "NA")
        user.lb22.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][22], pb=float(user.pb22.value) if user.pb22.value != 0 else "NA")
        user.lb23.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][23], pb=float(user.pb23.value) if user.pb23.value != 0 else "NA")
        user.lb24.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][24], pb=float(user.pb24.value) if user.pb24.value != 0 else "NA")
        user.lb25.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][25], pb=float(user.pb25.value) if user.pb25.value != 0 else "NA")
        user.lb26.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][26], pb=float(user.pb26.value) if user.pb26.value != 0 else "NA")
        user.lb27.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][27], pb=float(user.pb27.value) if user.pb27.value != 0 else "NA")
        user.lb28.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][28], pb=float(user.pb28.value) if user.pb28.value != 0 else "NA")
        user.lb29.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][29], pb=float(user.pb29.value) if user.pb29.value != 0 else "NA")
        user.lb30.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][30], pb=float(user.pb30.value) if user.pb30.value != 0 else "NA")
        user.lb31.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][31], pb=float(user.pb31.value) if user.pb31.value != 0 else "NA")
        user.lb32.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][32], pb=float(user.pb32.value) if user.pb32.value != 0 else "NA")
        user.lb33.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][33], pb=float(user.pb33.value) if user.pb33.value != 0 else "NA")
        user.lb34.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][34], pb=float(user.pb34.value) if user.pb34.value != 0 else "NA")
        user.lb35.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][35], pb=float(user.pb35.value) if user.pb35.value != 0 else "NA")
        user.lb36.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][36], pb=float(user.pb36.value) if user.pb36.value != 0 else "NA")


class NCD(Screen):
    disease_list = ObjectProperty(None)
    disease_list = []
    user = User()
    title = ObjectProperty(Label)
    version = ObjectProperty(StringProperty)
    customflag = ObjectProperty(StringProperty)


    ############NCD DATA PARSE########################
    def __init__(self, *args, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.user = User()
        self.user = User(state="USA", age=999, gender="M")
        self.customflag = 0
        print("Default NCD User: ", self.user.state, self.user.age, self.user.gender)
        self.disease_list = disease_list

    @classmethod
    def parse_csv(user, customflag):
        if (User.user.gender == "M" or User.user.gender == "X"):
            data_path = "C:\\Users\\gcurtin\\PycharmProjects\\RISKFINDER\\venv\\data\\NCD_male_risk.csv"
        if (User.user.gender == "F"):
            data_path = "C:\\Users\\gcurtin\\PycharmProjects\\RISKFINDER\\venv\\data\\NCD_female_risk.csv"

        disease_data = pd.read_csv(data_path, encoding = 'latin1')

        disease_rows = {}
        disease_rows.clear()
        disease_tuples = []
        rounded_age = 999
        def myround(x):
            if x <= 5:
                x = 5
            elif (x >= 5) and (x < 14):
                x = 10
            elif (x >= 15) and (x < 19):
                x = 17
            elif (x >= 19) and (x < 24):
                x = 22
            elif (x >= 24) and (x < 30):
                x = 27
            elif (x >= 30) and (x < 34):
                x = 32
            elif (x >= 34) and (x < 39):
                x = 37
            elif (x >= 39) and (x < 44):
                x = 42
            elif (x >= 44) and (x < 49):
                x = 47
            elif (x >= 49) and (x < 54):
                x = 52
            elif (x >= 54) and (x < 59):
                x = 57
            elif (x >= 59) and (x < 64):
                x = 62
            elif (x >= 64) and (x < 69):
                x = 67
            elif (x >= 69) and (x < 999):
                x = 72
            elif (x == 999):
                x = 999
            return x

        if customflag == 0:
            st = "USA"
            age = 999 #average column
            rounded_age = 999

        if customflag == 1:
            age = User.user.age
            print("Age is: ", age)
            rounded_age = myround(age)
            print("age is ", age, "rounded to ", myround(age))

        for index, row in disease_data.iterrows():
            data_row = (row['Type'], row[str(rounded_age)])
            disease_rows[str(rounded_age)] = data_row
            disease_tuples.append(disease_rows[str(rounded_age)])

        disease_list = [[i for i, j in disease_tuples], [j for i, j in disease_tuples]]
        print("CSV NCD List: ", disease_list)

        return disease_list

class NCDWidget(BoxLayout, Label, Widget):
    def __init__(self, *args, **kwargs):
        super(NCDWidget, self).__init__(*args, **kwargs)
        self.disease_list = disease_list

    def update(user, customflag, *args):
        print("Average" if customflag == 0 else "Custom")
        print("Diagnosis Rate")
        user.disease_list = NCD.parse_csv(customflag=customflag)
        print("NCD Diagnosis Update:", user.disease_list)
        user.pb.value = round(user.disease_list[1][0],4)
        user.pb1.value = round(user.disease_list[1][1],4)
        user.pb2.value = round(user.disease_list[1][2],4)
        user.pb3.value = round(user.disease_list[1][3],4)
        user.pb4.value = round(user.disease_list[1][4],4)
        user.pb5.value = round(user.disease_list[1][5],4)
        user.pb6.value = round(user.disease_list[1][6],4)
        user.pb7.value = round(user.disease_list[1][7],4)
        user.pb8.value = round(user.disease_list[1][8],4)
        user.pb9.value = round(user.disease_list[1][9],4)
        user.pb10.value = round(user.disease_list[1][10],4)
        user.pb11.value = round(user.disease_list[1][11],4)
        user.pb12.value = round(user.disease_list[1][12],4)
        user.pb13.value = round(user.disease_list[1][13],4)
        user.pb14.value = round(user.disease_list[1][14],4)
        user.pb15.value = round(user.disease_list[1][15],4)
        user.pb16.value = round(user.disease_list[1][16],4)
        user.pb17.value = round(user.disease_list[1][17],4)
        user.pb18.value = round(user.disease_list[1][18],4)
        user.pb19.value = round(user.disease_list[1][19],4)
        user.pb20.value = round(user.disease_list[1][20],4)
        user.pb21.value = round(user.disease_list[1][21],4)
        user.pb22.value = round(user.disease_list[1][22],4)
        user.pb23.value = round(user.disease_list[1][23],4)
        user.pb24.value = round(user.disease_list[1][24],4)
        user.pb25.value = round(user.disease_list[1][25],4)
        user.pb26.value = round(user.disease_list[1][26],4)
        user.pb27.value = round(user.disease_list[1][27],4)
        user.pb28.value = round(user.disease_list[1][28],4)
        user.pb29.value = round(user.disease_list[1][29],4)
        user.pb30.value = round(user.disease_list[1][30],4)
        user.pb31.value = round(user.disease_list[1][31],4)
        user.pb32.value = round(user.disease_list[1][32],4)
        user.lb.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][0], pb=float(user.pb.value) if user.pb.value != 0 else "NA")
        user.lb1.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][1], pb=float(user.pb1.value) if user.pb1.value != 0 else "NA")
        user.lb2.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][2], pb=float(user.pb2.value) if user.pb2.value != 0 else "NA")
        user.lb3.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][3], pb=float(user.pb3.value) if user.pb3.value != 0 else "NA")
        user.lb4.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][4], pb=float(user.pb4.value) if user.pb4.value != 0 else "NA")
        user.lb5.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][5], pb=float(user.pb5.value) if user.pb5.value != 0 else "NA")
        user.lb6.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][6], pb=float(user.pb6.value) if user.pb6.value != 0 else "NA")
        user.lb7.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][7], pb=float(user.pb7.value) if user.pb7.value != 0 else "NA")
        user.lb8.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][8], pb=float(user.pb8.value) if user.pb8.value != 0 else "NA")
        user.lb9.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][9], pb=float(user.pb9.value) if user.pb9.value != 0 else "NA")
        user.lb10.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][10], pb=float(user.pb10.value) if user.pb10.value != 0 else "NA")
        user.lb11.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][11], pb=float(user.pb11.value) if user.pb11.value != 0 else "NA")
        user.lb12.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][12], pb=float(user.pb12.value) if user.pb12.value != 0 else "NA")
        user.lb13.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][13], pb=float(user.pb13.value) if user.pb13.value != 0 else "NA")
        user.lb14.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][14], pb=float(user.pb14.value) if user.pb14.value != 0 else "NA")
        user.lb15.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][15], pb=float(user.pb15.value) if user.pb15.value != 0 else "NA")
        user.lb16.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][16], pb=float(user.pb16.value) if user.pb16.value != 0 else "NA")
        user.lb17.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][17], pb=float(user.pb17.value) if user.pb17.value != 0 else "NA")
        user.lb18.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][18], pb=float(user.pb18.value) if user.pb18.value != 0 else "NA")
        user.lb19.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][19], pb=float(user.pb19.value) if user.pb19.value != 0 else "NA")
        user.lb20.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][20], pb=float(user.pb20.value) if user.pb20.value != 0 else "NA")
        user.lb21.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][21], pb=float(user.pb21.value) if user.pb21.value != 0 else "NA")
        user.lb22.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][22], pb=float(user.pb22.value) if user.pb22.value != 0 else "NA")
        user.lb23.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][23], pb=float(user.pb23.value) if user.pb23.value != 0 else "NA")
        user.lb24.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][24], pb=float(user.pb24.value) if user.pb24.value != 0 else "NA")
        user.lb25.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][25], pb=float(user.pb25.value) if user.pb25.value != 0 else "NA")
        user.lb26.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][26], pb=float(user.pb26.value) if user.pb26.value != 0 else "NA")
        user.lb27.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][27], pb=float(user.pb27.value) if user.pb27.value != 0 else "NA")
        user.lb28.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][28], pb=float(user.pb28.value) if user.pb28.value != 0 else "NA")
        user.lb29.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][29], pb=float(user.pb29.value) if user.pb29.value != 0 else "NA")
        user.lb30.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][30], pb=float(user.pb30.value) if user.pb30.value != 0 else "NA")
        user.lb31.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][31], pb=float(user.pb31.value) if user.pb31.value != 0 else "NA")
        user.lb32.text = '{lb}: {pb}%'.format(lb=user.disease_list[0][32], pb=float(user.pb32.value) if user.pb32.value != 0 else "NA")

###########COD######################

class COD(Screen):
    cause_list = ObjectProperty(None)
    cause_list = []
    user = User()
    title = ObjectProperty(Label)
    version = ObjectProperty(StringProperty)
    customflag = ObjectProperty(StringProperty)

###########COD DATA PARSE######################
    def __init__(self, *args, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.user = User()
        self.user = User(state="USA", age=999, gender="M")
        self.customflag = 0
        print("Default COD User: ", self.user.state, self.user.age, self.user.gender)
        self.cause_list = cause_list

    @classmethod
    def parse_csv(user, customflag):

        data_path = "C:\\Users\\gcurtin\\PycharmProjects\\RISKFINDER\\venv\\data\\causeofdeath.csv"
        cause_data = pd.read_csv(data_path, encoding = 'latin1', header=0)

        cause_rows = {}
        cause_list = []
        cause_names = []
        cause_rates = []
        cause_rows.clear()
        cause_tuples = []
        rounded_age = 999

        def myround(x):
            if x <= 1:
                x = 1
            elif (x > 1) and (x <= 4):
                x = 4
            elif (x > 4) and (x <= 9):
                x = 9
            elif (x > 9) and (x <= 14):
                x = 14
            elif (x > 14) and (x <= 19):
                x = 19
            elif (x > 19) and (x <= 24):
                x = 24
            elif (x > 24) and (x <= 34):
                x = 34
            elif (x > 34) and (x <= 44):
                x = 44
            elif (x > 44) and (x <= 54):
                x = 54
            elif (x > 54) and (x <= 64):
                x = 64
            elif (x > 64) and (x <= 74):
                x = 74
            elif (x > 74) and (x <= 84):
                x = 84
            elif (x > 84) and (x <= 998):
                x = 998
            elif (x == 999):
                x = 999
            return x

        def find_risk(val, age):
            if val > 0.0001:
                exp = (0 - ((val / 100000) * (78.6 - age)))
                lifetime_risk = (1 - math.exp(exp)) * 100
                #lifetime_risk = (val/100000)*100
            else:
                lifetime_risk = 0.0


            return lifetime_risk

        if customflag == 0:
            st = "USA"
            age = 999 #average column
            rounded_age = 999

            # for index, row in cause_data.iterrows():
            #      data_row = (row['State'], row['Limit'], row['COD'], row['Crude Rate'])
            #      if row['State'] == str(st):
            #          cause_list.append(data_row)

        if customflag == 1:
            st = "CO"
            if User.user.state != "USA":
                st = User.user.state
            age = User.user.age
            print("Age is: ", age)
            rounded_age = myround(age)
            print("age is ", age, "rounded to ", myround(age))
            print("st is ", st)


        for index, row in cause_data.iterrows():
            data_row = (row['State'], row['Limit'], row['COD'], row['Crude Rate'])
            if row['Limit'] == rounded_age and row['State'] == str(st):
                tmplist = list(data_row)
                if rounded_age != 999:
                    tmplist[3] = round(find_risk(float(tmplist[3]),rounded_age),6)
                else:
                    tmplist[3] = round(find_risk(float(tmplist[3]),35.5),6)
                tmptpl = tuple(tmplist)
                #cause_list.append(data_row)
                cause_tuples.append(tmptpl)

        for state, limit, cod, rate in cause_tuples:
            cause_names.append(cod)
            cause_rates.append(rate)
        cause_list = [cause_names, cause_rates]
        #cause_dict = dict(cause_list.row['COD'], cause_list.row['Crude Rate'])

                #cause_tuples.append(cause_rows[row['Limit']])
            #cause_tuples.append(cause_rows([str(rounded_age)]))

        #cause_list = cause_tuples

        print("Cause Data")
        print(cause_data)
        print("cause_tuples")
        print(cause_tuples)
        #print("cause_tuples select")
        #print(cause_tuples[0][1], cause_tuples[0][2], cause_tuples[0][3])
        #print(cause_tuples[1][1], cause_tuples[1][2], cause_tuples[1][3])
        #print("cause list")
        print("cause list", cause_list)




        #for index, row in disease_data.iterrows():
        #    data_row = (row['Type'], row[str(rounded_age)])
        #    disease_rows[str(rounded_age)] = data_row
        #    disease_tuples.append(disease_rows[str(rounded_age)])

        #disease_list = [[i for i, j in disease_tuples], [j for i, j in disease_tuples]]
        #print("CSV NCD List: ", disease_list)

        return cause_list

class CODWidget(BoxLayout, Label, Widget):
    def __init__(self, *args, **kwargs):
        super(CODWidget, self).__init__(*args, **kwargs)
        self.cause_list = cause_list

    def update(user, customflag, *args):
        print("Average" if customflag == 0 else "Custom")
        user.cause_list = COD.parse_csv(customflag=customflag)
        print("COD Update:", user.cause_list)
        print("length (0):", len(user.cause_list[0]))
        print("length (1):", len(user.cause_list[1]))
        pblist = (user.pb, user.pb1, user.pb2, user.pb3, user.pb4, user.pb5, user.pb6, user.pb7, user.pb8, user.pb9, user.pb10, user.pb11, user.pb12, user.pb13, user.pb14, user.pb15, user.pb16, user.pb17, user.pb18, user.pb19)
        lblist = (user.lb, user.lb1, user.lb2, user.lb3, user.lb4, user.lb5, user.lb6, user.lb7, user.lb8, user.lb9, user.lb10, user.lb11, user.lb12, user.lb13, user.lb14, user.lb15, user.lb16, user.lb17, user.lb18, user.lb19)
        for i in range(len(user.cause_list[0])):
            pblist[i].value = round(user.cause_list[1][i],4)
            lblist[i].text = '{lb}: {pb}%'.format(lb=user.cause_list[0][i], pb=float(pblist[i].value) if pblist[i].value != 0.000 else "NA")
        for i in range(len(user.cause_list[0]), 20):
            print("i", i, "lb",str(lblist[i].text))
            if customflag == 1:
                pblist[i].value = 0.0
                lblist[i].text = 'NA'


        # user.pb1.value = round(user.cause_list[1][1],4)
        # user.pb2.value = round(user.cause_list[1][2],4)
        # user.pb3.value = round(user.cause_list[1][3],4)
        # user.pb4.value = round(user.cause_list[1][4],4)
        # user.pb5.value = round(user.cause_list[1][5],4)
        # user.pb6.value = round(user.cause_list[1][6],4)
        # user.pb7.value = round(user.cause_list[1][7],4)
        # user.pb8.value = round(user.cause_list[1][8],4)
        # user.pb9.value = round(user.cause_list[1][9],4)
        # user.pb10.value = round(user.cause_list[1][10],4)
        # user.pb11.value = round(user.cause_list[1][11],4)
        # user.pb12.value = round(user.cause_list[1][12],4)
        # user.pb13.value = round(user.cause_list[1][13],4)
        # user.pb14.value = round(user.cause_list[1][14],4)
        # user.pb15.value = round(user.cause_list[1][15],4)
        # user.pb16.value = round(user.cause_list[1][16],4)
        # user.pb17.value = round(user.cause_list[1][17],4)
        # user.pb18.value = round(user.cause_list[1][18],4)
        # user.pb19.value = round(user.cause_list[1][19],4)
        # user.pb20.value = round(user.cause_list[1][20],4)
        # user.pb21.value = round(user.cause_list[1][21],4)
        # user.pb22.value = round(user.cause_list[1][22],4)
        # user.pb23.value = round(user.cause_list[1][23],4)
        # user.pb24.value = round(user.cause_list[1][24],4)
        # user.pb25.value = round(user.cause_list[1][25],4)
        # user.pb26.value = round(user.cause_list[1][26],4)
        # user.pb27.value = round(user.cause_list[1][27],4)
        # user.pb28.value = round(user.cause_list[1][28],4)
        # user.pb29.value = round(user.cause_list[1][29],4)
        # user.pb30.value = round(user.cause_list[1][30],4)
        # user.pb31.value = round(user.cause_list[1][31],4)
        # user.pb32.value = round(user.cause_list[1][32],4)
        # user.lb.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][0], pb=float(user.pb.value) if user.pb.value != 0.000 else "NA")
        # user.lb1.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][1], pb=float(user.pb1.value) if user.pb1.value != 0.000 else "NA")
        # user.lb2.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][2], pb=float(user.pb2.value) if user.pb2.value != 0.000 else "NA")
        # user.lb3.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][3], pb=float(user.pb3.value) if user.pb3.value != 0.000 else "NA")
        # user.lb4.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][4], pb=float(user.pb4.value) if user.pb4.value != 0.000 else "NA")
        # user.lb5.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][5], pb=float(user.pb5.value) if user.pb5.value != 0.000 else "NA")
        # user.lb6.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][6], pb=float(user.pb6.value) if user.pb6.value != 0.000 else "NA")
        # user.lb7.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][7], pb=float(user.pb7.value) if user.pb7.value != 0.000 else "NA")
        # user.lb8.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][8], pb=float(user.pb8.value) if user.pb8.value != 0.000 else "NA")
        # user.lb9.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][9], pb=float(user.pb9.value) if user.pb9.value != 0.000 else "NA")
        # user.lb10.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][10], pb=float(user.pb10.value) if user.pb10.value != 0.000 else "NA")
        # user.lb11.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][11], pb=float(user.pb11.value) if user.pb11.value != 0.000 else "NA")
        # user.lb12.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][12], pb=float(user.pb12.value) if user.pb12.value != 0.000 else "NA")
        # user.lb13.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][13], pb=float(user.pb13.value) if user.pb13.value != 0.000 else "NA")
        # user.lb14.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][14], pb=float(user.pb14.value) if user.pb14.value != 0.000 else "NA")
        # user.lb15.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][15], pb=float(user.pb15.value) if user.pb15.value != 0 else "NA")
        # user.lb16.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][16], pb=float(user.pb16.value) if user.pb16.value != 0 else "NA")
        # user.lb17.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][17], pb=float(user.pb17.value) if user.pb17.value != 0 else "NA")
        # user.lb18.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][18], pb=float(user.pb18.value) if user.pb18.value != 0 else "NA")
        # user.lb19.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][19], pb=float(user.pb19.value) if user.pb19.value != 0 else "NA")
        # user.lb20.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][20], pb=float(user.pb20.value) if user.pb20.value != 0 else "NA")
        # user.lb21.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][21], pb=float(user.pb21.value) if user.pb21.value != 0 else "NA")
        # user.lb22.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][22], pb=float(user.pb22.value) if user.pb22.value != 0 else "NA")
        # user.lb23.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][23], pb=float(user.pb23.value) if user.pb23.value != 0 else "NA")
        # user.lb24.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][24], pb=float(user.pb24.value) if user.pb24.value != 0 else "NA")
        # user.lb25.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][25], pb=float(user.pb25.value) if user.pb25.value != 0 else "NA")
        # user.lb26.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][26], pb=float(user.pb26.value) if user.pb26.value != 0 else "NA")
        # user.lb27.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][27], pb=float(user.pb27.value) if user.pb27.value != 0 else "NA")
        # user.lb28.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][28], pb=float(user.pb28.value) if user.pb28.value != 0 else "NA")
        # user.lb29.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][29], pb=float(user.pb29.value) if user.pb29.value != 0 else "NA")
        # user.lb30.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][30], pb=float(user.pb30.value) if user.pb30.value != 0 else "NA")
        # user.lb31.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][31], pb=float(user.pb31.value) if user.pb31.value != 0 else "NA")
        # user.lb32.text = '{lb}: {pb}%'.format(lb=user.cause_list[0][32], pb=float(user.pb32.value) if user.pb32.value != 0 else "NA")

class FINAL_SCREEN(Screen):
    previous = StringProperty()
    def update(user, *args):
        user.pbval = 20
    def default(user, *args):
        user.pbval = 50


class CustLabel(Widget):
    lb = ObjectProperty()
    id = ObjectProperty(Widget)
    texture = ObjectProperty(Label)

    def __init__(self, *kwargs):
        super(CustLabel, self).__init__(**kwargs)
        self.lb = Label()
        self.size = self.texture_size
        self.font_size: 12
        self.color = [1, 1, 1, 1]


class CustPBar(Widget):
    pb = ObjectProperty()
    id = ObjectProperty(Widget)

    def __init__(self, *kwargs):
        super(CustPBar, self).__init__(**kwargs)
        self.pb = ProgressBar()
        self.size_hint_x = .9
        self.height = '48dp'
        self.max: 100


class MAINApp(App):
    def build(self):
        self.root = MyScreenManager()
        return self.root


if __name__ == '__main__':
    MAINApp().run()