#!/usr/bin/env python3

from collections import defaultdict
import unicodedata
import sys

__version__ = '0.0.1 (unidata_version = {})'.format(unicodedata.unidata_version)

DEFAULT_TEMPLATE = '  «{codepoint}» (U+{codepoint_ord:04X}) {name}'
READ_INCREMENT = 4096  # Arbitrary buffer size


class ModuleBackend:
    def get_category(self, char):
        # These character names are uninteresting.
        return unicodedata.category(char)

    def get_name(self, char):
        try:
            return unicodedata.name(char)
        except ValueError:
            return 'NO NAME'


class CodepointSet:
    def __init__(self, backend=None):
        self.codepoints = set()
        self.read_increment = READ_INCREMENT
        self.backend = backend or ModuleBackend()

    def extend_by_str(self, the_str):
        self.codepoints.update(the_str)

    def extend_by_codepoint_set(self, codepoint_set):
        self.codepoints.update(codepoint_set.codepoints)

    def extend_by_textfile(self, fp_text):
        while True:
            buf = fp_text.read(self.read_increment)
            if not buf:
                break
            self.codepoints.update(buf)

    # def extend_by_binaryfile  # Nope

    def extend_by_filename(self, filename, encoding=None, errors=None):  # `errors='ignore'` to ignore unreadable unicode chars.
        with open(filename, 'r', encoding=encoding, errors=errors) as fp:
            self.extend_by_textfile(fp)

    def clear(self):
        self.codepoints = set()

    def get_grouped(self):
        by_category = defaultdict(set)
        for c in self.codepoints:
            by_category[self.backend.get_category(c)].add(c)
        return by_category

    def get_sorted_analysis(self):
        by_category = self.get_grouped()
        cat_names = list(by_category.keys())  # Copy
        cat_names.sort()
        result = []
        for category in cat_names:
            codepoints = list(by_category[category])  # Copy
            codepoints.sort(key=ord)
            codepoints_result = []
            for c in codepoints:
                codepoints_result.append((c, self.backend.get_name(c)))
            result.append((category, codepoints_result))
        return result


def print_analysis(sorted_analysis, template=None):
    if template is None:
        template = DEFAULT_TEMPLATE
    first_category = True
    for category_name, category_content in sorted_analysis:
        if first_category:
            first_category = False
        else:
            print()
        print('Category "{}":'.format(category_name))
        for cp_value, cp_name in category_content:
            cp_display = cp_value.encode(errors='replace').decode()  # I feel dirty.  This is for surrogates like \ud800.
            print(template.format(name=cp_name, codepoint=cp_display, codepoint_ord=ord(cp_value)))


def analyze_file(filename, encoding=None, errors=None):  # `errors='ignore'` to ignore unreadable unicode chars.
    print('== Analysis for {} ==\n'.format(filename))
    cp_set = CodepointSet()
    cp_set.extend_by_filename(filename, encoding=encoding, errors=errors)
    print_analysis(cp_set.get_sorted_analysis())


def show_universe():
    be = ModuleBackend()
    for i in range(0x110000):
        chr_i = chr(i)
        cp_display = chr_i.encode(errors='replace').decode()  # I feel dirty.  This is for surrogates like \ud800.
        print(DEFAULT_TEMPLATE.format(name=be.get_name(chr_i), codepoint=cp_display, codepoint_ord=ord(chr_i)))


def run(argv):
    if len(argv) < 2:
        print('USAGE: {} <TEXTFILES...>'.format(argv[0]), file=sys.stderr)
        exit(1)

    for filename in argv[1:]:
        analyze_file(filename)


if __name__ == '__main__':
    run(sys.argv)
