def prime_list(min_val, max_val):
    sieve = [False] * 2 + [True] * (max_val+1)

    m = int(max_val ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i+i, max_val+1, i):
                sieve[j] = False

    return [i for i in range(min_val, max_val+1) if sieve[i]]


input_str = input()
min_val, max_val = int(input_str.split()[0]), int(input_str.split()[1])
prime_num = prime_list(min_val, max_val)
for num in prime_num:
    print(num)


