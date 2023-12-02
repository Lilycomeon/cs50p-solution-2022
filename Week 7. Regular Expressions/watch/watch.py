import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
   if matches := re.search(r'<(?:.+)src="https?://(?:www\.)?youtube\.com/embed/([a-z0-9_]+)"', s, re.IGNORECASE):
        resulting = "https://youtu.be/" + matches.group(1)
        return resulting

if __name__ == "__main__":
    main()