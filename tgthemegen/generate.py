import re
import random
import tgthemegen


class ColorParseError(Exception):
    def __init__(self, color: str):
        super().__init__('invalid color literal: {}'.format(color))


class Color:

    color_regex = re.compile(r'^[0-9a-fA-F]{6,8}$')

    def __init__(self, red: int, green: int, blue: int, alpha: int=None):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    @classmethod
    def parse(cls, s: str):
        s = s.strip('#')
        if cls.color_regex.match(s): 
            i = int(s, base=16)
            if len(s) == 6:
                return Color(red=(i & 0xff0000) >> 16,
                             green=(i & 0x00ff00) >> 8,
                             blue=(i & 0x0000ff))
            elif len(s) == 8:
                return Color(red=(i & 0xff000000) >> 24,
                             green=(i & 0x00ff0000) >> 16,
                             blue=(i & 0x0000ff00) >> 8,
                             alpha=(i & 0x000000ff))
            else:
                raise ColorParseError(s)
        else:
            raise ColorParseError(s)

    def __repr__(self):
        return f'<{self.__class__.__name__} {str(self)}>'  # self.ты('пидор')

    def __str__(self):
        if self.alpha is not None:
            return f'#{self.red:02x}{self.green:02x}{self.blue:02x}{self.alpha:02x}'
        else:
            return f'#{self.red:02x}{self.green:02x}{self.blue:02x}'


def generate(primary: Color, accent: Color, background: Color) -> (str, str):
    for (key, value) in tgthemegen.properties.items():
        yield (key, value if type(value) else value.calculate(primary, accent))
