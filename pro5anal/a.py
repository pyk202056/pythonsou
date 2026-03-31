def quick_sort(a):
    n = len(a)

    if n <= 1:
        return a

    pivot = a[-1]

    g1 = []
    g2 = []

    for i in range(0, n - 1):
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])

    print('g1 : ', g1)
    print('g2 : ', g2)
    return quick_sort(g1) + [pivot] + quick_sort(g2)

d = [6,8,3,1,2,4,7,5]
print(quick_sort(d))