import csv
import numpy as np
import pandas as pd

data_path = "C:\\Users\\gcurtin\\PycharmProjects\\RISKFINDER\\venv\\data\\injurybystate.csv"
injury_data = pd.read_csv(data_path)
choking_data = []
falls_data = []
motor_data = []
poison_data = []
input_state = input("Enter State Acronym: ")
input_state = input_state.upper()

def parseInjury():
    for index, row in injury_data.iterrows():
        choking_row = (row['State'],row['Choking'])
        print("Choking Row", choking_row)
        choking_data.append(choking_row)

    for index, row in injury_data.iterrows():
        falls_row = (row['State'],row['Falls'])
        print("Falls Row", falls_row)
        falls_data.append(falls_row)

    for index, row in injury_data.iterrows():
        motor_row = (row['State'], row['Motor Vehicle'])
        print("Motor Row", motor_row)
        motor_data.append(motor_row)

    for index, row in injury_data.iterrows():
        poison_row = (row['State'],row['Poisoning'])
        print("Poision Row", poison_row)
        poison_data.append(poison_row)

parseInjury()

def find_risk(val):
    risk_val = (val/100000) * 100
    return risk_val

ChokingDict = dict(choking_data)
FallsDict = dict(falls_data)
MotorDict = dict(motor_data)
PoisonDict = dict(poison_data)

choking_chance = ChokingDict.get(input_state)
falls_chance = FallsDict.get(input_state)
motor_chance = MotorDict.get(input_state)
poison_chance = PoisonDict.get(input_state)

choking_risk = round(find_risk(choking_chance),6)
falls_risk = round(find_risk(falls_chance),6)
motor_risk = round(find_risk(motor_chance),6)
poison_risk = round(find_risk(poison_chance),6)

def print_risk():
    print('\n')
    print("Your choking risk for {}: ".format(str(input_state)), choking_risk)
    print("Your fall risk for {}: ".format(str(input_state)), falls_risk)
    print("Your motor vehicle risk for {}: ".format(str(input_state)), motor_risk)
    print("Your poison risk for {}: ".format(str(input_state)), poison_risk)
    print('\n')
    print("Average choking risk:", round(find_risk(ChokingDict.get("USA")),6))
    print("Average fall risk:", round(find_risk(FallsDict.get("USA")),6))
    print("Average motor vehicle risk", round(find_risk(MotorDict.get("USA")),6))
    print("Average poison risk", round(find_risk(PoisonDict.get("USA")),6))

def find_variance():
    print('\n')
    var_choking = choking_risk - round(find_risk(ChokingDict.get("USA")),6)
    sign = find_sign(var_choking)
    print ("Choking Variance: ", sign, abs(round(var_choking, 5)))
    var_falls = falls_risk - round(find_risk(FallsDict.get("USA")),6)
    sign = find_sign(var_falls)
    print ("Falls Variance: ", sign, abs(round(var_falls, 5)))
    var_motor = motor_risk - round(find_risk(MotorDict.get("USA")),6)
    sign = find_sign(var_motor)
    print ("Motor Vehicle Variance: ", sign, abs(round(var_motor, 5)))
    var_poison = poison_risk - round(find_risk(PoisonDict.get("USA")),6)
    sign = find_sign(var_poison)
    print ("Poison Variance: ", sign, abs(round(var_poison, 5)))
    print('\n')

def find_sign(val):
    if val >= 0:
        sign = "+"
    if val < 0:
        sign = '-'
    return sign


print_risk()
find_variance()
