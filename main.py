def prime_list(min_val, max_val):
    sieve = [False] * 2 + [True] * (max_val+1)

    m = int(max_val ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i+i, max_val+1, i):
                sieve[j] = False

    return [i for i in range(min_val, max_val+1) if sieve[i]]


max_val_arr = []
min_val_arr = []
while 1:
    input_str = int(input())
    if input_str == 0:
        break
    else:
        min_val_arr.append(input_str+1)
        max_val_arr.append(input_str*2)

for i in range(len(min_val_arr)):
    min_val, max_val = min_val_arr[i], max_val_arr[i]
    prime_num = prime_list(min_val, max_val)
    print(len(prime_num))


