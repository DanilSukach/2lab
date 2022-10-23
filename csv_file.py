import os
import csv
import random
from array import array


def csv_file(path: str,label: str) -> None:
    """Функция принимает путь к файлам: path и метку класса: label"""
    info = os.listdir(path)
    data = []
    for i in range(1100):
        n = str(i)
        absolute = os.path.abspath(path + info[i])
        relative = os.path.relpath(path + info[i])
        data.append([absolute,relative,label])
    with open("data.csv","a+",newline="") as file:
        writer = csv.writer(file,delimiter = ";")
        writer.writerows(data)

def main():
    csv_file("dataset/tiger/","tiger")
    csv_file("dataset/leopard/","leopard")
    

if __name__ == "__main__":
    main()