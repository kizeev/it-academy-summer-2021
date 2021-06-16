# Sort the odd
# You will be given an array of numbers. You have to sort the odd numbers in
# ascending order while leaving the even numbers at their original positions

def sort_array(source_array):
    list_even = []
    new_list = source_array[:]

    for i in source_array:
        if i % 2 != 0:
            list_even.append(i)

    list_even.sort()
    a = 0

    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            new_list[i] = list_even[a]
            a += 1
    return new_list
