
class Mylist(list):
    def indexOf(self, element, fromIndex):
        
def main():
    list1 = MyList()
    
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list1.append(1)
    list1.append(5)

    print(list1.indexOf(1, 3))
    print(list1.lastIndexOf(1, 2))
  
main()
