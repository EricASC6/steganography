import sys
import stegapy as stp
import time

img_path = "image.jpg"
encoded_img_path = "./encoded_img.jpg"
message = "Hello my name is eric chen and I go the high school for math science and engineering"


def main():
    stp.encrypt(img_path, message)
    # stp.decrypt(encoded_img_path)


main()
