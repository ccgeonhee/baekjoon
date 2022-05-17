min_val = int(input())
max_val = int(input())

sum = 0
min = 0
is_first = 0
for i in range(min_val, max_val+1):
    if i <= 1:
        continue
    else:
        err = 0
        for j in range(2, i):
            if i % j == 0:
                err = 1
                break
            else:
                pass
        if err == 0:
            sum += i
            if is_first == 0:
                min = i
                is_first = 1
            else:
                pass

if sum != 0 and min != 0:
    print(sum)
    print(min)
else:
    print(-1)
