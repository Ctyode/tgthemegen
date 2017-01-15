import tgthemegen
import random


class ColorParseError(Exception):

    def __init__(self, color: str):
        super().__init__(self, 'bad color literal: {}'.format(color))


class Color:

    def __init__(self, red: int, green: int, blue: int, alpha: int=0xFF):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    @staticmethod
    def parse(s: str):
        s = s.strip('#')
        s = (s + 'ff') if len(s) == 6 else s
        if len(s) != 8:
            raise ColorParseError(s)
        i = int(s, base=16)

        return Color(red=(i & 0xff000000) >> 24,
                     green=(i & 0x00ff0000) >> 16,
                     blue=(i & 0x0000ff00) >> 8,
                     alpha=(i & 0x000000ff))

    def __repr__(self):
        return ('<{} {}>'.format(self.__class__.__name__, str(self)))

    def __str__(self):
        return ('#{:x}{:x}{:x}{:x}'
                .format(self.red, self.green, self.blue, self.alpha))


def generate(primary: Color, accent: Color, background: Color) -> dict:
    return dict(map(
        lambda x: (x, random.choice([primary, accent, background])),
        tgthemegen.properties))
