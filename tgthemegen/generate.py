import tgthemegen
import random


class ColorParseError(Exception):

    def __init__(self, color: str):
        super().__init__(self, 'bad color literal: {}'.format(color))


class Color:

    def __init__(self, red: int, green: int, blue: int, alpha: int=None):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    @staticmethod
    def parse(s: str):
        s = s.strip('#')
        i = int(s, base=16)
        if len(s) == 6:
            return Color(red  =(i & 0xff0000) >> 16,
                         green=(i & 0x00ff00) >> 8,
                         blue =(i & 0x0000ff))
        elif len(s) == 8:
            return Color(red  =(i & 0xff000000) >> 24,
                         green=(i & 0x00ff0000) >> 16,
                         blue =(i & 0x0000ff00) >> 8,
                         alpha=(i & 0x000000ff))
        else:
            raise ColorParseError(s)

    def __repr__(self):
        return ('<{} {}>'.format(self.__class__.__name__, str(self)))

    def __str__(self):
        if self.alpha is not None:
            return ('#{:02x}{:02x}{:02x}{:02x}'
                    .format(self.red, self.green, self.blue, self.alpha))
        else:
            return ('#{:02x}{:02x}{:02x}'
                    .format(self.red, self.green, self.blue))


def generate(primary: Color, accent: Color, background: Color) -> dict:
    return dict(map(
        lambda x: (x, random.choice([primary, accent, background])),
        tgthemegen.properties))