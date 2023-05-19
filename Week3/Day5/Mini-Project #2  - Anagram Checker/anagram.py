from anagram_checker import AnagramChecker

def validate_input(word):
    if len(word.split()) > 1:
        print("Error: Only a single word is allowed.")
        return False

    if not word.isalpha():
        print("Error: Only alphabetic characters are allowed.")
        return False

    return True

def format_anagrams(anagrams):
    if not anagrams:
        return "No anagrams found."
    return ", ".join(anagrams)

def main():
    anagram_checker = AnagramChecker('textfile.txt')

    while True:
        print("Menu:")
        print("1. Enter a word")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            word = input("Enter a word: ").strip()

            if validate_input(word):
                if anagram_checker.is_valid_word(word):
                    anagrams = anagram_checker.get_anagrams(word)
                    formatted_anagrams = format_anagrams(anagrams)
                    print(f"YOUR WORD: {word}")
                    print("This is a valid English word.")
                    print(f"Anagrams for your word: {formatted_anagrams}")
                else:
                    print("The word is not valid.")
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
