"""Everyday Wonder — entry for make.fun.

Writes one line to /output/entry.txt.
The line is one sentence about a small everyday moment of wonder, at most 200 characters.
"""
import os

LINE = "The elevator doors opened on a stranger humming my favourite song, and for one floor the whole building felt like it was in on the secret."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
