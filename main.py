def prime_list(min_val, max_val):
    sieve = [False] * 2 + [True] * (max_val+1)

    m = int(max_val ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i+i, max_val+1, i):
                sieve[j] = False

    return sieve


test_case_num = int(input())

test_case_arr = []
for i in range(test_case_num):
    test_case_arr.append(int(input()))

prime_arr = prime_list(0, 10000)
for case in test_case_arr:
    result_case = []

    half_case = case // 2
    for i in range(half_case, 1, -1):
        if prime_arr[case - i] is True and prime_arr[i] is True:
            print(i, case - i)
            break
