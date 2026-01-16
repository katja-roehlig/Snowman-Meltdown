import random
from snowman_stages import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    pass


def find_occurences(secret_word, user_char):
    # amount = secret_word.count(user_char)
    index_list = [i for i, char in enumerate(secret_word) if char == user_char]
    return index_list


print(find_occurences("canada", "x"))


# def play_game():
#     secret_word = get_random_word()
#     print("Welcome to Snowman Meltdown!")
#     print("Secret word selected: " + secret_word)  # for testing, later remove this line
#     print(STAGES[0])
#     length_secret_word = len(secret_word)
#     printed_word = "_ " * length_secret_word
#     print(f"Word: {printed_word}")
#     guess = input("\nGuess a letter: ").lower()
#     # print("You guessed:", guess)
#     mistakes = 0
#     index = secret_word.find(guess)
#     if index == -1:
#         mistakes += 1
#     print(STAGES[mistakes])
#     print(f"Word: {'_ '*index}{guess} {'_ '* (length_secret_word - index -1)}")


# if __name__ == "__main__":
#     play_game()
