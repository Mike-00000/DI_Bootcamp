# EXERCICE XP ------------------------------------


import psycopg2

connection = psycopg2.connect(
    database = 'Restaurant_Menu_Manager',
    user = 'postgres',
    password = 'test',
    host = 'localhost',
    port = '5432'
)

cursor = connection.cursor()

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def save(self):
        query = f"""
        INSERT INTO Menu_Items
        (item_name, item_price)
        VALUES {self.name, self.price}
        """
        cursor.execute(query)
        connection.commit()

    def delete(self):
        query = f"""
        DELETE FROM Menu_Items
        WHERE item_name = '{self.name}' AND item_price = {self.price}
        """
        cursor.execute(query)
        connection.commit()

    def update(self, new_name, new_price):
        query = f"""
        UPDATE Menu_Items SET item_name = '{new_name}', item_price = {new_price}
        WHERE item_name = '{self.name}' AND item_price = {self.price}
        """
        cursor.execute(query)
        connection.commit()

item1 = MenuItem("Couscous", 50)
# item1.save()
# item1.delete()
# item1.update("New Couscous", 69)

# item2 = MenuItem("Mega Burger", 65)
# item2.save()

# item3 = MenuItem("Pizza 4 cheeses", 59)
# item3.save()


cursor.close()
connection.close()