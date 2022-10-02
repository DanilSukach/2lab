import csv


def url(path: str,name: str,label: str):
    """Функция принимает путь к фалу: path
    метку класса по этому пути: name
    метку с которой нужжно сравнить: label"""
    if name == label:
        return path
    else:
        return None

def path(label:str) -> list:
    """Функция принимает метку класса: label"""
    data=[]
    with open ("data.csv") as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")
        for i in file_reader:
            path = url(i[0],i[2],label)
            if path != None:
                data.append(path)
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
    data = path("leopard")
    s = SimpleIterator(data,4)
    print(next(s))
    print(next(s))
    print(next(s))
    print(next(s))


if __name__ == "__main__":
    main()
            