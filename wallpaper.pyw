import ctypes
import random
import os, os.path

SPI_SETDESKWALLPAPER = 20
folderName = str(" ".join(
    os.listdir("C:/Users/Jamuna/AppData/Roaming/Mozilla/Firefox/Profiles/tfjp59z9.default/tabtrekker/images/")))
numfiles = next(os.walk("C:/Users/Jamuna/AppData/Roaming/Mozilla/Firefox/Profiles/tfjp59z9.default/tabtrekker/images/{0}".format(folderName)))[2]

numfiles = len(numfiles)

wallpaperNumber = str(random.randint(1, numfiles - 1))
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0,
                                           "C:/Users/Jamuna/AppData/Roaming/Mozilla/Firefox/Profiles/tfjp59z9.default/tabtrekker/images/{0}/{1}.jpg".format(
                                               folderName, wallpaperNumber), 0)
