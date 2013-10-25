from font import Font, FontLoader
from textdrawer import TextDrawer

def getText():
    return 'Git'

class Font:
    pass

class FontLoader:
    def loadFont(self,directory):
        pass


text = getText()
font = FontLoader().loadFont('fancyFont/')
drawer = TextDrawer()
drawer.setFont(font)
drawer.draw(text)
