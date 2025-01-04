#bubble sort in python


def bubble_sort(array):

    #2 loops
    for i in range(len(array)-1):
        for j in range(len(array)- 1- i):
            #if current number is bigger then the next one swap !
            if array[j] > array[j+1]:
                 # basically its a,b = b,a
                 array[j], array[j + 1] = array[j + 1], array[j]




    return array


print(bubble_sort([1,5,2,8,9]))

