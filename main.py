import time
import random

test_list = []
i = 0
while i < 1000:
    test_list.append(round(random.random()*1000))
    i += 1

def sort(list):
    change = True
    while change:
        change = False
        index = 0
        for item in list:
            if (index != 0):
                if (list[index-1] > item):
                    change = True
                    list.pop(index)
                    list.insert((index - 1), item)
            index = index + 1

    return list

start_time = time.time()
sort(test_list)
print("--- %s seconds ---" % (time.time() - start_time))
