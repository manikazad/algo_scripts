

def Inversion(array):
    l = len(array)
    if l == 1:
        return array,0
    arr_a, arr_b = array[:l/2], array[l/2:]
    sort_a,inv_a = Inversion(arr_a)
    sort_b,inv_b = Inversion(arr_b)

    sort_c = []
    inv_c = inv_a+inv_b
    i,j = 0, 0
    for k in range(l):
        if i< len(sort_a) and j < len(sort_b):
            if sort_a[i] <= sort_b[j]:
                sort_c.append(sort_a[i])
                i +=1

            elif sort_a[i] > sort_b[j]:
                sort_c.append(sort_b[j])
                inv_c += len(sort_a)-i
                j +=1
        elif i >= len(sort_a):
            sort_c.append(sort_b[j])
            j += 1
        elif j >= len(sort_b):
            sort_c.append(sort_a[i])
            i += 1
    return sort_c, inv_c

if __name__ == "__main__":
    data = open('IntegerArray.txt').readlines()
    data = [int(d.strip()) for d in data]
    print data[:10]
    arr, count = Inversion(data)
    print count