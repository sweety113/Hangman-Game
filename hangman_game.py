#hangaman game :it is a guessing game.two or three persons will  play
#first persson   second person
#apple(will be given by 1st person)
#second person will be given -----(5 dashes apple length)
#within limited number of gusses should be there
#hanging man will be drawn by 1st person by the gueses of sescond person
#if 2nd  one told ------ 1st dash head will be drawn like wise all attempts
#if 2nd persons guses (full hangman diagram drawn by 1st)compled then game over
#2nd person willl loose
#   +--------+
#   |        |
#   0        |
#  /|\       |
#  / \       |
#            |

import random
import stages

word_list=["apple","beautiful","potato","attitude","fan","light","supriya","naveen","nani","altitude","arrogant","paris","python"]
lives=6
choosen_word=random.choice(word_list)
print(choosen_word)

display=[]
for i in range(len(choosen_word)):# 0 1 2 3 4 5#apple
    display += '_'
print(display)

game_over=False
while not game_over:#we dont know the number of iteratioins in while loop
    guessed_letter=input("gusses a letter:").lower()#p  _pp__
    for position in range(len(choosen_word)):#0 1 2 3 4
        letter=choosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)

    if guessed_letter not in choosen_word:
        lives -=1
        if lives ==0:
            game_over=True
            print("You lose!!")

    if '_' not in display:
        game_over=True
        print("You win!!")
    print(stages.stages[lives])



































