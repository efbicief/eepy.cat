from ascii_magic import AsciiArt
from os import listdir
for f in listdir("cats"):
    my_art = AsciiArt.from_image(f'cats/{f}')
    my_art.to_html_file(f'ascii/{f}.html', monochrome=False, columns=200)