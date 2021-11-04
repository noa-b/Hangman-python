import random
from hangman_art import logo
from hangman_words import word_list 
from hangman_art import stages

print(logo)

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()

word = random.choice(word_list)
print(word)

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("you already tried", guess, "!")
            elif guess not in word:
                print(guess, "isn't in the word :(")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Nice one,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already tried ", guess, "!")
            elif guess != word:
                print(guess, " ist nicht das Wort :(")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("invalid input")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Good Job, you guessed the word!")
    else:
        print("I'm sorry, but you ran out of tries. The word was " + word + ". Maybe next time!")

hint = input("Do you want a hint?(Y/N)").lower




def display_hangman(tries):
 print(stages[tries]) 

def main():
    word = get_word(word_list)
    play(word)
    while input("Again? (Y/N) ").upper() == "Y":
        word = get_word(word_list)
        play(word)

if __name__ == "__main__":
    main()

# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')
# word_length = len(chosen_word)

# display = []
# #number_of_blankes = len(chosen_word)
# #display = ["_"] * number_of_blankes
# #print(display)
# display = []
# for _ in range(word_length):
#     display += "_"

# #for position in range(number_of_blankes):
# #    letter = chosen_word[position]
#  #   if letter == guess :
#   #    display[position] = letter
#    # else:
#     # pass
# End_of_game = False

# tries = 6
# print(display_hangman(tries))

# while not End_of_game : 
#   guess = input("Guess a letter: ").lower()

#   for position in range(word_length):
#       letter = chosen_word[position]
#       #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#       if letter == guess:
#          display[position] = letter
#          print(display)
#          tries -= 1
#       else:
#         pass
#         tries -= 1

# print(display)

# if "_" not in display:
#   End_of_game = True
#   print("Good job \n you won :)")
