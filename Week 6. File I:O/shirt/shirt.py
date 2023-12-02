import sys
from PIL import Image, ImageOps

def main():
    command_line_check()
    ps_image()

def ps_image():
    try:
        image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    else:
        shirt = Image.open("shirt.png")
        image_adjusted = ImageOps.fit(image, shirt.size)
        image_adjusted.paste(shirt,mask = shirt)
        image_adjusted.save(sys.argv[2])

def command_line_check():
    type = [".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"]
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(tuple(type)):
        sys.exit("Invalid input")
    elif not sys.argv[2].endswith(tuple(type)):
        sys.exit("Invalid output")
    elif sys.argv[1][-4:] != sys.argv[2][-4:]:
        sys.exit("Input and output have different extensions")

if __name__ == "__main__":
    main()
