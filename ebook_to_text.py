import sys
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup


def epub_to_text(path, out_file):
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head',
        'input',
        'script',
    ]
    book = epub.read_epub(path)
    chapters = []
    for image in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        chapters.append(image.get_content())
    with open(out_file, 'w') as file:
        for c in chapters:
            output = ''
            soup = BeautifulSoup(c, 'html.parser')
            text = soup.find_all(text=True)
            for t in text:
                if t.parent.name not in blacklist:
                    output = f'{output}{t} '
            file.write(output)


if __name__ == '__main__':
    epub_to_text(sys.argv[1], sys.argv[2])

