import nltk

nltk.download(
    ["punkt", "stopwords", "averaged_perceptron_tagger"],
    download_dir=".\\nltk_data",
)
nltk.data.path = [".\\nltk_data"]
from nltk.corpus import stopwords

if __name__ == "__main__":
    print("Please run the main app")
