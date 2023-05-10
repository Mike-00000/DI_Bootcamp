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


for i in range(len(sentence)):
    print(f"The character at {i} index position: {sentence[i]}")
print(sentence)


new_sentence = ""
for letter in sentence:
    new_sentence = new_sentence + letter
    print(new_sentence)


strlist = list(sentence)
print(strlist)
random.shuffle(strlist)
print(strlist)
shuffled_str = ''.join(strlist)

print(shuffled_str)





# # shuffled_sentence = random.shuffle(random.sample(sentence))

# # sentence_to_print = shuffled_sentence.join

# # print(sentence_to_print)