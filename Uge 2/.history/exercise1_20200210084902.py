from sys import argv
import csv
import platform
import argparse
import webget

url = 'https://raw.githubusercontent.com/ehmatthes/pcc/master/chapter_10/pi_30_digits.txt' 

def webgetFunc(url):
    print(webget.download(url))

def print_file_content(file):
    with open(file) as f_obj:
        content = f_obj.readlines()

    for line in content:
        print(line.strip().split(','))

def write_list_to_file(output_file, *lst):
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None
    
    with open(output_file, 'w', newline=newline) as file:
        output_writer = csv.writer(file)
        for ele in lst:
            output_writer.writerow(ele)

def read_csv(file):
    with open(file) as file_object:
        lines = file_object.readlines()

    for line in lines:
        print(line.rstrip())

def run():
    if(argv[1] == "webgetFunc"):
        url = argv[2]
        webgetFunc(url)
    filename = argv[2]
    if argv[1]=="print_file_content":
        print_file_content(filename)
    if argv[1]=="write_list_to_file":
        inputlist = argv[3:]
        write_list_to_file(filename,inputlist)
    if argv[1]=="read_csv":
        read_csv(filename)


def run2():
    if args.webgetFunc:
        url = argv[2]
        webgetFunc(url)
    if args.print_file_content:
        filename = argv[2]
        print_file_content(filename)
    if args.write_list_to_file:
        filename = argv[2]
        inputlist = argv[3:]
        write_list_to_file(filename,inputlist)
    if args.read_csv:
        filename = argv[2]
        read_csv(filename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Homemade handler of files")
    parser.add_argument("--print_file_content", help="print file")
    parser.add_argument("--write_list_to_file", nargs='*', help="Write to file")
    parser.add_argument("--read_csv",  help="print list")
    parser.add_argument("--webgetFunc", nargs='*', default=url, help="Downloads a url")
    args = parser.parse_args()
    run2()

