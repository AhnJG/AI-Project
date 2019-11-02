import argparse
import os
import sys
   
path = 'coco/images/val'
abs_path = os.path.abspath(__file__)
abs_dir = os.path.dirname(abs_path)

print('abs_path : ', abs_path)
print('abs_dir : ', abs_dir)

path_join = os.path.join(abs_dir, path)
print(path_join)
print(os.sep)

join_file = os.path.join(path_join, 't.py')
print(join_file)