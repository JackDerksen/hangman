from random import randint
from words import word_list
from stages import hangman_stages


class Word:
    def __init__(self) -> None:
        self.__word = word_list[randint(1, 300)]
        self.__guessed_letters = []
        self.__wrong_guesses = []
        self.__num_wrong_guesses = 0
        self.is_guessed = False
        self.game_over = False

    # Turn the word into a list of underscores
    def hide(self):
        return '_' * len(self.__word)

    # Turn the word into a list of letters
    def listify(self):
        return [letter for letter in self.__word]

    # Append the guessed letter to the list of guessed letters
    def add_letter_to_guessed(self, letter):
        self.__guessed_letters.append(letter)

    # Fill in the blanks with correctly-guessed letters
    def fill(self):
        return [letter if letter in self.__guessed_letters else '_' for letter in self.__word]

    # Check if the user guessed a letter right
    def is_in_word(self, letter):
        if (letter in self.__guessed_letters) or (letter in self.__wrong_guesses):
            print('You already guessed that letter!')
            return True if letter in self.__guessed_letters else False

        if letter in self.__word:
            self.__guessed_letters.append(letter)
            if ''.join(self.__guessed_letters) == self.__word:  # NOT WORKING #################
                self.is_guessed = True
            return True
        else:
            self.__num_wrong_guesses += 1
            self.__wrong_guesses.append(letter)
            return False

    # Check if the user guessed the whole word right
    def guessed_word(self, guess):
        if guess == self.__word:
            print('🎆 Congratulations, you guessed the word! 🎆')
            print(f'-> {self.__word}')
            self.is_guessed = True
        else:
            self.__num_wrong_guesses += 1

    # Print the right hangman stage based on the number of wrong guesses
    def display_hangman(self):
        if self.__num_wrong_guesses < 7:
            print(hangman_stages[self.__num_wrong_guesses])
        else:
            print('Game over!')
            self.game_over = True


def main():
    word = Word()
    hidden = word.hide()
    listed = word.listify()
    # print(f'Debug: {listed}')
    counter = 0

    while not word.is_guessed or word.game_over:
        if counter == 0:
            print(hidden)

        guess = input('\nGuess a letter or the whole word: ').lower()

        # Guessing a letter
        if len(guess) == 1:
            if word.is_in_word(guess):
                print('\nCorrect!\n\n\n')
                if word.is_guessed:
                    print('\n🎆 Congratulations, you won! 🎆')
                    break
            else:
                # Automatically updates the number of wrong guesses in word.is_in_word()
                print('Wrong!')

            word.display_hangman()
            print(' '.join(word.fill()))

        # Guessing the whole word
        else:
            word.guessed_word(guess)
            word.display_hangman()
            print(' '.join(word.fill()))

        counter += 1


if __name__ == '__main__':
    main()


# TODO:
#   - Line 39: the game does not end if the word contains multiples of the same letter
#     and the user guesses all of them (ex: 'viking' does not register both the 'i')
#       >> maybe multiply the guessed letter by the number of times it appears in the word,
#          and also sort the letters alphabetically so that order does not matter
