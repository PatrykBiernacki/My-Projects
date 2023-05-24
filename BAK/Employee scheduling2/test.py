import datetime
# from collections import defaultdict


# # capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}

# # print(list(capital_city.values())[-1])
# capital_city = defaultdict()


# dict_ion = defaultdict()

# dict_ion.update(capital_city)
    
# print(dict_ion)
# print(dict_ion.keys())

#print (datetime.datetime.min)

list_of_dict = [{1: "Kathmandu", 2:'a'}, {2: "Rome", 3:'a'}, {3: "London", 4:'a'}]
capital_city = {1: "Kathmandu", 2: "Rome", 3: "London"}

# list_of_dict.sort(key= lambda x: list(x.keys())[-1], reverse= True)

# print(list_of_dict)

for key in capital_city:
    print(key)