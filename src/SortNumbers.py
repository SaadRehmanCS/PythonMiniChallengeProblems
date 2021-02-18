from random import randint

list = []
for i in range(100000):
    list += [randint(0, i)]

def selectionSort(list):
    sortedList = []
    for i in range(len(list)):
        sortedList += [min(list)]
        list.remove(min(list))
    return sortedList


print(selectionSort(list))