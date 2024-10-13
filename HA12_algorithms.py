#Algorithms
def sorting(l):
    comparisons = 0
    n = len(l)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l

list1=[2,3,1,10,7]
sorting(list1)

list2=[10,8,15,25,100,45,37,38,43,1000]
sorting(list2)