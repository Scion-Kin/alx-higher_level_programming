#!/usr/bin/python3
write_file = __import__('1-write_file').write_file
printer = __import__('0-read_file').read_file

nb_characters = write_file("my_file_0.txt", "This School is so cool!\n")
print(nb_characters)
printer("my_file_0.txt")
