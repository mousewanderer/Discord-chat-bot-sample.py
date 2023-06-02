import os, time


# Use pip to download and install modules

list_of_modules =["urllib","numpy","discord.py",
                  "beautifulsoup4","request","json",
                  "difflib"]


for downloads in list_of_modules:
    time.sleep(2)
    os.system(f'pip install {downloads}')
