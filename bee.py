#! /usr/bin/env python3

import argparse
import os
import readline

from scraper import fetch_chars

DICT_PATH = "/usr/share/dict/words"
DASH_LEN = 10


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


def read_outers():
    def prompt():
        return str(input("outers> "))

    def is_valid(outers):
        return len(outers) == 6 and outers.isalpha()

    outers = None

    while not outers:
        outers = prompt()

        if is_valid(outers):
            outers = outers.lower()
        else:
            outers = None

    return outers


def can_be_formed(word, center, outers):
    return center in word and (set(word) - {center}).issubset(outers)


def is_pangram(word, center, outers):
    return can_be_formed(word, center, outers) and set(word) == set(outers) | {center}


def format_word(word, center):
    formatted_word = []
    for letter in word:
        if letter == center:
            formatted_word.append(letter.upper())
        else:
            formatted_word.append(letter)
    return "".join(formatted_word)


def print_valid_words(valid_words, center, outers):
    for valid_word in valid_words:
        if is_pangram(valid_word, center, outers):
            print(valid_word.upper())
        else:
            print(format_word(valid_word, center))


def print_dashes():
    print("-" * DASH_LEN)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog=os.path.basename(__file__))
    parser.add_argument("-d", "--dict", help="use dictionary at this path")
    parser.add_argument("-l", "--live", action="store_true", help="solves today's live puzzle")

    args = parser.parse_args()

    DICT_PATH = args.dict if args.dict is not None else DICT_PATH
    dictionary = read_dict(DICT_PATH)

    if args.live:
        center, outers = fetch_chars()
    else:
        center = read_center()
        outers = read_outers()

    valid_words = []
    for word in dictionary:
        if len(word) >= 4 and can_be_formed(word, center, outers):
            valid_words.append(word)
    valid_words.sort()

    print(f"center = {center}")
    print(f"outers = {outers}")

    print_dashes()

    print_valid_words(valid_words, center, outers)

    print_dashes()

    print(f"Found {len(valid_words)} words")
