# Exercise 2
# Create a module called utils.py and put the following functions inside:
import os.path 
from os import path
from sys import argv
import csv
import platform
import argparse
from exercise1 import write_list_to_file
# first function takes a path to a folder and writes all filenames in the folder to a specified output file


def write_filenames_to_file(filename, path):
    entries = os.listdir(path)
    write_list_to_file(filename, entries)

# second takes a path to a folder and write all filenames recursively (files of all sub folders to)

my_set = {}
def write_filenames_to_file_recursively(filename, path):
    entries = os.listdir(path)
    for entry in entries:
        if os.path.isdir(entry):
            write_filenames_to_file_recursively(entry)
        else:
            my_set.add(entry)
            write_filenames_to_file_recursively

# third takes a list of filenames and print the first line of each
# fourth takes a list of filenames and print each line that contains an email (just look for @)
# fifth takes a list of md files and writes all headlines (lines starting with a hashtag) to a file 
# Make sure your module can be called both from cli and imported to another module Create a new module that imports utils.py and test each function.


def run():
    if args.write_filenames_to_file:
        filename = argv[2]
        path = argv[3]
        write_filenames_to_file(filename,path)
    if args.write_filenames_to_file_recursively:
        filename = argv[2]
        path = argv[3]
        write_filenames_to_file(filename,path)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Homemade handler of files")
    parser.add_argument("--write_filenames_to_file", nargs='*', help="Write filenames to file")
    parser.add_argument("--write_filenames_to_file_recursively", nargs='*', help="Write filenames to file")
    args = parser.parse_args()
    run()