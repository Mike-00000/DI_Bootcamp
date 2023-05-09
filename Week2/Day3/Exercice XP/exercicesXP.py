# Exercise 1 : Convert Lists Into Dictionaries
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# new = zip(keys, values)
# print(list(new))


# Exercise 2 : Cinemax
# family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
# total_cost = 0
# for name, age in family.items():
#     if age < 3:
#         cost = 0
#     elif age <= 12:
#         cost = 10
#     else:
#         cost = 15
#     print(name, "has to pay $", cost)
#     total_cost += cost
# print("Total cost for the family:", total_cost)
# print(family.items())



# Exercise 3: Zara
brand = {
    "name": "Zara ",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona ", 
    "type_of_clothes": "men " "women " "children " "home ",
    "international_competitors": "Gap " "H&M " "Benetton ", 
    "number_stores": 7000, 
    "major_color": {
        "France": "blue ", 
        "Spain": "red ", 
        "US": "pink " "green ",
    }
}
# print(brand)

brand["number_stores"] = 2
# print(brand["type_of_clothes"])


# client = []
# for item in brand["type_of_clothes"]:
#     if item != "home":
#         client.append(item)(brand)
# clients_str = "".join(client)
# print('The clients of Zara are {}'.format(clients_str))


# brand["country_creation"] = "Spain"

competitors = brand["international_competitors"].split(",")
competitors.append("Desigual")
brand["international_competitors"] = "".join(competitors)
print(brand)

brand.pop("creation_date")
print(brand)

competitors = brand["international_competitors"]
print(competitors[2]) # It does'nt work...

last_value = list(brand.values())[-3][-1]
print(last_value)

last_value = list(brand.values())[-1]
print(last_value)

num_pairs = len(brand)
print("The number of key-value pairs in the dictionary is:", num_pairs)

print(brand.keys())

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

brand.update(more_on_zara)

print(brand["number_stores"])


# Exercise 4 : Disney Characters



