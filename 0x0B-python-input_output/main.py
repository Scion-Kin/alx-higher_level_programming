#!/usr/bin/python3
write_file = __import__('1-write_file').write_file
printer = __import__('0-read_file').read_file
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("my_file_0.txt", "This School is so cool!\n")
nb_characters = write_file("my_file_0.txt", "This School is so cool!\n")
print(nb_characters)
print(nb_characters_added)
printer("my_file_0.txt")
