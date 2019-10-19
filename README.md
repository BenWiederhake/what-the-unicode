# what-the-unicode

> Tells you what-the-unicode is going on.

This library/executable tells you what the unicode is going on with your textfile.

Specifically, you can feed text(-ish) data in,
and get feedback about what characters are used, and which are obvious candidates for trouble.

It uses the built-in module [`unicodedata`](https://docs.python.org/3/library/unicodedata.html),
which has a hardcoded copy of the data in [the official files](ftp://ftp.unicode.org/Public/).
You can check which version got compiled into your version of python by running `python3 -c 'import unicodedata as ucd; print(ucd.unidata_version)'`.

This tool was inspired by [someone's](https://www.reddit.com/r/programming/comments/djnp8k/my_favourite_git_commit/) [favorite commit message](https://fatbusinessman.com/2019/my-favourite-git-commit), or rather the underlying bug: a non-breaking space (`U+00A0`) in a ASCII-only document.
On the broken version, the output of `collect_chars.py` ends in:

    Category "Zs":
      « » (U+0020) SPACE
      « » (U+00A0) NO-BREAK SPACE

    Some of the characters used bit 7, i.e., need bytes between 0x80 and 0xff.

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [TODOs](#todos)
- [NOTDOs](#notdos)
- [Contribute](#contribute)

## Install

TODO, but probably nothing.

## Usage

Just use it!  No dependencies, and it's short enough.

TODO?

### Example: Single file

For example, on this file you get the following output:

    == Analysis for README.md ==

    Category "Cc":
      «?» (U+000A) NO NAME

    Category "Ll":
      «a» (U+0061) LATIN SMALL LETTER A
      «b» (U+0062) LATIN SMALL LETTER B
      «c» (U+0063) LATIN SMALL LETTER C
      «d» (U+0064) LATIN SMALL LETTER D
      «e» (U+0065) LATIN SMALL LETTER E
      «f» (U+0066) LATIN SMALL LETTER F
      «g» (U+0067) LATIN SMALL LETTER G
      «h» (U+0068) LATIN SMALL LETTER H
      «i» (U+0069) LATIN SMALL LETTER I
      «j» (U+006A) LATIN SMALL LETTER J
      «k» (U+006B) LATIN SMALL LETTER K
      «l» (U+006C) LATIN SMALL LETTER L
      «m» (U+006D) LATIN SMALL LETTER M
      «n» (U+006E) LATIN SMALL LETTER N
      «o» (U+006F) LATIN SMALL LETTER O
      «p» (U+0070) LATIN SMALL LETTER P
      «r» (U+0072) LATIN SMALL LETTER R
      «s» (U+0073) LATIN SMALL LETTER S
      «t» (U+0074) LATIN SMALL LETTER T
      «u» (U+0075) LATIN SMALL LETTER U
      «v» (U+0076) LATIN SMALL LETTER V
      «w» (U+0077) LATIN SMALL LETTER W
      «x» (U+0078) LATIN SMALL LETTER X
      «y» (U+0079) LATIN SMALL LETTER Y

    Category "Lu":
      «A» (U+0041) LATIN CAPITAL LETTER A
      «B» (U+0042) LATIN CAPITAL LETTER B
      «C» (U+0043) LATIN CAPITAL LETTER C
      «D» (U+0044) LATIN CAPITAL LETTER D
      «E» (U+0045) LATIN CAPITAL LETTER E
      «F» (U+0046) LATIN CAPITAL LETTER F
      «G» (U+0047) LATIN CAPITAL LETTER G
      «H» (U+0048) LATIN CAPITAL LETTER H
      «I» (U+0049) LATIN CAPITAL LETTER I
      «J» (U+004A) LATIN CAPITAL LETTER J
      «K» (U+004B) LATIN CAPITAL LETTER K
      «L» (U+004C) LATIN CAPITAL LETTER L
      «M» (U+004D) LATIN CAPITAL LETTER M
      «N» (U+004E) LATIN CAPITAL LETTER N
      «O» (U+004F) LATIN CAPITAL LETTER O
      «P» (U+0050) LATIN CAPITAL LETTER P
      «Q» (U+0051) LATIN CAPITAL LETTER Q
      «R» (U+0052) LATIN CAPITAL LETTER R
      «S» (U+0053) LATIN CAPITAL LETTER S
      «T» (U+0054) LATIN CAPITAL LETTER T
      «U» (U+0055) LATIN CAPITAL LETTER U
      «V» (U+0056) LATIN CAPITAL LETTER V
      «W» (U+0057) LATIN CAPITAL LETTER W
      «X» (U+0058) LATIN CAPITAL LETTER X
      «Y» (U+0059) LATIN CAPITAL LETTER Y
      «Z» (U+005A) LATIN CAPITAL LETTER Z

    Category "Nd":
      «0» (U+0030) DIGIT ZERO
      «1» (U+0031) DIGIT ONE
      «2» (U+0032) DIGIT TWO
      «3» (U+0033) DIGIT THREE
      «4» (U+0034) DIGIT FOUR
      «5» (U+0035) DIGIT FIVE
      «6» (U+0036) DIGIT SIX
      «7» (U+0037) DIGIT SEVEN
      «8» (U+0038) DIGIT EIGHT
      «9» (U+0039) DIGIT NINE

    Category "Pc":
      «_» (U+005F) LOW LINE

    Category "Pd":
      «-» (U+002D) HYPHEN-MINUS

    Category "Pe":
      «)» (U+0029) RIGHT PARENTHESIS
      «]» (U+005D) RIGHT SQUARE BRACKET

    Category "Pf":
      «»» (U+00BB) RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK

    Category "Pi":
      ««» (U+00AB) LEFT-POINTING DOUBLE ANGLE QUOTATION MARK

    Category "Po":
      «!» (U+0021) EXCLAMATION MARK
      «"» (U+0022) QUOTATION MARK
      «#» (U+0023) NUMBER SIGN
      «'» (U+0027) APOSTROPHE
      «*» (U+002A) ASTERISK
      «,» (U+002C) COMMA
      «.» (U+002E) FULL STOP
      «/» (U+002F) SOLIDUS
      «:» (U+003A) COLON
      «;» (U+003B) SEMICOLON
      «?» (U+003F) QUESTION MARK

    Category "Ps":
      «(» (U+0028) LEFT PARENTHESIS
      «[» (U+005B) LEFT SQUARE BRACKET

    Category "Sk":
      «`» (U+0060) GRAVE ACCENT

    Category "Sm":
      «+» (U+002B) PLUS SIGN
      «=» (U+003D) EQUALS SIGN
      «>» (U+003E) GREATER-THAN SIGN

    Category "Zs":
      « » (U+0020) SPACE
      « » (U+00A0) NO-BREAK SPACE

    Some of the characters used bit 7, i.e., need bytes between 0x80 and 0xff.


## TODOs

Next up are these:
* Check whether `READ_INCREMENT` fulfills its purpose, or should be 1, or should be 16 MiB, or whatever.
* Check entire directory tree. (Or maybe not?)
* Ship with a "custom" download of unicodedata, thus having two backends.
* Tests?
  * handwritten
  * https://github.com/minimaxir/big-list-of-naughty-strings/
  * Find https://github.com/alphagov/govuk-puppet/commit/63b36f93bf75a848e2125008aa1e880c5861cf46
* Machine-readable output format?

## NOTDOs

Here are some things this project will definitely not do:
* Reimplement just for efficiency.  (Efficiency is great, just don't reduce the usability!)

## Contribute

Feel free to dive in! [Open an issue](https://github.com/BenWiederhake/what-the-unicode/issues/new) or submit PRs.
