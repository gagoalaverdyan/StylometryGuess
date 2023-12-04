import nltk

LINES = ["-", ":", "--"]


def readfile(filename):
    """Reads the file into a string and returns it."""
    with open(filename, encoding="utf-8", errors="ignore") as file:
        return file.read()


def makeworddict(strings):
    """Returns a dictionary of tokenized words per corpus."""
    words = dict()
    for author in strings:
        tokens = nltk.word_tokenize(strings[author])
        words[author] = [token.lower() for token in tokens if token.isalpha()]
    return words


def findshortestcorpus(authorwords):
    """Return the length of the shortest corpus."""
    wordcount = []
    for author in authorwords:
        currentlength = len(authorwords[author])
        wordcount.append(currentlength)
        print(f"\nNumber of words for {author} = {currentlength}\n")
    shortestcorpus = min(wordcount)
    print(f"The length of the shortest corpus is {shortestcorpus}.")
    return shortestcorpus


if __name__ == "__main__":
    print("Please run the main app")
