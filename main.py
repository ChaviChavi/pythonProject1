import re


def abbreviate(phrase):
    one = r'\b[a-zA-Z]+\b'
    pattern = fr'({one})'
    word = []
    for c in re.findall(pattern,phrase):
        word.append(c[0].upper())
        for x in c[1:]:
            if x.isupper():
                word.append(x)
    return ''.join(word)







print(abbreviate('javaScript object notation'))
