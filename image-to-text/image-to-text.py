#sudo apt install tesseract-ocr
#pip install pytesseract

import pytesseract
import shutil
import os
import random
try:
 from PIL import Image
except ImportError:
 import Image


def getfiles(image_path_folder):
	files=[]
	for path in os.listdir(image_path_folder):
		full_path = os.path.join(image_path_folder, path)
		if os.path.isfile(full_path):
			files.append(full_path)
	#print(files)
	return files

def imtotext(image_path_file):
	image_path_file=image_path_file
	extractedInformation = pytesseract.image_to_string(Image.open(image_path_file))
	#print(extractedInformation)
	return extractedInformation

def gettext(files):
	info=[]
	for file_path in files:
		info.append(imtotext(file_path))
	return info

if __name__=="__main__":
	image_path_folder = "/content/test-data"
	files=getfiles(image_path_folder)
	info=gettext(files)
