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

lst = []
def write_filenames_to_file_recursively(path):
    entries = os.listdir(path)
    for entry in entries:
        if os.path.isdir(entry):
            write_filenames_to_file_recursively(entry)
        else:
             lst.append(entry)

    write_list_to_file("test.csv", lst)

# third takes a list of filenames and print the first line of each

def read_first_line_from_files(*files):
    for file in files:
        for ele in file:
            with open(ele) as f_obj:
                content = f_obj.readline()
                print(content)

# fourth takes a list of filenames and print each line that contains an email (just look for @)

def print_lines_with_email(*files):
    for file in files:
        for ele in file:
            with open(ele) as f_obj:
                content = f_obj.readlines()
            for line in content:
                if '@' in line:
                    print(line)

# fifth takes a list of md files and writes all headlines (lines starting with a hashtag) to a file 

def print_lines_with_markdown(*files):
    for file in files:
        for ele in file:
            with open(ele) as f_obj:
                content = f_obj.readlines()
            for line in content:
                if '#' in line:
                    lst.append(line)
    write_list_to_file('test.csv', lst)

# Make sure your module can be called both from cli and imported to another module Create a new module that imports utils.py and test each function.


# def run():
#     if args.write_filenames_to_file_recursively:
#         filename = argv[2]
#         path = argv[3]
#         write_filenames_to_file_recursively(path)
#     if args.write_filenames_to_file:
#         filename = argv[2]
#         path = argv[3]
#         write_filenames_to_file(filename,path)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Homemade handler of files")
    parser.add_argument("--write_filenames_to_file", nargs='*', help="Write filenames to file")
    parser.add_argument("--write_filenames_to_file_recursively", nargs='*', help="Write filenames and folders to file")
    args = parser.parse_args()
    
    if args.write_filenames_to_file_recursively:
        path = argv[2]
        write_filenames_to_file_recursively(path)

    if args.write_filenames_to_file:
        filename = argv[2]
        path = argv[3]
        write_filenames_to_file(filename,path)


    # run()