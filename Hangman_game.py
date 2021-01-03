
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display=[]

#Testing code
print(f'Pssst, the available options are {word_list}. \nYour job is to choose the correct word, before you ran out of lives')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
for n in range(len(chosen_word)):
  display.append("_")



#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
# for letter in chosen_word:
#     if letter == guess:
#         display[n]=guess
#     else:
#         print("Wrong")

lives=7

while "_" in display!=False:
    guess = input("Guess a letter: ").lower()
    for n in range(len(chosen_word)):
        if guess == chosen_word[n]:
            display[n]=guess
        #else:
        #  print("wrong")
    print(f"{' '.join(display)}")
    if(guess not in display):
        lives-=1
        print(stages[lives])
    print(f"the number of lives you have is equal to {lives}")
    
    if lives==0:
      print("Sorry!! you loose")
      exit()
    elif "_" not in display:
      print("congrats!! you win")
#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

