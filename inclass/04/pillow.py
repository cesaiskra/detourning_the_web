from PIL import Image, ImageDraw, ImageFont
from sys import argv


def drawtext(filename, text):
    im = Image.open(filename)
    canvas = ImageDraw.Draw(im)

    fnt = ImageFont.truetype('/Library/Fonts/BigCaslon.ttf', 60)

    canvas.text((10, 10), text, font=fnt, fill=(0, 0, 0))

    canvas.rectangle([(100, 100), (500, 500)], fill=(255, 0, 0))

    im.save('cop.png')


drawtext(argv[1], argv[2])
