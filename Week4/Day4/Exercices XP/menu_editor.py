from menu_manager import MenuManager, MenuItem

class MenuEditor:
    @staticmethod
    def show_user_menu():
        while True:
            print("Program Menu:")
            print("V: View an Item")
            print("A: Add an Item")
            print("D: Delete an Item")
            print("U: Update an Item")
            print("S: Show the Menu")
            print("Q: Quit the Program")

            choice = input("Enter your choice: ").upper()

            if choice == "V":
                MenuEditor.view_item()
            elif choice == "A":
                MenuEditor.add_item_to_menu()
            elif choice == "D":
                MenuEditor.delete_item_from_menu()
            elif choice == "U":
                MenuEditor.update_item_in_menu()
            elif choice == "S":
                MenuEditor.show_restaurant_menu()
            elif choice == "Q":
                MenuEditor.show_restaurant_menu()
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def view_item():
        item_name = input("Enter the name of the item to view: ")
        item = MenuManager.get_by_name(item_name)

        if item is None:
            print("Item not found.")
        else:
            print(f"Item: {item.name}, Price: {item.price}")

    @staticmethod
    def add_item_to_menu():
        name = input("Enter the item's name: ")
        price = input("Enter the item's price: ")

        item = MenuItem(name, price)
        MenuManager.add_item(item)
        print("Item was added successfully.")

    @staticmethod
    def delete_item_from_menu():
        name = input("Enter the name of the item to delete: ")
        MenuManager.delete_item(name)
        print("Item was deleted successfully.")

    @staticmethod
    def update_item_in_menu():
        name = input("Enter the name of the item to update: ")
        new_name = input("Enter the new name of the item: ")
        new_price = input("Enter the new price of the item: ")
        MenuManager.update_item(name, new_name, new_price)
        print("Item was updated successfully.")

    @staticmethod
    def show_restaurant_menu():
        items = MenuManager.all_items()

        if items:
            print("Restaurant's Menu:")
            for item in items:
                print(f"Item: {item.name}, Price: {item.price}")
        else:
            print("No items found in the menu.")

if __name__ == "__main__":
    MenuEditor.show_user_menu()
