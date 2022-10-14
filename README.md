# OCR-PY
Originally created by Crennis for PCBS2 stream

Tutorial: https://www.youtube.com/watch?v=hjUjylNEtNY&t=1s

# Easy Usage Tutorial (*Windows*)

1. Download [tesseract-ocr](https://github.com/UB-Mannheim/tesseract/wiki). The file should be at the top of the page, named *similar* to tesseract-ocr-w64-setup-vxxxxxxxxx.exe.
2. Run the installer and just press next the whole way through. DO NOT CHANGE THE INSTALL LOCATION OR THE SCRIPT WILL NOT WORK
3. Download the latest pre-built ocr.py binary from [releases](https://github.com/iCallH4x/OCR-PY/releases)
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
# Script difference

The scripts with the suffix -old are the versions as seen in the video. The scripts without -old are currently experimental but will have more QoL features, such as regex string verification and a grayscale window to clearly view the key.
