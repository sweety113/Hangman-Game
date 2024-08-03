import random
from hangman_stages import stages
list_name=["apple","banana","cherry"]
lives=6
chosen_word=random.choice(list_name)
print(chosen_word)
display=[]
for letter in chosen_word:
    display+='_'
print(display)

game_over=False

while not game_over:
    guess=input("Guess the letter:").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=guess
    print(display)


    if guess not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("you lose!")
    if '_' not in display:
        print("you win")       
    print(stages[lives])