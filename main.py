import time
import random


#Creating the test list
#Set amount to the number of numbers yout want to test
amount = 1000

def create_test_list():
    test_list = []
    i = 0
    while i < amount:
        test_list.append(round(random.random()*1000))
        i += 1
    return test_list


#Function for testing the speed of a algorithm
def test_algorithm(name, algorithm):
    start_time = time.time()
    algorithm(test_list)
    print(name, "took:", (time.time() - start_time), "seconds")


#All sort algorithms
def scalo_sort(list):
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


#Testing all algorithms
print("----------")
print("Creating the test list...")
test_list = create_test_list()
print("Testing all algorithms...")
test_algorithm("Scalo Sort", scalo_sort)
print("----------")
