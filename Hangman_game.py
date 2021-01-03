
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


print(f'Pssst, the available options are {word_list}. \nYour job is to choose the correct word, before you ran out of lives')


for n in range(len(chosen_word)):
  display.append("_")


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
