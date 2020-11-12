import re
from typing import Dict

# re_opening_tag = re.compile(r'<\w+\s(.+)>')
re_opening_tag = re.compile(r'(<\w+\s(.+)/?>)')
re_attr = re.compile(r'(\w+)="(.*?)"')


def find_tag(attributes: Dict[str, str]):
    """
    Find all opening tags in file with all of the given attributes (both keys and values).
    """
    text = ''
    with open('test.xml', 'r') as f:
        text = f.read()
    tags = re_opening_tag.findall(text)
    good_tags = []
    for tag, attrs in tags:
        attr_pairs = set(re_attr.findall(attrs))
        ok = True
        for k, v in attributes.items():
            if (k, v) not in attr_pairs:
                ok = False
                break
        if ok:
            good_tags.append(tag)
    return good_tags


if __name__ == '__main__':
    for tag in find_tag({
        'where': '',
        'follow': 'true'
    }):
        print(tag)
