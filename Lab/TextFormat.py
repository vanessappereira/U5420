"""
Develop a program that receives text through standard input and formats it into X columns. Read all the text from standard input using the method sys.stdin.read(which we will see in the next part of the laboratory). Use the textwrap module to format the text.
"""

import sys
from textwrap import fill


def textFormat():
    if len(sys.argv) != 2:
        print("Usage: python3", sys.argv[0], "<NUM_COLUMNS>")
    else:
        txt = sys.stdin.read()
        print(fill(txt, int(sys.argv[1])))


def main():
    textFormat()


if __name__ == "__main__":
    main()
