# what-the-unicode

> Tells you what-the-unicode is going on.

This library/executable tells you what the unicode is going on with your textfile.

Specifically, you can feed text(-ish) data in,
and get feedback about what characters are used, and which are obvious candidates for trouble.

It uses the built-in module [`unicodedata`](https://docs.python.org/3/library/unicodedata.html),
which has a hardcoded copy of the data in [the official files](ftp://ftp.unicode.org/Public/).
You can check which version got compiled into your version of python by running `python3 -c 'import unicodedata as ucd; print(ucd.unidata_version)'`.

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

TODO

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
