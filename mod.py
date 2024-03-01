#!/usr/bin/python3

if __name__ == "__main__":

    """ This script assumes that you have python3 installed and
        can be executed like in the examples below:

        usage 1: ./mod.py example.py

                example.py is the target file you want to write to.
                If 'example.py' or any file type specified doesn't exist, it will be created.

        usage 2: ./mod.py *.py

                *.py specifies all the files in the current directory which 'mod.py' is located in.
                bare in mind that this will ovewrite the script file as well. To avoid it, 
                move the script file to the parent directory of the directory that contains the
                files that you want to work with and execute the script as below:

                    ./mod.py /targetDirectory/*.py
                    or
                    ./mod.py /targetDirectory/* (this writes to all the files and not just python files.)"""


    import os
    import sys

    argc = len(sys.argv)

    for i in range(1, argc):

        try:
            with open(sys.argv[i], mode="w", encoding="UTF-8") as myFile:
                myFile.write("#!/usr/bin/node\n")

        except Exception:
            help(mod)
