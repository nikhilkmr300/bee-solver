#! /usr/bin/env python3

import argparse
import os
import readline

DICT_PATH = "/usr/share/dict/words"


def cleanup_string(s):
    s = "".join([c for c in s if c.isalpha()])
    s = s.lower()

    return s


def read_dict(dict_path):
    with open(dict_path, "r") as f:
        lines = f.readlines()
        lines = [cleanup_string(line.rstrip("\n")) for line in lines]

    return sorted(list(set(lines)))


def read_center():
    def prompt():
        return str(input("center> "))

    def is_valid(center):
        return len(center) == 1 and center.isalpha()

    center = None

    while not center:
        center = prompt()

        if is_valid(center):
            center = center.lower()
        else:
            center = None

    return center


def read_chars():
    def prompt():
        return str(input("chars> "))

    def is_valid(chars):
        return len(chars) == 6 and chars.isalpha()

    chars = None

    while not chars:
        chars = prompt()

        if is_valid(chars):
            chars = chars.lower()
        else:
            chars = None

    return chars


def can_be_formed(word, center, chars):
    return center in word and (set(word) - {center}).issubset(chars)


def is_pangram(word, center, chars):
    return can_be_formed(word, center, chars) and set(word) == set(chars) | {center}


def format_word(word, center):
    formatted_word = []
    for letter in word:
        if letter == center:
            formatted_word.append(letter.upper())
        else:
            formatted_word.append(letter)
    return "".join(formatted_word)


def print_valid_words(valid_words, center, chars):
    for valid_word in valid_words:
        if is_pangram(valid_word, center, chars):
            print(valid_word.upper())
        else:
            print(format_word(valid_word, center))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog=os.path.basename(__file__))
    parser.add_argument("-d", "--dict", help="use dictionary at this path")

    args = parser.parse_args()

    DICT_PATH = args.dict if args.dict is not None else DICT_PATH
    dictionary = read_dict(DICT_PATH)

    center = read_center()
    chars = read_chars()

    valid_words = []
    for word in dictionary:
        if len(word) >= 4 and can_be_formed(word, center, chars):
            valid_words.append(word)
    valid_words.sort()

    print("-" * 10)
    print_valid_words(valid_words, center, chars)
    print("-" * 10)

    print(f"Found {len(valid_words)} words")
