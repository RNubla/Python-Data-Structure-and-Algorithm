# bit vector is a list of bits

import mmh3
import fnv

bit_vector = [0] * 20

# fnv_Pika = fnv.hash("Pikachu", algorithm=fnv.fnv, bits=64)
# fnv_Char = fnv.hash("Charmander", algorithm=fnv.fnv) % 20

murmur_Pika = mmh3.hash("Pikachu") % 20
murmur_Char = mmh3.hash("Charmander") % 20

# print(fnv_Pika)
# print(fnv_Char)

print(murmur_Pika)
print(murmur_Char)

bit_vector[murmur_Pika] = 1
bit_vector[murmur_Char] = 1

print(bit_vector)
