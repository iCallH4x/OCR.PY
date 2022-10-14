# OCR-PY
Originally created by Crennis for PCBS2 stream

Tutorial: https://www.youtube.com/watch?v=hjUjylNEtNY&t=1s

# Requirements - Windows
You will need [Python3.8 or higher](https://www.python.org/downloads/) to run this

To install the required packages, run:
```py
py -m pip install -r requirements.txt
```
You will also need to download and install [tesseract-ocr](https://github.com/UB-Mannheim/tesseract/wiki)

# Requirements - Linux
To install the required packages, run:
```bash
python3.8 -m pip install -r requirements.txt
```
You will also need to download and install tesseract-ocr with your chosen package manager, for example:
```bash
sudo apt install tesseract
```
# Script difference

The scripts with the suffix -old are the versions as seen in the video. The scripts without -old are currently experimental but will have more QoL features, such as regex string verification and a grayscale window to clearly view the key.
