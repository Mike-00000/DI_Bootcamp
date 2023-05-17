
# DAILY CHALLENGE - TEXT ANALYSIS ----------------------
# Part I -----------------------------------------------
class Text():
    def __init__(self, text):
        self.text = text
    
    def countOccurrences(self, word):
        splittext = self.text.split(" ")
        count = 0
        for i in range(len(splittext)):
            if word == splittext[i]:
                count += 1
        return count
    
    def findMostCommonWord(self):
        splittext = self.text.split(" ")
        word_count = {}
        for word in splittext:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        max_count = max(word_count.values())
        most_common_words = [word for word, count in word_count.items() if count == max_count]
        return most_common_words
    
    def getUniqueWords(self):
        splittext = self.text.split(" ")
        word_count = {}
        for word in splittext:
            lowercase_word = word.lower()
            if lowercase_word in word_count:
                word_count[lowercase_word] += 1
            else:
                word_count[lowercase_word] = 1
        unique_words = [word for word, count in word_count.items() if count == 1]
        return unique_words

text1 = Text("A good book would sometimes cost as much as a good house.")


word_to_count = "good"
count = text1.countOccurrences(word_to_count)
print(f"The word '{word_to_count}' appeares {count} time in the text.\n")


most_common_words = text1.findMostCommonWord()
print("The most frequent words in the text are:")
for word in most_common_words:
    print(word)

print()
unique_words = text1.getUniqueWords()
print("The unique words in the text are:")
for word in unique_words:
    print(word)




# Part II -----------------------------------------------
class Text:
    def __init__(self, text):
        self.text = text
    
    @classmethod
    def from_file(cls, file_name):
        with open("the_stranger.txt", 'r') as file:
            text = file.read()
        return cls(text)

text_from_file = Text.from_file('the_stranger.txt')
print(text_from_file.text)
