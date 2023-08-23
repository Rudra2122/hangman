import random
from hangman_wordlist import word_list

chosen_word = random.choice(word_list)
print("Your chosen word is ", chosen_word)

lives = 6

from hangman_stages import logo

print(logo)

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"  # adding underscores for each character of the selected word
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Enter your guess letter: ").lower()

    if guess in display:
        print("You have already guessed ", guess)

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print("You have guessed a letter that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            print("You Lose")
            end_of_game = True

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win")
    from hangman_stages import stages

    print(stages[lives])
