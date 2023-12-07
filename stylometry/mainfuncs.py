import os

import nltk
from termcolor import colored

LINES = ["-", ":", "--"]


def welcome_message():
    print(
        "\n\n\n",
        "      ______ ______",
        f"    _/      Y      \\_	    {colored("Welcome to StylometryGuess", "green")}",
        "   // ~~ ~~ | ~~ ~  \\\\",
        f"  // ~ ~ ~~ | ~~~ ~~ \\\\     {colored("Find the author of the unknown text", "yellow")}",
        f" //________.|.________\\\\    {colored("by analyzing the known ones.", "yellow")}",
        "`----------`-'----------', ",
        sep="\n",
    )

def get_known_corpuses():
    """Receive how many known corpuses will be analyzed and return the number."""
    while True:
        n = input(colored("Enter the number of books and authors to analyze (e.g. 4):\n", "green"))
        try:
            n = int(n)
            if n >= 2:
                return n
            else:
                print(colored("The number must be 2 or more.", "red"))
        except ValueError:
            print(colored("Please enter a valid integer.", "red"))

def get_author(n):
    """Get the information for the n-th author"""
    if n == "unknown":
        while True:
            book = input(
                colored(
                    f"Enter the name of the {n} .txt file (e.g. hyperion.txt):\n",
                    "green",
                )
            )
            if not book or book[-4:] != ".txt" or not os.path.exists(book):
                print(colored("Enter a valid .txt filename:\n", "red"))
            else:
                return (n, book)
    else:
        author = input(
            colored(
                f"Enter the name of the author of file # {n+1} (e.g. Dan Simmons):\n",
                "green",
            )
        )
        while True:
            book = input(
                colored(
                    f"Enter the name of the .txt file # {n+1} (e.g. hyperion.txt):\n",
                    "green"
                )
            )
            if not book or book[-4:] != ".txt" or not os.path.exists(book):
                print(colored("Enter a valid .txt filename:", "red"))
            else:
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
