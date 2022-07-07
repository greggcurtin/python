import csv
import numpy as np
import pandas as pd

data_path = "C:\\Users\\gcurtin\\PycharmProjects\\RISKFINDER\\venv\\data\\injurybystate.csv"
injury_data = pd.read_csv(data_path ,names = ['State','Vehicle','Firearm','Poisoning','Falls','Occupational','Choking','FireSmoke','Drowning','HeatCold','BluntForce'])
choking_data = []
falls_data = []
motor_data = []
poison_data = []
input_state = input("Enter State Acronym: ")
input_state = input_state.upper()
InjuryDict = dict()
InjuryRisk = dict()
testlist = dict()
injuries = []
states = []
# def parseInjury():
#     for index, row in injury_data.iterrows():
#         choking_row = (row['State'],row['Choking'])
#         print("Choking Row", choking_row)
#         choking_data.append(choking_row)
#
#     for index, row in injury_data.iterrows():
#         falls_row = (row['State'],row['Falls'])
#         print("Falls Row", falls_row)
#         falls_data.append(falls_row)
#
#     for index, row in injury_data.iterrows():
#         motor_row = (row['State'], row['Motor Vehicle'])
#         print("Motor Row", motor_row)
#         motor_data.append(motor_row)
#
#     for index, row in injury_data.iterrows():
#         poison_row = (row['State'],row['Poisoning'])
#         print("Poision Row", poison_row)
#         poison_data.append(poison_row)

def find_lists():
    for tuple in injury_data.itertuples(index=False, name='Injury'):
        # print(row)
        # print(row.State, row.Choking, row.Falls, row.Poisoning)
        # ChokingDict[row.State] = [row.Choking]
        InjuryDict[tuple[0]] = tuple
    value = 0
    states = list(InjuryDict.keys())
    states.remove('State')
    injuries = list(injury_data)
    injuries.remove('State')
    print("States", states)
    print("Injuries", injuries)
    del InjuryDict['State']
    pass

def parseInjury2():

    def find_risk(val):
        if int(val) < 0.001:
            val = 0.001
        risk_val = (int(val) / 100000) * 100
        return round(risk_val,6)

    for tuple in injury_data.itertuples(index=False, name='Injury'):
        #print(row)
        #print(row.State, row.Choking, row.Falls, row.Poisoning)
        #ChokingDict[row.State] = [row.Choking]
        InjuryDict[tuple[0]] = tuple
    value = 0
    states = list(InjuryDict.keys())
    states.remove('State')
    injuries =list(injury_data)
    injuries.remove('State')
    print("States" , states)
    print("Injuries", injuries)
    del InjuryDict['State']
    InjuryRisk = InjuryDict
    for state in states:
        print("State", state, InjuryRisk[state])
        for value in InjuryRisk.values():
            print(value)

                #testlist[state][i] = list(zip(*InjuryRisk[state][i]))

        #print(InjuryRisk[state])
        #for i in range(1,11,1):
            #InjuryRisk[state][i] = value
            #value = value /1000
            #print(value)
    #print(InjuryRisk)

    #print(InjuryDict['TX'])
    #print(InjuryDict['TX'].Choking)
    print(InjuryDict[input_state])



    #print(InjuryRisk['TX'])
    #for state in states:
        #InjuryRisk[state] = InjuryDict[state].value
    #for i, row in enumerate(injury_data.itertuples(), 1):
        #print("Enumerate", i, row[1], row[2], row[3])
    #injuries = InjuryDict.
    #for i,v in InjuryDict.items():
        #print(find_risk(int(InjuryDict[i].Choking)))
        #print(InjuryDict[i])

def parseInjury3():
    testdata = []
    testrow = []
    riskval = []
    states = ["State", "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC",
              "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA",
              "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN",
              "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM",
              "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI",
              "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA",
              "WV", "WI", "WY"]
    find_lists()
    def find_risk(val):
        if val < 0.001:
            val = 0.001
        risk_val = (val / 100000) * 100
        return round(risk_val,6)

    for index, row in injury_data.iterrows():
        #print("row", row)
        #print("index",index)
        for state in states:
            for injury in injuries:
                injury_row[state] = (row[injury], row[state])
                injury_data.append(injury_row[state])
        #print(injury_data)
    print("table", injury_data)
    print("input state", input_state)
    print("states", states)
    print("state", injury_data.State[states.index(input_state)])
    print("Vehicle", injury_data.Vehicle[states.index(input_state)])
    injury_list = [[i for i, j in injury_data], [j for i, j in injury_data]]
    vrisk = find_risk(float(injury_data.Vehicle[states.index(input_state)]))
    print(vrisk)
    print(injury_list)
        #print(item[0],item[1])
    #print("choking",injury_data.Choking)
        #print("rows", injury_data.State())
        #print("columns", injury_data.State())
        #choking_row = (row['State'], row['Choking'])
        #choking_data.append(choking_row)
    #print(choking_data)
            #testrow[injury] = (row['State'], row[injury])
            #testdata.append(testrow)
        #print("testdata", testdata)



        #InjuryRisk[index] = row
            #print(InjuryRisk.values())
            #print(row.State, row.Choking, row.Falls, row.Poisoning)
        #ChokingDict[row.State] = [row.Choking]
        #InjuryDict[row[1]] = row
        #print(index, row)

    #states = InjuryDict.keys()
    #injuries =InjuryDict.values()
    #print("States" , states)
    #injuries = InjuryDict.
    #for i,v in InjuryDict.items():
        #print(find_risk(InjuryDict[i].Choking))
        #print(InjuryDict[i])
        #print(InjuryDict[i])




#parseInjury2()
find_lists()
parseInjury3()

#print(InjuryDict[str(input_state)])
#print(InjuryRisk[str(input_state)])
#for i in InjuryDict:
    #print (i, InjuryDict[i])
#for k,v in InjuryDict.items():
    #print ('key',k, '-->','value', v)
    #print(v.Choking)
#print(InjuryDict[input_state].Choking)
#print(InjuryDict[input_state].Falls)
#print(InjuryDict[input_state].Poisoning)
#print(InjuryDict[input_state].Drowning)
#print(InjuryDict[input_state].Vehicle)




def find_risk(val):
    risk_val = (val/100000) * 100
    return risk_val

# ChokingDict = dict(choking_data)
# FallsDict = dict(falls_data)
# MotorDict = dict(motor_data)
# PoisonDict = dict(poison_data)
#
# choking_chance = ChokingDict.get(input_state)
# falls_chance = FallsDict.get(input_state)
# motor_chance = MotorDict.get(input_state)
# poison_chance = PoisonDict.get(input_state)
#
# choking_risk = round(find_risk(choking_chance),6)
# falls_risk = round(find_risk(falls_chance),6)
# motor_risk = round(find_risk(motor_chance),6)
# poison_risk = round(find_risk(poison_chance),6)

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


#print_risk()
#find_variance()
