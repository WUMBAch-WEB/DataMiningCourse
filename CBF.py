import math
import hashlib
import re


#  Functions

def add(element):
    keys = hash_func(element)
    key = 0

    for indx in range(hashing_n):
        key = int(keys[indx] % size)
        array[key] += 1


def hash_func(element):
    keys = []
    hash_object1 = hashlib.md5(element.encode())
    hash_object2 = hashlib.sha1(element.encode())
    hash_object3 = hashlib.sha224(element.encode())
    hash_object4 = hashlib.sha256(element.encode())
    hash_object5 = hashlib.sha384(element.encode())
    hash_object6 = hashlib.sha512(element.encode())
    keys.append(int(hash_object1.hexdigest(), 16))
    keys.append(int(hash_object2.hexdigest(), 16))
    keys.append(int(hash_object3.hexdigest(), 16))
    keys.append(int(hash_object4.hexdigest(), 16))
    keys.append(int(hash_object5.hexdigest(), 16))
    keys.append(int(hash_object6.hexdigest(), 16))
    return keys


def search(element):
    found = True
    keys = hash_func(element)
    key = 0

    for indx in range(hashing_n):
        key = int(keys[indx] % size)

        if (not array[key] > 0):
            found = False

    return found


def prepare_array_from_file(path_file: str):
    words_pattern = '[a-zA-Zа-яА-Я-]+'
    file = open(path_file)
    array = []
    line = file.readline()
    while line:
        for element in re.findall(words_pattern, line):
            array.append(element)
        line = file.readline()
    return array

path = 'CBF_Text.txt'
words_from_text = prepare_array_from_file(path)
expected_size = len(words_from_text)
false_positive = 0.1
size = -1 * round((expected_size * math.log(false_positive)) / (math.log(2)) ** 2)
array = [0] * size
hashing_n = round((size / expected_size) * math.log(2))

if (hashing_n > 6):
    hashing_n = 6
elif (hashing_n < 1):
    hashing_n = 1

for element in words_from_text:
    add(element)

print("   --- RESULTS --- \n")
print("Filter data:")
for i in range(0, len(array), 40):
    print(array[i:i+40])
print()
print("Filter size: ", len(array), '\n')
print("Count of used hash functions: ", hashing_n, '\n')

print("Just test for search function: ")
print("Is word 'кудряву' in filter? ", search("кудряву"))
print("Is word 'Срежу' in filter? ", search("Срежу"))
print("Is word 'Александр' in filter? ", search("Александр"))
print("Is word 'Люли-люли' in filter? ", search("Люли-люли"))


