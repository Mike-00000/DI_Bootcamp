import random

sentence = input("Type a string, please. It must be 10 characters long ")
if len(sentence) < 10:
    print("string not long enough")
elif len(sentence) > 10:
    print("string too long")
else:
    firstChar = sentence[0]
    print(f"First character : {firstChar}")
    lastChar = sentence[-1:]
    print(f"Last character: {lastChar}")


i = 0

while(i < len(sentence)):
    print("The Character at %d Index Position = %c" %(i, sentence[i]))
    i = i + 1

print(sentence)

strlist = list(sentence)
print(strlist)
random.shuffle(strlist)
print(strlist)
shuffled_str = ''.join(strlist)

print(shuffled_str)
# shuffled_sentence = random.shuffle(random.sample(sentence))

# sentence_to_print = shuffled_sentence.join

# print(sentence_to_print)