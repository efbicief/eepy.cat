from ascii_magic import AsciiArt
from os import listdir
from random import shuffle

# turn images to ascii
html_fnames = []
for f in listdir("img/cats"):
    print(f'Generating {f}')
    my_art = AsciiArt.from_image(f'img/cats/{f}')
    my_art.to_html_file(f'img/ascii/{f}.html', monochrome=False, columns=200, additional_styles='font-weight: 900;')
    html_fnames.append(f'img/ascii/{f}.html')

# concatenate resulting ascii
shuffle(html_fnames)
newdoc = """<!DOCTYPE html>
    <head>
        <title>eepy cats</title>
    </head>
    <body style="background-color:#000000;">"""
for fname in html_fnames:
    print(f'Concatenating {f}')
    openfile = open(fname)
    content = openfile.readlines()[6]
    newdoc += f'<div style="text-align: center; align: center;">\n{content}</div>\n'
newdoc += """
<div style="text-align: center; align: center;">
        <a style="color: white;">submit cat pics / enviar fotos de gats: eepycats at fbcf · xyz</a>
</div>
</body>"""

# write out
print('Writing out')
with open("allcats.html", "w") as text_file:
    text_file.write(newdoc)
