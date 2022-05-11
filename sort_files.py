#!/usr/bin/env python3

import os
import shutil 

path_to_folder = "/home/yashbhatt/Downloads/"

dir = os.listdir(path_to_folder)

# print(dir)
for file in dir:
    if file.endswith(".ipynb"):
        shutil.move(path_to_folder+file, path_to_folder+'Jupyter_Notebooks')
    elif file.endswith('.pdf'):
        shutil.move(path_to_folder+file, path_to_folder+'PDFs')
    elif file.endswith('.png'):
        shutil.move(path_to_folder+file, path_to_folder+'Pics')
    elif file.endswith('.jpeg'):
        shutil.move(path_to_folder+file, path_to_folder+'Pics')
    elif file.endswith('.deb'):
        shutil.move(path_to_folder+file, path_to_folder+'Debian_Files')
        shutil.move(path_to_folder+file, path_to_folder+'ZIP-TAR')
    elif file.endswith('.gz'):
        shutil.move(path_to_folder+file, path_to_folder+'ZIP-TAR')
    elif file.endswith('.xlsx'):
        shutil.move(path_to_folder+file, path_to_folder+'Excel')    
    elif file.endswith('.csv'):
        shutil.move(path_to_folder+file, path_to_folder+'Excel')