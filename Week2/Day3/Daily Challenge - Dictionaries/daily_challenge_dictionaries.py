# CHALLENG 1 ---------------------------------

# word = input("Please enter a word: ")

# letter_indexes = {}

# for index, letter in enumerate(word):
#     if letter not in letter_indexes:
#         letter_indexes[letter] = []
#     letter_indexes[letter].append(index)

# print(letter_indexes)



# CHALLENGE 2 ---------------------------------
items_purchase = {
  "Water": 1,
  "Bread": 3,
  "TV": 1000,
  "Fertilizer": 20
}

wallet = 0

affordable_items = []

for item, price in items_purchase.items():
    if price <= wallet:
        affordable_items.append(item)

if len(affordable_items) == 0:
    print("Nothing")
else:
    affordable_items.sort()
    print("You can afford:", affordable_items)


