# hangman game behen ka bhosda
import random
lives = 6
word_list = ["chootar", "chaati", "rasgulla"]
a = random.choice(word_list)
print(a)
placeholder = ""
wordlen = len(a)
for position in range(wordlen):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letter = []

while not game_over:
    guess = input("guess the letter")

    display = ""

    for i in a:
        if i == guess:
            display += i
            correct_letter.append(guess)
        elif i in correct_letter:
            display += i

        else:
            display += "_"
    print(display)

    if guess not in a:
        lives -= 1
        if lives == 0:
            print("you lose")
            game_over = True


    if "_" not in display:
        game_over = True
        print("you win")