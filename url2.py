import csv
import os


def path(label: str) -> list:
    """Функция принимает метку класса: label"""
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
    """Класс итератор - задается итерируемый объект и ограничение """
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
            