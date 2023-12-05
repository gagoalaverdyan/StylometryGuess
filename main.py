from stylometry.mainfuncs import *
from stylometry.tests import *


def main():
    # Welcome the user and get the required information
    welcome_message()
    first_author, first_file = get_author("first")
    second_author, second_file = get_author("second")
    unknown_author, unknown_file = get_author("unknown")

    # Store the corpuses as strings
    author_strings = dict()
    author_strings[first_author] = read_file(first_file)
    author_strings[second_author] = read_file(second_file)
    author_strings[unknown_author] = read_file(unknown_file)
    author_words = make_word_dict(author_strings)
    shortest_corpus_len = find_shortest_corpus(author_words)

    # Run the tests and find the author
    wordlentest(author_words, shortest_corpus_len)
    stopwordstest(author_words, shortest_corpus_len)
    speechparttest(author_words, shortest_corpus_len)
    vocabtest(author_words)
    jaccardtest(author_words, shortest_corpus_len)


if __name__ == "__main__":
    main()
