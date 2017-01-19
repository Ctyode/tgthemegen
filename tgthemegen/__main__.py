import os
import zipfile
from argparse import ArgumentParser
from tgthemegen.generate import generate, Color

# люблю всяких котиков

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--color-primary', required=True)
    parser.add_argument('--color-accent', required=True)
    parser.add_argument('--color-background', required=True)
    parser.add_argument('--tiled', action='store_true')
    parser.add_argument('--background', required=True)
    parser.add_argument('--out', required=True)
    parser.add_argument('--dark', action='store_true')
    args = parser.parse_args()
    here = os.path.dirname(os.path.abspath(__file__))
    with zipfile.ZipFile('{}.tdesktop-theme'.format(args.out), 'w') as myzip:
        myzip.write(args.background, arcname=(('tiled' if args.tiled else 'background') + os.path.splitext(args.background)[1]))
        myzip.writestr('colors.tdesktop-theme',
                       '\n'.join(list(map(lambda x: '{}: {};'.format(x[0], x[1]),
                                          generate(primary=Color.parse(args.color_primary),
                                                   accent=Color.parse(args.color_accent),
                                                   background=Color.parse(args.color_background),
                                                   dark=args.dark)))))
