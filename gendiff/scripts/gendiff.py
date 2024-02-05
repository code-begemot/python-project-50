#!/usr/bin/env python3
import argparse
from gendiff import generate_diff

def main():
    parser = argparse.ArgumentParser(description='Compare \
    two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output', default='stylish')
    args = parser.parse_args()

    file_path1 = args.first_file
    file_path2 = args.second_file
    file_format = args.format


    # file_path1 = 'file1.json'
    # file_path2 = 'file2.json'
    # format = 'plain'

    result = generate_diff(file_path1, file_path2, file_format)
    print(result)

if __name__ == '__main__':
    main()
