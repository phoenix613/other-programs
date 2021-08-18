def bubble_sort (a):
    n = len(a)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]    
    return a

def selection_sort (b):
    n = len(b)
    
    
    for j in range(n):
        min_index = j    
        for i in range(j+1,n):
            if b[i] < b[min_index]:
                min_index = i
        b[min_index], b[j] =  b[j], b[min_index] 
    return b        

def insert_sort (a):
    n = len(a)
    
    for i in range(1,n):
        elem = a[i]
        j = i
        while a[j-1] > elem and j >= 1:
            a[j] = a[j-1]
            j-=1
        a[j] = elem    
    return a

b = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
print(insert_sort(b) == selection_sort(b))    