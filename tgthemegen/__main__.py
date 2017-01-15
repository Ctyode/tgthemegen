import os
from argparse import ArgumentParser
from tgthemegen.generate import generate, Color
import zipfile

# люблю всяких котиков

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--primary-color', required=True)
    parser.add_argument('--accent-color', required=True)
    parser.add_argument('--background-color', required=True)
    parser.add_argument('--tiled', required=True)
    parser.add_argument('--background', required=True)
    args = parser.parse_args()
    here = os.path.dirname(os.path.abspath(__file__))
    with zipfile.ZipFile('name.tdesktop-theme', 'w') as myzip:
        myzip.write(os.path.join(os.getcwd(), args.background), arcname='background.jpg')
        myzip.writestr('colors.tdesktop-theme',
                       '\n'.join(list(map(lambda x: '{}: {};'.format(x[0], x[1]),
                                          generate(primary=Color.parse(args.primary_color),
                                                   accent=Color.parse(args.accent_color),
                                                   background=Color.parse(args.background_color).items())))))
