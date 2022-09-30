import os
import csv
import cv2

def csv_file(path,url):
    data = [
        ("absolute_path","relative_path","class"),
    ]
    for i in range(1100):
        n = str(i)
        absolute = os.path.abspath(path + n.zfill(4) + ".jpg")
        relative = os.path.relpath(path + n.zfill(4) + ".jpg")
        data.append([absolute,relative,url])
    with open("data.csv","a+",newline="") as file:
        writer = csv.writer(file,delimiter = ";")
        writer.writerows(data)

def copy(url):
    if not os.path.isdir("dataset_copy"):
        os.mkdir("dataset_copy")
    for i in range(1100):
        a=str(i)
        filename=str('dataset/' + url + '/' + a.zfill(4) +'.jpg')
        image=cv2.imread(filename)
        filewrite=str('dataset_copy/' + url + '_' + a.zfill(4) +'.jpg')
        cv2.imwrite(filewrite,image)

def main():
    csv_file("dataset/leopard/","leopard")
    csv_file("dataset/tiger/","tiger")
    copy("tiger")

if __name__ == "__main__":
    main()