import numpy as np
import math
import os
from PIL import Image

# Functions to encrypt and decrypt images

# Conversion functions


def to_binary_str(ascii_str):
    return [bin(char)[2:].zfill(8) for char in bytearray(ascii_str, "utf-8")]


def to_binary(num):
    return bin(num)[2:].zfill(8)


def to_num(binary):
    return int(binary, base=2)


def to_dec_arr(bin_arr):
    return [to_num(byte) for byte in bin_arr]


def get_least_sig_bits(byte_arr):
    bits = "".join(byte_arr)
    least_sig_bits = [bits[i] + bits[i + 1]
                      for i in range(0, len(bits) - 1, 2)]
    return least_sig_bits


def get_binary_from_img(img_path):
    img = Image.open(img_path)
    img_binary = [to_binary(num) for num in np.array(bytearray(img.tobytes()))]
    return img_binary


def get_binary_from_str(string):
    return to_binary_str(string)


def encode_size(img_binary, string):
    size = len(string)
    size_bin = to_binary(size)
    print("size -> " + str(size))
    least_sig_bits = get_least_sig_bits([size_bin])
    print(least_sig_bits)
    for i in range(4):
        img_binary[i] = img_binary[i][0:-2] + least_sig_bits[i]


def encode_message(img_binary, string):
    str_binary = get_binary_from_str(string)
    least_sig_bits = get_least_sig_bits(str_binary)
    print("str binary: -> " + string)
    print(least_sig_bits)
    for i in range(4, int(4 + (len(string) * 8)/2)):
        sig = least_sig_bits[i - 4]
        img_binary[i] = img_binary[i][0:-2] + sig
        print(img_binary[i])


def create_img_array(img_binary):
    return bytes(img_binary)

# Encryption functions


def encrypt(img_path, message):
    img = Image.open(img_path)
    img_binary = get_binary_from_img(img_path)
    encode_size(img_binary, message)
    encode_message(img_binary, message)
    print(img_binary[0: 8])
    dec_lst_bytes = to_dec_arr(img_binary)
    img_array = create_img_array(dec_lst_bytes)
    print(img_array)
    encoded_img = Image.frombytes("RGB", (400, 400), img_array)
    encoded_img.save("./encoded_img.png")
    encoded_img.show()


# Decryption functions
def get_size(img_path):
    img = Image.open(img_path)
    img_binary = np.asarray(img)
    print(img_binary)


def decrypt(img_path):
    get_size(img_path)
