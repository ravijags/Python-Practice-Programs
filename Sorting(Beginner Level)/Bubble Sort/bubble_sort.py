def bubble_sort(list1):
    n = len(list1)
    for i in range(n):     # No of Passes
        for j in range(0,n-i-1):  # Size(-i-1) because last i elements are already sorted
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]

num_list = [8,7,13,1,-9,4]
bubble_sort(num_list)
print('The Sorted list is:')
for i in range(len(num_list)):
    print(num_list[i], end=' ')