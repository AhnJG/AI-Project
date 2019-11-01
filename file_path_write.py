"""
Usage : python file_path_write.py --folder="./Object_detection/coco/labels/train/"
Output : ./Object_detection/coco/labels/train/write_file.txt
"""
import argparse
import os
import sys
   
def file_write(path):
    files = os.listdir(path)
    
    # File Filter (hide file, .txt file)
    for _file in files:
        name, ext = _file.split('.')

        if _file[0] == '.':
            files.remove(_file)
        elif ext == 'txt':        
            files.remove(_file)
            print(_file)

    # Get abspath all files in folder_path
    files = [os.path.abspath(_file) for _file in files]

    with open(path+"write_file.txt", "w") as f:
        for line in files:
            f.write(line + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", type=str,
                        help="Source Folder")  
                                           
    args = parser.parse_args()
    file_write(args.folder)