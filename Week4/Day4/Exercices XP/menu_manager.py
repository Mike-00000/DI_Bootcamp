import psycopg2

connection = psycopg2.connect(
    database='Restaurant_Menu_Manager',
    user='postgres',
    password='test',
    host='localhost',
    port='5432'
)

cursor = connection.cursor()

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        query = f"""
        SELECT * FROM Menu_Items
        WHERE item_name = '{name}'
        """
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            item_id, item_name, item_price = result
            return MenuItem(item_name, item_price)
        else:
            return None

    @classmethod
    def all_items(cls):
        query = """
        SELECT * FROM Menu_Items
        """
        cursor.execute(query)
        results = cursor.fetchall()

        items = []
        for item in results:
            item_id, item_name, item_price = item
            items.append(MenuItem(item_name, item_price))
        
        return items

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Exemple d'utilisation de la méthode get_by_name()
item = MenuManager.get_by_name("Couscous")
if item:
    print(f"Item found: {item.name}, Price: {item.price}")
else:
    print("Item not found")


items = MenuManager.all_items()
for item in items:
    print(f"Item: {item.name}, Price: {item.price}")