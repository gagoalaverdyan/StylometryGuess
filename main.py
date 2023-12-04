from stylometry.mainfuncs import *
from stylometry.tests import *


def main():
    # Creating a dictionary and storing read lines in it
    author_strings = dict()
    author_strings["doyle"] = readfile("hound.txt")
    author_strings["wells"] = readfile("war.txt")
    author_strings["unknown"] = readfile("lost.txt")
    # Checking imported lines
    print(author_strings["doyle"][:200])
    author_words = makeworddict(author_strings)
    shortest_corpus_len = findshortestcorpus(author_words)
    wordlentest(author_words, shortest_corpus_len)
    stopwordstest(author_words, shortest_corpus_len)
    speechparttest(author_words, shortest_corpus_len)
    vocabtest(author_words)
    jaccardtest(author_words, shortest_corpus_len)


if __name__ == "__main__":
    main()
