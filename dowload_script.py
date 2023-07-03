import os, time


# Use pip to download and install modules

list_of_modules =["urllib3","numpy","discord.py",
                  "beautifulsoup4","request","json",
                  "difflib","randfacts","nltk","cdifflib"]


for downloads in list_of_modules:
    time.sleep(10)
    os.system(f'pip install {downloads}')

nltk.download()
