#Objective: Create a script that performs various operations on a string input.

"""Ask the user to enter a sentence
Display the following information about their input: 
The original sentence
The sentence in ALL UPPERCASE
The sentence in all lowercase
The number of characters (including spaces)
The number of words
The first word
The last word
The sentence with all 'a' characters replaced with '@'"""

user_input=input("Enter a sentence:  ")

words = user_input.split()

print(f"\nOriginal: {user_input}")
print(f"\nAll UPPER: {user_input.upper()}")
print(f"\nall lower: {user_input.lower()}")
print(f"\nCharacter Count: {len(user_input)}")
print(f"\nWord Count: {len(words)}")
print(f"\nFirst Word: {words[0]}")
print(f"\nLast Word: {words[-1]}")
print(f"\nReplaced: {user_input.replace('a','@')}")
