import os
from html.parser import HTMLParser

class ImgAltParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.missing = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'img':
            attr_dict = dict(attrs)
            alt = attr_dict.get('alt', '')
            if not alt or not alt.strip():
                self.missing.append(attr_dict.get('src', ''))

def check_file(path):
    parser = ImgAltParser()
    with open(path, 'r', encoding='utf-8') as f:
        parser.feed(f.read())
    return parser.missing

def test_images_have_alt():
    html_files = ['index.html', 'thank-you.html']
    for fname in html_files:
        missing = check_file(fname)
        assert not missing, f"Images missing alt text in {fname}: {missing}"
