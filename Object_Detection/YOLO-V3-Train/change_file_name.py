"""
All file name change what you want format in input folder
Usage:
    python change_file_name.py --folder= --format=
    python change_file_name.py --folder="./Object Detection/images/test2" --format="test"
"""

import argparse
import os
import sys
from os import rename, listdir
   
def change(path, format_name):
    files = listdir(path)

    # Separate name and extension
    files = [file.split('.') for file in files] 
    count = 0

    for name, ext in files:
        # replace name
        replace_name = name.replace(name, format_name) + '.'

        # add count
        new_name = replace_name.replace(".", "{0:04d}.".format(count))

        name = path+'/'+name + '.'+ ext
        new_name = path+'/'+new_name + ext
        
        # rename file
        rename(name, new_name)
        count += 1

 

def main():
    '''main function'''
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", type=str,
                        help="Source Folder")
    parser.add_argument("--format", type=str,
                        help="Output Format")                        
    args = parser.parse_args()
    change(args.folder, args.format)

if __name__ == "__main__":
    main()