import csv
import os

def url(path,name,label):
    if name == label:
        return path
    else:
        return None

def path(label):
    data=[]
    array = os.listdir("dataset_copy")
    n = 0
    for i in array:
        name = array[n].find(label)
        if name != -1:
            data.append(array[n])
        n += 1
    return data

class SimpleIterator:
    def __init__(self,start,limit):
        self.limit = limit
        self.counter = 0
        self.num = start
        
    def __next__(self):
        if self.counter < self.limit:
            i = self.counter
            self.counter += 1
            return self.num[i]
        else:
            raise StopIteration
        
def main():
    data = path("tiger")
    s = SimpleIterator(data,4)
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))


if __name__ == "__main__":
    main()
            