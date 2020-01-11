import numpy as np
from PIL import Image

# Functions to encrypt and decrypt images


def bin_to_ascii(binary):
    return bytes([(int(byte, base=2)) for byte in binary])


def get_binary_from_img(img_path):
    img = Image.open(img_path)
    print(img.size)
    img_bytes = np.array(bytearray(img.tobytes()))
    img_binary = [bin(byte)[2:].zfill(8) for byte in img_bytes]
    return img_binary


def get_least_sig_bits_ascii(string):
    byte_arr = np.array(bytearray(string, "utf-8"))
    binary = "".join([bin(byte)[2:].zfill(8) for byte in byte_arr])
    least_sigs = [binary[i] + binary[i + 1]
                  for i in range(0, len(binary) - 1, 2)]
    return least_sigs


def change_least_sigs(img_binary, least_sigs):
    for i in range(len(least_sigs)):
        sigs = least_sigs[i]
        binary = img_binary[i]
        img_binary[i] = binary[:6] + sigs
    return bin_to_ascii(img_binary)


def encrypt(img_path, message):
    img_binary = get_binary_from_img(img_path)
    least_sigs_ascii = get_least_sig_bits_ascii(message)
    new_binary = change_least_sigs(img_binary, least_sigs_ascii)
    encrypted_img = Image.frombytes("RGB", (400, 400), new_binary)
    encrypted_img.show()
