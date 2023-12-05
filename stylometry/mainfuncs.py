import os

import nltk
import termcolor

LINES = ["-", ":", "--"]


def welcome_message():
    print(
        termcolor.colored(
            "\nWelcome to Stylometry Author Finder!\n",
            "green",
        )
    )
    print(
        termcolor.colored(
            "This program analyzes two known author texts to suggest the most likely author of an\nunknown text. It generates three graphs depicting word lengths, stop word usage, and\nparts of speech. The final suggestion is determined through vocabulary and Jaccard\ntests. Ensure all three .txt files are in the program's directory.\n",
            "blue",
        )
    )


def get_author(n):
    if n == "unknown":
        book = input(
            termcolor.colored(
                f"Enter the name of the {n} .txt file (e.g. hyperion.txt):\n",
                "magenta",
            )
        )
        while not book or book[-4:] != ".txt" or not os.path.exists(book):
            book = input(
                termcolor.colored(
                    f"Enter a valid .txt filename:\n",
                    "red",
                )
            )
        return (n, book)
    else:
        author = input(
            termcolor.colored(
                f"Enter the name of the {n} file's author (e.g. Dan Simmons):\n",
                "magenta",
            )
        )
        book = input(
            termcolor.colored(
                f"Enter the name of the {n} .txt file (e.g. hyperion.txt):\n",
                "magenta",
            )
        )
        while not book or book[-4:] != ".txt" or not os.path.exists(book):
            book = input(
                termcolor.colored(
                    f"Enter a valid .txt file name:\n",
                    "red",
                )
            )
        return (author, book)


def read_file(filename):
    """Reads the file into a string and returns it."""
    with open(filename, encoding="utf-8", errors="ignore") as file:
        return file.read()


def make_word_dict(strings):
    """Returns a dictionary of tokenized words per corpus."""
    words = dict()
    for author in strings:
        tokens = nltk.word_tokenize(strings[author])
        words[author] = [token.lower() for token in tokens if token.isalpha()]
    return words


def find_shortest_corpus(authorwords):
    """Return the length of the shortest corpus."""
    wordcount = []
    for author in authorwords:
        currentlength = len(authorwords[author])
        wordcount.append(currentlength)
        # For testing purposes
        # print(f"\nNumber of words for {author} = {currentlength}\n")
    shortestcorpus = min(wordcount)
    # For testing purposes
    # print(f"The length of the shortest corpus is {shortestcorpus}.")
    return shortestcorpus


if __name__ == "__main__":
    print("Please run the main.py app")
