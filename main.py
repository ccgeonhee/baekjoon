import pprint


def equivalency(a):
    equivalency_arr = []
    for i in range(1, a + 1):
        num = str(i)
        if len(num) <= 2:
            equivalency_arr.append(num)
        else:
            num_arr = [num[i] for i in range(len(num))]
            diff = int(num_arr[-1]) - int(num_arr[-2])
            err = 0
            for j in range(len(num_arr) - 1, 0, -1):
                cur_diff = int(num_arr[j]) - int(num_arr[j - 1])
                if diff != cur_diff:
                    err = 1
                else:
                    pass
            if err == 0:
                equivalency_arr.append(num)
    han_len = len(equivalency_arr)
    print(han_len)
    return han_len


_num = int(input())
equivalency(_num)
