num = int(input())

err = 1
val = 0
for i in range(num):
    string_num = str(i)
    sum_val = i
    for j in string_num:
        sum_val += int(j)
    if sum_val == num:
        err = 0
        val = i
        break
print(val)
