import sys
import stegapy as stp

img_path = "image.jpg"
message = "Hello my name is eric chen and I go the high school for math science and engineering"


def main():
    stp.encrypt(img_path, message)


main()
