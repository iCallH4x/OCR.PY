# OCR.py
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python Version: 3.8+](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![GitHub contributors](https://img.shields.io/github/contributors/iCallH4x/OCR-PY)](https://github.com/iCallH4x/OCR-PY/graphs/contributors)

Initially created by [Crennis](https://github.com/crennis) for PCBS2 key sniping.

# Easy Usage Tutorial (*Windows*)

1. Download [tesseract-ocr](https://github.com/UB-Mannheim/tesseract/wiki). The file should be at the top of the page, named *similar* to tesseract-ocr-w64-setup-vxxxxxxxxx.exe. Make sure you download the correct version for your machine (generally 64bit).
2. Run the installer and just press next the whole way through. DO NOT CHANGE THE INSTALL LOCATION OR THE SCRIPT WILL NOT WORK
3. Download the latest pre-built OCR.py binary from [releases](https://github.com/iCallH4x/OCR-PY/releases)
4. Run the file
5. Profit

This is the easiest *pretty much* one-click way to run the script if you lack the technical know-how. If you do have the technical knowhow, read below!

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
