import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s.strip()
    valid = re.search(
        r'^<iframe.* src="([^"]*)"',
        s,
    )
    if valid:
        newstr = valid.group(1)
        if "youtube.com/embed" in newstr:
            newstr = newstr.replace("http:", "https:")
            newstr = newstr.replace("www.", "")
            newstr = newstr.replace("be.com/embed", ".be")
            return newstr
        else:
            return None
    else:
        return None


if __name__ == "__main__":
    main()
