import random

class Game:
    def __init__(self):
        self.user_item = None
        self.computer_item = None

    @staticmethod
    def get_user_item():
        list_choice = ["r", "p", "s"]
        user_item = input("Select (r)ock, (p)aper or (s)cissors ")
        if user_item not in list_choice:
            user_item = input("Wrong choice! Select (r)ock, (p)aper or (s)cissors ")
        return user_item
    
    @staticmethod
    def get_computer_item():
        list_choice = ["r", "p", "s"]
        computer_item = random.choice(list_choice)
        return computer_item
    
    def get_game_result(self):
        print(f"The user's chosen item is {self.user_item}")
        print(f"The computer's chosen item is {self.computer_item}")
        if self.user_item == self.computer_item:
            # print("It's a draw!")
            return "It's a draw!"
        elif self.user_item == "r" and self.computer_item == "s":
            # print("You win!")
            return "You win!"
        elif self.user_item == "r" and self.computer_item == "p":
            # print("You loose!")
            return "You loose!"
        elif self.user_item == "s" and self.computer_item == "r":
            # print("You loose!")
            return "You loose!"
        elif self.user_item == "s" and self.computer_item == "p":
            # print("You win!")
            return "You win!"
        elif self.user_item == "p" and self.computer_item == "r":
            # print("You win!")
            return "You win!"
        else:
            # print("You loose!")
            return "You loose!"
    
    def play(self):
        game = Game()
        game.user_item = game.get_user_item()
        game.computer_item = game.get_computer_item()

        result = game.get_game_result()
        print(f"Result: {result}!")
        return result

# game1 = Game()
# game1.get_game_result()



game = Game()
game.play()


