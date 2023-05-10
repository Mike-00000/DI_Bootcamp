


matrix = "7i3Tsih%xi #sM $a #t%^r!"

# rows = []
# current_row = ""
# for caractere in matrix:
#     current_row += caractere
#     if len(current_row) == 3:
#         rows.append(current_row)
#         current_row = ""

# print(rows)



# rows = [matrix[i:i+3] for i in range(0, len(matrix), 3)]
# resultat = ""
# for row in rows:
#     if len(row) > 0 and row[0].isalpha():
#         resultat += row[0]

# print(resultat)



# rows = [matrix[i:i+3] for i in range(0, len(matrix), 3)]

# resultat_position_0 = ""
# resultat_position_1 = ""
# resultat_position_2 = ""

# for row in rows:
#     if len(row) > 0 and row[0].isalpha():
#         resultat_position_0 += row[0]
#     if len(row) > 1 and row[1].isalpha():
#         resultat_position_1 += row[1]
#     if len(row) > 2 and row[2].isalpha():
#         resultat_position_2 += row[2]

# print("Position 0:", resultat_position_0)
# print("Position 1:", resultat_position_1)
# print("Position 2:", resultat_position_2)


rows = [matrix[i:i+3] for i in range(0, len(matrix), 3)]

resultat_position_0 = ""
resultat_position_1 = ""
resultat_position_2 = ""

for row in rows:
    if len(row) > 0 and (row[0].isalpha() or row[0] == " "):
        resultat_position_0 += row[0]
    if len(row) > 1 and (row[1].isalpha() or row[1] == " "):
        resultat_position_1 += row[1]
    if len(row) > 2 and (row[2].isalpha() or row[2] == " "):
        resultat_position_2 += row[2]

resultat_total = f"{resultat_position_0} {resultat_position_1} {resultat_position_2}"
resultat_total = resultat_total.replace("matr ix", "matrix") # BUT THAT DOES'NT WORK
print(resultat_total)
