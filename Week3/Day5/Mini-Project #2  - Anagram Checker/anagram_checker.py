

# class AnagramChecker:
#     def __init__(self, textfile):
#         self.textfile = textfile
#         with open("text-file.txt", "r") as file:
#             textfile = file.readlines()
    
#     def is_valid_word(self):
#         word = input("Give a word ")
#         try:
#             if word in self.textfile:
#                 print("You gave a valid word ")
#         except:
#             input("You gave an unvalid word. Give another word ")


# ana = AnagramChecker(1)
# ana.is_valid_word()



class AnagramChecker:
    def __init__(self, textfile):
        self.wordlist = self.load_wordlist(textfile)
    
    def load_wordlist(self, textfile):
        with open("text-file.txt", 'r') as file:
            return [word.strip().lower() for word in file.readlines()] 

    def is_valid_word(self, word):
        return word.lower() in self.wordlist
    
    def is_anagram(self, word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()
        if len(word1) != len(word2):
            return False
        return sorted(word1) == sorted(word2) and word1 != word2
    
    def get_anagrams(self, word):
        word = word.lower()
        anagrams = []
        for w in self.wordlist:
            if self.is_anagram(word, w):
                anagrams.append(w)
        return anagrams

anagram_checker = AnagramChecker('textfile.txt')

word = input("Enter a word: ")
anagrams = anagram_checker.get_anagrams(word)
print(anagrams)

if anagram_checker.is_valid_word(word):
    print("The word is valid.")
else:
    print("The word is not valid.")
