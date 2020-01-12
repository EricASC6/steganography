import sys
import stegapy as stp
import time


args = sys.argv
img_path = args[2]


def encrypt():
    img_path = args[2]
    message = input("Enter your secret message: ")
    stp.encrypt(img_path, message)


def decrypt():
    img_path = args[2]
    stp.decrypt(img_path)


def start():
    flag = args[1]
    if flag == "-h":
        encrypt()
    elif flag == "-d":
        decrypt()
    else:
        print("Invalid flag")


def main():
    start()


if __name__ == "__main__":
    main()
