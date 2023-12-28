import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower().split()
    count = 0
    for word in s:
        if word.startswith("um") and word[2:3] != "m" and word[2:].isalpha() == False:
            count = count + 1
    return count


if __name__ == "__main__":
    main()
