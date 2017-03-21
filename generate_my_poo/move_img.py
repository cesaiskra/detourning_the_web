import os


for filename in os.listdir('./img'):
    os.rename('./img/' + filename, '/Users/chino/Google Drive/ITP/detourning the web/poo/' + filename)
