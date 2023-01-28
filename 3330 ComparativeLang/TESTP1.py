def getDict(list):
    dictList = {};
    for i in range(0, len(list)):
        dictList.update({list[i] : list.count(list[i])})
    return dictList

def main() :    
    list = [1, 3, 4, 6, 7, 8, 9, 1, 2]

    print("Dictionary of list is ", getDict(list))
    
main()