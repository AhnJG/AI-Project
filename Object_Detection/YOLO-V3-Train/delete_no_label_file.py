"""
Description : 해당 폴더에 라벨링 되어있지 않은 모든 이미지 파일을 삭제한다"
    Labeling : (1.jpg + 1.txt), (2.png + 2.txt)
    No Labeling : (1.jpg), (2.jpg)
Usage : python delete_no_label_file.py --folder="./coco/images/train/"

"""
import argparse
import os
import sys
   
def file_delete(path):
    files = os.listdir(path)
    img_file_list = []

    # 파일의 개수
    print('file count : ', len(files))

    # 모든 이미지 파일을 리스트에 넣는다    
    for _file in files:
        name, ext = _file.split('.')

        if ext == "jpg" or ext == "jpeg" or ext == "png" or ext == "gif":
            img_file_list.append(name)
            # files.remove(_file)
        
    # 리스트에 있는 이미지 파일 중에서 .txt파일도 같이 가지고 있으면 리스트에서 삭제한다
    for _file in files:
        name, ext = _file.split('.')

        if ext == "txt":
            if name in img_file_list:
                img_file_list.remove(name)

    #리스트에 남아 있는 파일 삭제
    for name in img_file_list:
        if os.path.isfile(path+name+".jpg"):
            print(name)
            os.remove(path+name+".jpg")
        elif os.path.isfile(path+name+".jpeg"):
            print(name)
            os.remove(path+name+".jpeg")
        elif os.path.isfile(path+name+".png"):
            print(name)
            os.remove(path+name+".png")
        elif os.path.isfile(path+name+".gif"):
            print(name)
            os.remove(path+name+".gif")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", type=str,
                        help="Source Folder")  
                                           
    args = parser.parse_args()
    file_delete(args.folder)