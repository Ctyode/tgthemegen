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
    parser.add_argument('--tiled')
    parser.add_argument('--background')
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    img_source = args.tiled or args.background
    here = os.path.dirname(os.path.abspath(__file__))
    with zipfile.ZipFile('{}.tdesktop-theme'.format(args.out), 'w') as myzip:
        myzip.write(img_source, arcname=(('tiled' if args.tiled else 'background') + os.path.splitext(img_source)[1]))
        myzip.writestr('colors.tdesktop-theme',
                       '\n'.join(list(map(lambda x: '{}: {};'.format(x[0], x[1]),
                                          generate(primary=Color.parse(args.color_primary),
                                                   accent=Color.parse(args.color_accent),
                                                   background=Color.parse(args.color_background)).items()))))
