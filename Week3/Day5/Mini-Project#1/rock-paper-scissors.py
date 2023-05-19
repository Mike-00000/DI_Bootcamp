
from game import Game

def get_user_menu_choice():
    user_choice = input('\'1\': Play a new game\n \'2\': Show scores\n \'3\' Quit: ')
    return user_choice

def print_results(results: dict):
    print("Thank you for playing. Here are the final results:\n")
    print(f"You won: {results.get('Win', 0)} times")
    print(f"You lost: {results.get('Loss', 0)} times")
    print(f"You drew: {results.get('Draw', 0)} times\n")

def main():
    final_results = {
        "Win": 0,
        "Loss": 0,
        "Draw": 0
    }
    user_choice = get_user_menu_choice()

    while user_choice != '3':
        if user_choice == '1':
            new_game = Game()
            result = new_game.play()
            final_results[result] = final_results.get(result, 0) + 1
            user_choice = get_user_menu_choice()
        elif user_choice == '2':
            print_results(final_results)
            user_choice = get_user_menu_choice()
        else:
            print("Invalid choice. Please try again.")
            user_choice = get_user_menu_choice()

main()
