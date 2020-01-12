import sys
import stegapy as stp
import time

img_path = "img.jpg"
decode_path = "encoded_img.png"
message = "H"


def main():
    stp.encrypt(img_path, message)
    stp.decrypt(decode_path)


if __name__ == "__main__":
    main()
