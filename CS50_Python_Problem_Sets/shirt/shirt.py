from sys import argv, exit
from os import path
from PIL import Image, ImageOps


def main():
    check_argv()
    read_merge_images()


def check_argv():
    ext_list = [".jpg", ".jpeg", ".png"]
    file_name, file_ext = path.splitext(argv[1])
    file1_name, file1_ext = path.splitext(argv[2])

    if len(argv) < 3:
        exit("Too few command_line arguments")
    if len(argv) > 3:
        exit("Too many command_line arguments")
    try:
        if file_ext not in ext_list or file1_ext not in ext_list:
            exit("Not a right IMG extension file")
        if file_ext != file1_ext:
            exit("input and output have different extensions")
    except FileNotFoundError:
        exit("File does not exist")


def read_merge_images():
    shirt = Image.open("shirt.png")
    background_image = Image.open(argv[1])
    background_image = ImageOps.fit(background_image, shirt.size)
    background_image.paste(shirt, shirt)
    background_image.save(argv[2])


main()
