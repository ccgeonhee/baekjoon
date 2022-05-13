import pprint


def self_num(a):
    _num = [i for i in range(10000)]
    val = set()
    for i in range(a):
        a = str(i)
        sum = 0
        for i in range(len(a)):
            sum += int(a[i])
        val.add(int(a) + sum)

    for i in range(len(_num)):
        if _num[i] not in val:
            print(_num[i])


self_num(10000)
