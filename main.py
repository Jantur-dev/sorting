from random import randint, shuffle
def create_array(min=10, max=10):
    return [randint(0, max) for arr in range(min)]
def is_sort(l):
    for i in range(1, len(x)):
        if l[i] < l[i-1]:
            return False
    return True
def bogo_sort(x):
    jml = 0
    while not is_sort(x):
        shuffle(x)
        jml+=1
    return jml, x

x = create_array(10, 10)
y, z = bogo_sort(x)

print(f"Unsorted array : {x}")
print(f"Number of Iterations : {y}")
print(f"Sorted array : {z}")