import matplotlib.pyplot as plt
import nltk
import termcolor

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

    # For testing purposes
    # print(f"\nNumber of stopwords is {len(stopwords)}")
    # print(stopwords)

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
            title="Parts of speech frequency per author",
        )
    plt.legend()
    plt.show(block=True)


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
            # For testing purposes
            # print(f"Chi-squared for {author} = {round(chisquared, 2)}")

    mostlikelyauthor = min(chisquares, key=chisquares.get)
    print(
        termcolor.colored(
            f"\n\nBased on the vocabulary, most-likely author is {mostlikelyauthor}.",
            "green",
            attrs=["reverse"],
        )
    )


def jaccardtest(authorwords, lencorpus):
    """Calculate Jaccard similarity of known corpuses to the unknown one."""
    jaccard_by_author = dict()
    unique_words_unknown = set(authorwords["unknown"][:lencorpus])
    authors = (author for author in authorwords if author != "unknown")
    for author in authors:
        unique_words_author = set(authorwords[author][:lencorpus])
        shared_words = unique_words_author.intersection(unique_words_unknown)
        jaccard_sim = float(len(shared_words)) / (
            len(unique_words_author) + len(unique_words_unknown) - len(shared_words)
        )
        jaccard_by_author[author] = jaccard_sim
        # For testing purposes
        # print(f"Jaccard similarity for {author} = {jaccard_sim}")

    mostlikelyauthor = max(jaccard_by_author, key=jaccard_by_author.get)
    print(
        termcolor.colored(
            f"Based on the Jaccard similarity, most-likely author is {mostlikelyauthor}",
            "yellow",
            attrs=["reverse"],
        )
    )


if __name__ == "__main__":
    print("Please run the main.py app")
