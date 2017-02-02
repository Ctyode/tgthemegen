import binascii
import tgthemegen
from tgthemegen import clamp


class ColorParseError(Exception):
    def __init__(self, color: str):
        super().__init__('invalid color literal: {}'.format(color))


class Color:
    def __init__(self, red: float, green: float, blue: float, alpha: float):
        self.__red = clamp(red)
        self.__green = clamp(green)
        self.__blue = clamp(blue)
        self.__alpha = clamp(alpha)

    @property
    def red(self):
        return self.__red

    @property
    def green(self):
        return self.__green

    @property
    def blue(self):
        return self.__blue

    @property
    def alpha(self):
        return self.__alpha

    @property
    def channels(self):
        return self.__red, self.__green, self.__blue, self.__alpha

    @property
    def bytes(self):
        return bytes([int(c * 255) for c in self.channels])

    def __str__(self):
        return '#' + binascii.hexlify(self.bytes).decode()

    @staticmethod
    def from_channels(channels):
        return Color(red=channels[0],
                     green=channels[1],
                     blue=channels[2],
                     alpha=channels[3])


def generate(primary: Color, accent: Color, foreground: Color, background: Color) -> (str, str):
    for (key, value) in tgthemegen.properties.items():
        yield (key, value if type(value) else value.calculate(primary, accent, foreground, background))
