import os
import shutil
import random
import csv


def copy_random(path1: str,url1: str,path2: str,url2: str) -> None:
    """Функция принимает два пути: path и две метки класса: label"""
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
            os.path.join(path1, a.zfill(4) + ".jpg"),
            os.path.join('dataset_copy_random/', rand + ".jpg")
        )
        absolute = os.path.abspath('dataset_copy_random/' + rand + ".jpg")
        relative = os.path.relpath('dataset_copy_random/' + rand + ".jpg")
        data.append([absolute,relative,url1])
        rand1 = str(array[i+1100])
        shutil.copy(
            os.path.join(path2, a.zfill(4) + ".jpg"),
            os.path.join('dataset_copy_random/', rand1 + ".jpg")
        )
        absolute = os.path.abspath('dataset_copy_random/' + rand1 + ".jpg")
        relative = os.path.relpath('dataset_copy_random/' + rand1 + ".jpg")
        data.append([absolute,relative,url2])
    with open("data_copy.csv","a+",newline="") as file:
            writer = csv.writer(file,delimiter = ";")
            writer.writerows(data)

       

def main():
    copy_random("dataset/tiger","tiger","dataset/leopard","leopard")
    

if __name__ == "__main__":
    main()