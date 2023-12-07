# StylometryGuess

StylometryGuess analyzes two known author texts to suggest the most likely author of an unknown text. It generates three graphs depicting word lengths, stop word usage, and parts of speech. The final suggestion is determined through vocabulary and Jaccard tests.

The program uses [NLTK](https://www.nltk.org/) for corpus analysis and [MatPlotLib](https://matplotlib.org/) for plotting.

![image](https://i.imgur.com/BzkyXYv.png)

![image](https://i.imgur.com/z7NTQK5.png)

## Installation

It is recommended to the program in a virtual environment since it has multiple requirements.

```bash
mkdir stylometry
cd stylometry
git clone https://github.com/gagoalaverdyan/StylometryGuess.git .
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```

## Usage

```python
python ./main.py
```

## Contributing

Pull requests are very welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

The program is licensed under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) and is free to download, use or distribute.