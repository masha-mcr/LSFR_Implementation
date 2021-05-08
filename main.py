import numpy as np


def generate_key(key_size: int, reg_size: int, indexes: list):
    register = np.array([1] * reg_size)
    key = register.copy()
    while len(key) < key_size:
        new_bit = register[indexes[0]]
        for index in indexes[1:]:
            new_bit = np.bitwise_xor(new_bit, register[index])
        register = np.roll(register, 1)
        pushed_bit = register[0]
        register[0] = new_bit
        p = np.array([pushed_bit])
        key = np.append(key, p)
    return key


def convert(data: list):
    bits = np.unpackbits(np.asarray(data, dtype=np.uint8))
    key = generate_key(len(bits), 24, [0, 2, 3, 23])
    res = []
    for i in range(len(bits)):
        res.append(bits[i] ^ key[i])
    return list(np.packbits(res))


file = open('data.txt', 'rb')
content = list(file.read())
encrypted_data = convert(content)
decrypted_data = convert(encrypted_data)
print("File contents: {}\nEncrypted: {}\nDecrypted: {}".format(content, encrypted_data, decrypted_data))


