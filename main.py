from stylometry.mainfuncs import *
from stylometry.tests import *


def main():
    # Welcome the user and get the required information
    welcome_message()
    number_of_corpuses = get_known_corpuses()
    corpuses = list()
    for n in range(number_of_corpuses):
        corpuses.append(get_author(n))
    corpuses.append(get_author("unknown"))

    # Store the corpuses as strings
    author_strings = dict()
    for pair in corpuses:
        author_strings[pair[0]] = read_file(pair[1])

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
