#1)
import numpy as np

#2)
np_array1 = np.zeros(10, dtype = np.uint8)
print(np_array1)

#3)
print(help(np.add))

#4)
np_array2 = np.zeros(10, dtype = np.uint8)
print(np_array2)
np_array2[4] = 1
print(np_array2)

#5)
np_array3 = np.arange(10, 50)
print(np_array3)

#6)
np_array4 = np.arange(0, 51,)
print(np.flip(np_array4))

#7)
np_matrix = np.arange(0, 9).reshape(3, 3)
print(np_matrix)

#8)
np_array5 = np.array([1, 2, 0, 0, 4, 0], dtype = np.uint8)
index = np.where(np_array5 != 0)
print(index)

#9)
matrix3D = np.random.randint(1, 21, size = (3, 3, 3))
print(matrix3D)

#10)
random_matrix2D = np.empty((10, 10), dtype = np.int16)
print(random_matrix2D)

max_value_of_matrix = np.amax(random_matrix2D)
min_value_of_matrix = np.amin(random_matrix2D)

print(max_value_of_matrix)
print(min_value_of_matrix)

#11)
np_array6 = np.random.rand(30)
mean_value_of_nparray = np.mean(np_array6)

print(mean_value_of_nparray)

#12)
np_array7 = np.arange(11)
values_from_3to8 = np.where((np_array7 >= 3) & (np_array7 <= 8))

print(values_from_3to8)

#13)
np_array8 = np.random.randint(1, 11, 20)

print(np_array8)
np_array8 = np_array8[np.where(np_array8 < 5)] * 2
print(np_array8)

#14)
np_array9 = np.array([1, 5, 6, 2, -2, 23, 45])
div2 = np.where(np_array9 % 2 == 0)
print(div2)

#15)
np_array10 = np.arange(1, 21)
print(np_array10)
div3 = np_array10[np.where(np_array10 % 3 == 0)]
print(div3)

#16)
np_array11 = np.arange(0, 5)
np_array11 = np.tile(np_array11, (5, 1)) 
print(np_array11)

#17)
np_array12 = np.random.randint(1, 11, size = (3, 5))
print(np_array12)

#18)
np_array13 = np.zeros(10, dtype = np.uint8)
print(np_array13)
np_array13[4] = 3
print(np_array13) 

#19)
np_array14 = np.arange(3,16)
print(np_array14)

#20)
def changNpArray(np_array):
    while np.mean(np_array) > 5:
        np_array = np_array / 2
    return np_array


#21)
def nparray_columns(np_array):
    numOfColumns = np_array.shape[1]
    l = [np_array[:, i] for i in range(numOfColumns)]
    return l

nparray2D_1to10_rand = np.random.randint(1, 10, size =(5,4), dtype = np.uint8)
print(nparray_columns(nparray2D_1to10_rand))
