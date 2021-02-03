
# Asks the input from the user
word1 = input("Enter The Word")

#Reverse the input
word2 = word1[-1::-1]

# makes the string a list
word2 = list(word2)

# String in which the final output  will be stored
result = ""

# Finding the position and replacing the vowels
for i in word2:
    if i == "a":
        pos_a = word2.index("a")
        word2.remove("a")
        word2.insert(pos_a, "0")
    if i == "e":
        pos_e = word2.index("e")
        word2.remove("e")
        word2.insert(pos_e, "1")
    if i == "o":
        pos_o = word2.index("o")
        word2.remove("o")
        word2.insert(pos_o, "2")
    if i == "u":
        pos_u = word2.index("u")
        word2.remove("u")
        word2.insert(pos_u, "3")

#Add 'aca' to the end of the word
word2.append("aca")
for i in word2:
    result += i

print(result)

