import random


def random_matching_letters(word):
    """
    Randomizes 10 letters in lowercase and checks for them in the word
    :param word:
    :return: total occurrences of the letters in the word
    """

    total_occurrences = 0

    for _ in range(10):
        letter = chr(random.randint(97, 123))
        total_occurrences += word.count(letter)

    return total_occurrences


city = input("Enter the Name of the City: ")

print(f"The Number of letters matched is: {random_matching_letters(city)}")
