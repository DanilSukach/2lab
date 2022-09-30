import os
import csv
import cv2

def csv_file(path,url):
    data = [
        ("absolute_path","relative_path","class"),
    ]
    for i in range(1100):
        n = str(i)
        absolute = os.path.abspath(path + "/"+ url +"/" + n.zfill(4) + ".jpg")
        relative = path + "/"+ url +"/" + n.zfill(4) + ".jpg"
        data.append([absolute,relative,url])
    with open("data.csv","a+") as file:
        writer = csv.writer(file,delimiter = " ")
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
    copy("leopard")
    copy("tiger")

if __name__ == "__main__":
    main()