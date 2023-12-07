# StylometryGuess

StylometryGuess analyzes known author texts given by the user to suggest the most likely author of an unknown text. It generates three graphs depicting word lengths, stop word usage, and parts of speech. The final suggestion is determined through vocabulary and Jaccard tests.

The program uses [NLTK](https://www.nltk.org/) for corpus analysis and [MatPlotLib](https://matplotlib.org/) for plotting.

![image](https://i.imgur.com/MPHEPIk.png)

![image](https://i.imgur.com/K0n7u4F.png)

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

The program comes with three .txt book files for testing:  
hound.txt - The Hound of the Baskervilles by Arthur Conan Doyle  
war.txt - The War of the Worlds by H. G. Wells  
frankenstein.txt - Frankenstein by Mary Shelley  

```python
python ./main.py
```

## Contributing

Pull requests are very welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

The program is licensed under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) and is free to download, use or distribute.