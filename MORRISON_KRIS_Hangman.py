import random

# PARAMETERS
LIFE = 6
FILE = "word_list.txt"
display = []
letter_already_guessed = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO 1.import txt file
file = open(FILE, "r")
all_text = file.read()
lists_word = list(map(str, all_text.split()))

# TODO 2.Random the name from the list of words
# Randomize the word choice and display the blanks
word = random.choice(lists_word)
length = len(word)

# make the word into a list
letter_list = list(word)

for letter in letter_list:
    display.append("*")

print(f"Welcome to the game of 'Hangman'")

# TODO 3. if player still has lifes, is the letter correct?
print(f"Here is your word to guess: {' '.join(map(str, display))}")
while LIFE > 0:
    result = "False"
    letter_guess = input("Please, guess a letter? ").lower()
    
    if len(letter_guess) > 1:
        print("Please only type one character!")
    elif letter_guess not in letters:
        print("Please don't type characters that are not in the alphabet!")
    elif letter_guess in letter_already_guessed:
        print("This letter is already guessed!")
    else:
        letter_already_guessed.append(letter_guess)
        for letter in letter_list:
            if letter_guess == letter:
                result = "True"
                for item in range(0, length):
                    character = letter_list[item]
                    if character == letter_guess:
                        display[item] = letter_guess

 # TODO 4. if player guess right or wrong? Take life or add letter to the word.
        if result == "False":
            LIFE -= 1
            print(f"This is not a letter in the word! You have lost a life. You have {LIFE} lifes left.")
            print(' '.join(map(str, display)))
        elif result == "True":
            print(' '.join(map(str, display)))
            print(f"This is a in the word! You have {LIFE} lifes left.")

        if LIFE == 0:
            print("Game Over! Your are out of lives!")
        elif display == letter_list:
            print("You Win and correctly got the word!")
