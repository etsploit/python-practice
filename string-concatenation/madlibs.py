# This project uses string concatenation in order to create a madlib
# I honestly didn't know what a madlib was until I googled it
# "Mad Libs is a phrasal template word game which consists of one player prompting others for a list of words 
# to substitute for blanks in a story before reading aloud. 
# The game is frequently played as a party game or as a pastime."

# String concatenation is about putting strings together
# Suppose we  want to create a string that says "My name is _____"
name = "Ethan" #some string variable

# several ways to complete this task
print("My name is " + name)
print("My name is {}".format(name))
print(f"My name is {name}")

# now to use these tools in a madlib
adj = input("Adjective: ")
love = input("What do you love? ")
feeling = input("Feeling: ")
feeling2 = input("Another Feeling: ")
someone = input("Someone: ")
madlib = f"Sometimes life is so {adj}! it makes me feel so {feeling} all the time because \
    I love my {love} but I get so {feeling2} and don't want to let {someone} down."

print(madlib)