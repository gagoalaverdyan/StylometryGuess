# StylometryGuess

StylometryGuess analyzes two known author texts to suggest the most likely author of an unknown text. It generates three graphs depicting word lengths, stop word usage, and parts of speech. The final suggestion is determined through vocabulary and Jaccard tests.

The program uses [NLTK](https://www.nltk.org/) for corpus analysis and [MatPlotLib](https://matplotlib.org/) for plotting.

![App Screenshot](https://www.dropbox.com/scl/fi/d17oy9cvgb7fa3ojltj7m/1.png?rlkey=i8kezr14whfa5o3l4u46llclj&dl=1)

![App Screenshot](https://www.dropbox.com/scl/fi/xkto7nh9hkk191psss8gj/2.png?rlkey=w49mir96krwqvswxzdys0g0uw&dl=1)
## Installation

```bash
mkdir stylometry
cd stylometry
git clone https://github.com/gagoalaverdyan/StylometryGuess.git
```

## Usage

Recommended using the program in a virtual environment.
```python
python -m .venv
.venv/Scripts/activate
pip install -r requirements.txt
python ./main.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)