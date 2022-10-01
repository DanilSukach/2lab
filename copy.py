import os
import shutil


def copy(path,url):
    ''''''
    if not os.path.isdir("dataset_copy"):
        os.mkdir("dataset_copy")
    for i in range(1100):
        a = str(i)
        shutil.copy(
            os.path.join(path, a.zfill(4) + ".jpg"),
            os.path.join('dataset_copy/', url + "_" + a.zfill(4) + ".jpg")
        )

def main():
    copy("dataset/tiger","tiger")
    copy("dataset/leopard","leopard")
    

if __name__ == "__main__":
    main()