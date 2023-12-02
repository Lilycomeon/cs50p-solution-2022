import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    n = input("Input: ")
    figlet = Figlet(random.choice(figlet.getFonts()))
    print(figlet.renderText(n))
elif len(sys.argv) == 2:
    sys.exit("invalid usage")
elif len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("invalid usage")
    elif sys.argv[2] not in figlet.getFonts():
        sys.exit("invalid usage")
    else:
        n = input("Input: ")
        figlet = Figlet(sys.argv[2])
        print(figlet.renderText(n))
