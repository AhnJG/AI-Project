"""
Usage : python file_path_write.py --folder="./Object_detection/coco/labels/train/"
Output : ./Object_detection/coco/labels/train/write_file.txt
"""
import argparse
import os
import sys
   
def file_write(path):
    files = os.listdir(path)
    file_list = []
    # File Filter (hide file, .txt file)
    for _file in files:
        name, ext = _file.split('.')

        if _file[0] == "." or ext == "txt":
            files.remove(_file)
        else:
            file_list.append('/Users/ahn/Documents/AI-Project/Object_detection/YOLO-V3-Train/coco/images/train/' + _file)


    # Get abspath all files in folder_path
    # files = [os.path.abspath(_file) + 'Object_detection/YOLO-V3-Train/coco/images/train/' for _file in files]

    with open(path+"write_file.txt", "w") as f:
        for line in file_list:
            f.write(line + "\n")
    
    print(path+"write_file.txt")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", type=str,
                        help="Source Folder")  
                                           
    args = parser.parse_args()
    file_write(args.folder)