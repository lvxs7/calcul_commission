import os
import json

#Définition de fonctions
### Conversion données JSON en données dictionnaire (table de hachage) Python 
def JSONtoPython(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            data=json.load(file)
        return data
    else:
        return False

### Calcul de commissions
def commission(objective, compensation):
    firstInterval= objective/2
    commission=0
    if compensation <= firstInterval:
        commission+= compensation*0.05
        return commission
    elif compensation >= firstInterval or compensation == objective:
        commission+= compensation*0.1
        return commission
    elif compensation > objective :
        commission+= (compensation - objective)*0.15
        return commission
    else:
        return False

    

#**********     MAIN     ***********
file_path="level3/data/input.json"
total_one=0
total_two=0
getUserID_one=0
getUserID_two=0

data = JSONtoPython(file_path)
getDeals=data['deals']
getUsers=data['users']

for user in getUsers:
    if(user['id']) == 1:
        getUserObjective_one = user['objective']
    else:
        getUserObjective_two = user['objective']

print(getUserObjective_one,getUserObjective_two) # Vérification

for deal in getDeals:
    if(deal['user']) == 1:
        getUserID_one=deal['user']
        if deal['amount'] <= getUserObjective_one/2:
            total_one+=commission(getUserObjective_one, float(deal['amount'])) # Fonction qui retourne un float alors essentiel de faire une conversion
        elif deal['amount'] >= getUserObjective_one/2 or deal['amount'] == getUserObjective_one:
            total_one+=commission(getUserObjective_one, float(deal['amount']))
        elif deal['amount'] > getUserObjective_one:
            total_one+=commission(getUserObjective_one, float(deal['amount']))
    else:
        getUserID_two=deal['user']
        if deal['amount'] <= getUserObjective_two/2:
            total_two+=commission(getUserObjective_two, float(deal['amount']))
        elif deal['amount'] >= getUserObjective_two/2 or deal['amount'] == getUserObjective_one:
            total_two+=commission(getUserObjective_two, float(deal['amount']))
        elif deal['amount'] > getUserObjective_two:
            total_two+=commission(getUserObjective_two, float(deal['amount']))



#data_commissions = {'commissions': }
print(total_one,total_two)
#print(type(commission(getUserObjective_one, 500)))
#print(commission(objective, compensation))