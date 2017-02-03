import binascii
import tgthemegen
from enum import Enum


def clamp(a: float, rng_min: float=0.0, rng_max: float=1.0) -> float:
    return min(rng_max, max(rng_min, a))


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
                     alpha=1.0 if len(channels) < 4 else channels[3])

    @staticmethod
    def parse(s):
        return Color.from_channels([b / 255 for b in binascii.unhexlify(s.encode()[1:])])


class ColorSource(Enum):
    primary = 0
    accent = 1
    background = 2
    foreground = 3
    predefined = 4


class ColorProperty:
    def __init__(self, source: ColorSource, color: Color=None, transform=None):
        self.source = source
        self.color = color
        self.transform = transform

    def calculate(self, primary: Color, accent: Color, foreground: Color, background: Color) -> Color:
        channels = []
        if self.source is ColorSource.primary:
            channels = primary.channels
        elif self.source is ColorSource.accent:
            channels = accent.channels
        elif self.source is ColorSource.foreground:
            channels = foreground.channels
        elif self.source is ColorSource.background:
            channels = background.channels
        return Color.from_channels([c * t for c, t in zip(channels, self.transform)])

    @staticmethod
    def from_repr(r):
        source = None
        if r[0] == 'primary':
            source = ColorSource.primary
        if r[0] == 'accent':
            source = ColorSource.accent
        if r[0] == 'background':
            source = ColorSource.background
        if r[0] == 'foreground':
            source = ColorSource.foreground
        return ColorProperty(source=source, transform=r[1])


def generate(primary: Color, accent: Color, foreground: Color, background: Color) -> (str, str):
    for (key, value) in tgthemegen.properties.items():
        yield (key, ColorProperty.from_repr(value.calculate(primary, accent, foreground, background)))
