#!/usr/bin/env python

import subprocess
import sys


TARGET_LANG = "en"


def translate(text):
    try:
        result = subprocess.run(
            ["trans", "-b", f":{TARGET_LANG}", text],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        subprocess.run(["rofi", "-e", "Translation error"])
        return None


def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    text = " ".join(sys.argv[1:])

    translated_text = translate_text(text)

    if translated_text:
        subprocess.run(["rofi", "-e", translated_text])


if __name__ == "__main__":
    main()
