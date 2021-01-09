import time
import random


#Creating the test list
#Set amount to the number of numbers yout want to test (With more than 1000 some algorithms may take a long time!)
amount = 1000

def create_test_list():
    test_list = []
    i = 0
    while i < amount:
        test_list.append(round(random.random()*1000))
        i += 1
    return test_list


#Function for testing the speed of a algorithm
def test_algorithm(name, algorithm, print_sorted):
    start_time = time.time()
    sorted = algorithm(test_list)
    print(name, "took:", (time.time() - start_time), "seconds")
    if print_sorted:
        print(name + ":", sorted)


#All sort algorithms
#Common algorithms
def quick_sort(list):
    less = []
    equal = []
    greater = []
    if len(list) > 1:
        pivot = list[0]
        for x in list:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick_sort(less)+equal+quick_sort(greater)  
    else:  
        return list


#Made by creative people for fun
#github.com/MrScalo
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


#Printing some stuff to make it look good
print("----------")
print("Creating the test list...")
test_list = create_test_list()
print("Testing all algorithms...")
#test_algorithm(name, algorithm, print_sorted)
print("<< Common algorithms >>")
test_algorithm("Quick Sort", quick_sort, False)
print("<< Made by creative people for fun >>")
test_algorithm("Scalo Sort", scalo_sort, False)
print("----------")
