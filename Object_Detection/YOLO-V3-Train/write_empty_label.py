"""
roi : label
roi 파일이 없는 이미지들의 roi를 파일을 만들어 주는 파이썬 코드를 첨부합니다.
"""
#-*- coding:utf-8 -*-
import os
from tqdm import tqdm


def returnFileList(dirname, extract):
    fileList = []
    filenames = os.listdir(dirname)
    for filename in filenames:
        ext = os.path.splitext(filename)[-1]
        if ext == extract: 
            fileList.append(filename)
    return fileList


CURRENT_PATH = os.getcwd() + "\\"
imgFileList = returnFileList(CURRENT_PATH, ".jpg")

for imgFile in imgFileList:
  roiName = (CURRENT_PATH+imgFile).replace("jpg", "txt")
  
  print(roiName)
  if (not (os.path.isfile(roiName))):
    f = open(roiName, "w")
    f.close()