import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes):
    print(STAGES[mistakes])


def find_word_state(printed_word, index_list, user_char):
    list_word = printed_word.split(" ")
    if not index_list:
        return printed_word
    for index in index_list:
        list_word[index] = user_char
    new_printed_word = " ".join(list_word)
    return new_printed_word


def find_occurences(word, user_char):
    index_list = [i for i, char in enumerate(word) if char == user_char]
    return index_list


def prepare_game(secret_word):
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)
    print(STAGES[0])
    length_secret_word = len(secret_word)
    printed_word = "_ " * length_secret_word
    print(f"Word: {printed_word}")
    return printed_word


def play_game():
    secret_word = get_random_word()
    printed_word = prepare_game(secret_word)
    mistakes = 0
    while True:
        user_char = input("\nGuess a letter: ").lower()
        index_list = find_occurences(secret_word, user_char)
        if not index_list:
            mistakes += 1
        display_game_state(mistakes)
        printed_word = find_word_state(printed_word, index_list, user_char)

        print(f"Word: {printed_word}")
        if mistakes == 3:
            print(f"Game over! The word was {secret_word}")
            break
        if printed_word.replace(" ", "") == secret_word:
            print("\nYou win! 🎉 \nThe snowman ist save now!\n Thank you!")
            break


if __name__ == "__main__":
    play_game()
