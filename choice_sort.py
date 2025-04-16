# choice_sort.py

def sort(list):
    for i in range(len(list)):
        for j in range(i):
            if list[j] > list[i]:
                buf = list.pop(i)
                list.insert(j, buf)

    return list