from abc import ABC,abstractmethod
class Smartphone(ABC):
    def download(self):
        pass

class iphone16(Smartphone):
    def download(self):
        print("good pace download")
class iphone17(Smartphone):
    def download(self):
        print("download is quick")
class iphone18(Smartphone):
    def download(self):
        print("download is really fast")

a=iphone17()
a.download()
b=iphone18()
b.download()
c=iphone16()
c.download()

class apple():
    def colour(self):
        print("the colour is blue")
    def size(self):
        print("it is big")
class samsung():
    def colour(self):
        print("the colour is black")
    def size(self):
        print("it is small")