import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def get_user_input(used_letters):
    """
    validates user_input
    :return user_input
    """
    while True:
        user_input = input("\nGuess a letter: ").lower()
        if len(user_input) == 1 and user_input.isalpha():
            if user_input in used_letters:
                print("You have used this letter already!\nTake another one!")
            else:
                return user_input
        else:
            print("That was not a valid input!")


def prepare_game(secret_word):
    """
    prints the initial display
    :param secret_word
    :return printed_word
    """
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)
    print(STAGES[0])
    length_secret_word = len(secret_word)
    printed_word = "_ " * length_secret_word
    print(f"Word: {printed_word}")
    return printed_word


def find_occurences(word, user_char):
    """
    Finds out how often and where a letter appears in a word and stores the indices in a list
    :param word
    :param user_char
    :return index_list
    """
    index_list = [i for i, char in enumerate(word) if char == user_char]
    return index_list


def display_game_state(mistakes):
    """
    printed the appearance of the snowman depending on the mistakes made
    """
    print(STAGES[mistakes])


def find_word_state(printed_word, index_list, user_char):
    """
    inserts the letter guessed by the user in the correct positions in the word

    :param printed_word: the current word with any letters already inserted
    :param index_list: Beschreibung
    :param user_char: Beschreibung
    :returns the new word with the newly added letters
    """
    list_word = printed_word.split(" ")
    if not index_list:
        return printed_word
    for index in index_list:
        list_word[index] = user_char
    new_printed_word = " ".join(list_word)
    return new_printed_word


def play_game():
    """
    the framework of the game, guides the user through the game
    """
    secret_word = get_random_word()
    printed_word = prepare_game(secret_word)
    mistakes = 0
    used_letters = set()
    while True:
        user_char = get_user_input(used_letters)
        used_letters.add(user_char)
        index_list = find_occurences(secret_word, user_char)
        if not index_list:
            mistakes += 1
        display_game_state(mistakes)
        printed_word = find_word_state(printed_word, index_list, user_char)
        print(f"Word: {printed_word}")
        print("\nletters already used: ", end="")
        print(*used_letters, sep=", ")
        if mistakes == 7:
            print(f"Game over! 😵\nThe word was {secret_word}")
            break
        if printed_word.replace(" ", "") == secret_word:
            print("\nYou win! 🎉 \nThe snowman ist save now!\nThank you!")
            break
    while True:
        user_repeat = input("\nDo you wanna play again? (Y/N): ")
        if user_repeat.lower() == "y":
            play_game()
        elif user_repeat.lower() == "n":
            break


if __name__ == "__main__":
    play_game()
