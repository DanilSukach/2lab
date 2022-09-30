import os
import csv


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

def main():
    csv_file("dataset","leopard")

if __name__ == "__main__":
    main()