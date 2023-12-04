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


def speechparttest(authorwords, lencorpus):
    """Plot the usage of parts of speech per author."""
    posfrequencies = dict()
    plt.figure(3)

    for i, author in enumerate(authorwords):
        authorpos = [pos[1] for pos in nltk.pos_tag(authorwords[author][:lencorpus])]
        posfrequencies[author] = nltk.FreqDist(authorpos)
        posfrequencies[author].plot(
            35,
            label=author,
            linestyle=LINES[i],
            title="PoS frquency per author",
        )
    plt.legend()
    # plt.show(block=True)


def vocabtest(authorwords):
    """Compares author vocabularies using the chi-squared statistical test."""
    chisquares = dict()
    for author in authorwords:
        if author != "unknown":
            # Combine corpus for the current author and the unknown one to find 1000 most common words.
            combinedcorpus = authorwords[author] + authorwords["unknown"]
            proportion = len(authorwords[author]) / len(combinedcorpus)
            combinedfrequency = nltk.FreqDist(combinedcorpus)
            mostcommonwords = list(combinedfrequency.most_common(1000))
            chisquared = 0

            # Calculate observed vs. expected word counts.
            for word, ccount in mostcommonwords:
                observedcount = authorwords[author].count(word)
                expectedcount = ccount * proportion
                chisquared += (observedcount - expectedcount) ** 2 / expectedcount
                chisquares[author] = chisquared
            print(f"Chi-squared for {author} = {round(chisquared, 3)}")

    mostlikelyauthor = min(chisquares, key=chisquares.get)
    print(f"Based on the vocabulary, most-likely author is {mostlikelyauthor}")


def jaccardtest():
    pass


if __name__ == "__main__":
    print("Please run the main.py app")
