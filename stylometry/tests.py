import matplotlib.pyplot as plt
import nltk

LINES = ["-", ":", "--"]


def wordlentest(authorwords, lencorpus):
    """Plot word length by author, shortening them to the shortest corpus length."""
    authorwordfrequencies = dict()
    plt.figure(1)
    plt.ion()

    for i, author in enumerate(authorwords):
        wordlengths = [len(word) for word in authorwords[author][:lencorpus]]
        authorwordfrequencies[author] = nltk.FreqDist(wordlengths)
        authorwordfrequencies[author].plot(
            15,
            linestyle=LINES[i],
            label=author,
            title="Word lengths by author",
        )
    plt.legend()
    # plt.show() Uncomment to show the plot


def stopwordstest(authorwords, lencorpus):
    """Plot stopwords frequency per author, shortening them to the shortest corpus length."""
    stopwordfrequencies = dict()
    plt.figure(2)
    stopwords = set(nltk.corpus.stopwords.words("english"))
    print(f"\nNumber of stopwords is {len(stopwords)}")
    print(stopwords)

    for i, author in enumerate(authorwords):
        authorstopwords = [
            word for word in authorwords[author][:lencorpus] if word in stopwords
        ]
        stopwordfrequencies[author] = nltk.FreqDist(authorstopwords)
        stopwordfrequencies[author].plot(
            50,
            label=author,
            linestyle=LINES[i],
            title="Most common stopwords by author",
        )
    plt.legend()
    # plt.show() Uncomment to show the plot


def speechparttest():
    pass


def vocabtest():
    pass


def jaccardtest():
    pass


if __name__ == "__main__":
    print("Please run the main app")
