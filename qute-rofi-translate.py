#!/usr/bin/env python

import sys
import re
import sh

TARGET_LANG = "en"
MAX_LEN_PER_PAGE = 700


def split_text(text):
    sentences = re.split(r"(?<=[.!?]) +", text)

    segments = []
    current_segment = ""

    for sentence in sentences:
        if len(current_segment) + len(sentence) + 1 <= MAX_LEN_PER_PAGE:
            if current_segment:
                current_segment += " " + sentence
            else:
                current_segment = sentence
        else:
            segments.append(current_segment)
            current_segment = sentence

    if current_segment:
        segments.append(current_segment)

    return segments


def main():
    text = " ".join(sys.argv[1:])

    translated_text = sh.trans("-b", f":{TARGET_LANG}", text).stdout.strip("\n").strip()

    pages = split_text(translated_text)

    for page in pages:
        if page:
            sh.rofi("-e", page)


if __name__ == "__main__":
    main()
