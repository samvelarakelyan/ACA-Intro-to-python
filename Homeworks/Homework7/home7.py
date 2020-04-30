

#1)
def root_square_of_number(number:int):
    import mat
    return math.sqrt(number)



#2)
def div(x:int, y:int):
    assert y != 0, "Can't divide"
    return x / y



#3)
def example_func(my_list:list):
    my_sum = 0
    sum_of_pairs = []
    
    for i in range(len(my_list) -1):
        try:
            my_sum = my_list[i] + my_list[i + 1]
        except TypeError as te:
            return te
        sum_of_pairs.append(my_sum)
    
    return "SumOfPairs = " + str(sum_of_pairs)



#4)
def UpperContent(fileName):
    try:
        my_file = open(fileName, "r")
    except FileNotFoundError as fnfe:
        print(fnfe)
    try:
        for line in my_file:
            print(line.upper(), end = "")
        my_file.close()
    except IOError as ioe:
        print(ioe)
        


import numpy as np
#5)
NumpyArray = np.random.randint(1, 11, size = (3, 5))


#6)
NpArrayZeros = np.zeros(10, dtype = np.uint8)
NpArrayZeros[4] = 3


#7)
NpArray3_to_15 = np.arange(3, 16)


#8)
firstNpArray = np.array([1, 3, 5, 2, 4, 5])
secondNpArray = firstNpArray.reshape(3, 2)
thirdNpArray = firstNpArray.reshape(2, 3)


#9)
def changNpArray(np_array):
    while np.mean(np_array) > 5:
        np_array = np_array / 2
    return np_array


#10)
def nparray_columns(np_array):
    numOfColumns = np_array.shape[1]
    l = [np_array[:, i] for i in range(numOfColumns)]
    return l


def nparray_rows(np_array):
    numOfRows = np_array.shape[0]
    l = [np_array[i] for i in range(numOfRows)]
    return l


nparray2D_1to10_rand = np.random.randint(1, 10, size =(5,4), dtype = np.uint8)



 







  




