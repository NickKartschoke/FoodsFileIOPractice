from curses.ascii import isspace
import json


def readFoodsFile():
    file_path = (r"C:\Users\nickk\repo\FileIOPractice\foods.txt")
    f = open(file_path)
    word_dict = f.read().split('\n')
    for i in range(0,len(word_dict)):
        word_dict[i] = word_dict[i].lower().strip()
    f.close()
    return word_dict

def readHighFiberFile():
    file_path = (r"C:\Users\nickk\repo\FileIOPractice\highfiber.txt")
    f = open(file_path)
    word_dict = f.read().split('\n')
    for i in range(0,len(word_dict)):
        word_dict[i] = word_dict[i].lower().strip()
    f.close()
    return word_dict

def readLowFatFile():
    file_path = (r"C:\Users\nickk\repo\FileIOPractice\lowfat.txt")
    f = open(file_path)
    word_dict = f.read().split('\n')
    for i in range(0,len(word_dict)):
        word_dict[i] = word_dict[i].lower().strip()
    f.close()
    return word_dict

def readGlycemicFile():
    file_path = (r"C:\Users\nickk\repo\FileIOPractice\low-glycemic-index.txt")
    f = open(file_path)
    word_dict = f.read().split('\n')
    for i in range(0,len(word_dict)):
        word_dict[i] = word_dict[i].lower().strip()
    f.close()
    return word_dict

foods = readFoodsFile()
highFiber = readHighFiberFile()
lowFat = readLowFatFile()
glycemic = readGlycemicFile()

l = list()
for i in range(0,len(foods)):
    dict = {}
    check = True
    dict['Food'] = foods[i].capitalize()
    dict['High Fiber'] = highFiber[i].capitalize()
    dict['Low Glycemic'] = glycemic[i].capitalize()
    dict['Low Fat'] = lowFat[i].capitalize()
    if not all(x.isalpha() or x.isspace() or x == ':' for x in foods[i]):
        check = False
    if not all(x.isalpha() or x.isspace() for x in highFiber[i]):
        check = False
    if not all(x.isalpha() or x.isspace() for x in glycemic[i]):
        check = False
    if not all(x.isalpha() or x.isspace() for x in lowFat[i]):
        check = False
    if foods[i] == '':
            check = False
    if check:
        l.append(dict)

noDuplicatesList = list()

for i in range(1,len(l)):
    if l[i] not in noDuplicatesList:
        noDuplicatesList.append(l[i])

with open("foodData.json", "w") as final:
    json.dump(noDuplicatesList, final, indent = 1)

final.close()

with open('foodData.json') as f:
    data = json.load(f)

countHighFiber = 0
countLowFat = 0
countLowGlycemic = 0

for i in range(0,len(data)):
    if data[i]['High Fiber'] == 'Yes':
        countHighFiber += 1
    if data[i]['Low Fat'] == 'Yes':
        countLowFat += 1
    if data[i]['Low Glycemic'] == 'Yes':
        countLowGlycemic += 1

print(countHighFiber)
print(countLowFat)
print(countLowGlycemic)

print(round(countHighFiber/len(data)*100.0,2), "%")
print(round(countLowFat/len(data)*100.0,2), "%")
print(round(countLowGlycemic/len(data)*100.0,2), "%")

f.close()