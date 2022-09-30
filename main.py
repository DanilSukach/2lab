import os
import csv
import shutil
import cv2
import random
from array import array

def csv_file(path,url,file_name):
    info = os.listdir(path)
    data = []
    for i in range(1100):
        n = str(i)
        absolute = os.path.abspath(path + info[i])
        relative = os.path.relpath(path + info[i])
        data.append([absolute,relative,url])
    with open(file_name + ".csv","a+",newline="") as file:
        writer = csv.writer(file,delimiter = ";")
        writer.writerows(data)

def copy(url):
    if not os.path.isdir("dataset_copy"):
        os.mkdir("dataset_copy")
    for i in range(1100):
        a = str(i)
        shutil.copy(
            os.path.join('dataset/' + url, a.zfill(4) + ".jpg"),
            os.path.join('dataset_copy/', url + "_" + a.zfill(4) + ".jpg")
        )

def copy_random(url1,url2):
    if not os.path.isdir("dataset_copy_random"):
        os.mkdir("dataset_copy_random")
    data=[]
    array=[]
    for i in range(3000):
        rand = random.randint(0,10000)
        if not rand in array:
            array.append(rand)
    for i in range(1100):
        rand = str(array[i])
        a = str(i)
        shutil.copy(
            os.path.join('dataset/' + url1, a.zfill(4) + ".jpg"),
            os.path.join('dataset_copy_random/', rand + ".jpg")
        )
        absolute = os.path.abspath('dataset_copy_random/' + rand + ".jpg")
        relative = os.path.relpath('dataset_copy_random/' + rand + ".jpg")
        data.append([absolute,relative,url1])
        rand1 = str(array[i+1100])
        shutil.copy(
            os.path.join('dataset/' + url2, a.zfill(4) + ".jpg"),
            os.path.join('dataset_copy_random/', rand1 + ".jpg")
        )
        absolute = os.path.abspath('dataset_copy_random/' + rand1 + ".jpg")
        relative = os.path.relpath('dataset_copy_random/' + rand1 + ".jpg")
        data.append([absolute,relative,url2])
    with open("data_copy" + ".csv","a+",newline="") as file:
            writer = csv.writer(file,delimiter = ";")
            writer.writerows(data)
    
        

def main():
    copy_random("leopard","tiger")
    

if __name__ == "__main__":
    main()