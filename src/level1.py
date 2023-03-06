import os
import json

#Définition des fonctions
### Conversion données JSON en données dictionnaire (table de hachage) Python
def JSONtoPython(file_path):
    if os.path.exists(file_path):
        with open(file_path,"r+") as fileJson:
            data=json.load(fileJson)
        return data
    else:
        return False

### Calcul de commissions
def commission(compensation, nb_sales, bonus):
    if nb_sales==1 or nb_sales==2:
        if compensation >= 2000:
            compensation+=(compensation*0.1)+bonus
        else:
            compensation+=compensation*0.1
        return compensation
    elif nb_sales > 2:
        if compensation >= 2000:
            compensation+=(compensation*0.2)+bonus
        else:
            compensation+=compensation*0.2
        return compensation
    elif compensation >= 2000:
        compensation+=bonus
        return compensation
    else:
        return False

#**********     MAIN     ***********
file_path="level1/data/input.json"
total_one=0
total_two=0
count_one=0 #Count number of sales
count_two=0
bonus = 500 #If sold more than 2000 euros
getUserID_one=0
getUserID_two=0
#print(type(getFile(file_path)))
data = JSONtoPython(file_path)
#print (data)
#print(data['deals'])
for deal in data['deals']:
    if(deal['user']) == 1:
        getUserID_one=deal['user']
        total_one+=deal['amount']
        count_one+=1
    else:
        getUserID_two=deal['user']
        total_two+=deal['amount']
        count_two+=1


#print(count_one,count_two)
data_commissions= {'commissions':[{'user_id': getUserID_one,'commission': commission(total_one, count_one, bonus)}, {'user_id': getUserID_two,'commission': commission(total_two, count_two, bonus)}]}

with open('level1/data/expected_outputLVI.json','w+') as file:
    json.dump(data_commissions,file,indent=4)

print("Compensation first user:",commission(total_one, count_one, bonus))
print("Compensation second user:",commission(total_two, count_two, bonus))