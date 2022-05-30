num_of_member = int(input())

big_arr = []
for i in range(num_of_member):
    big = input()
    weight, height = int(big.split()[0]), int(big.split()[1])
    big_arr.append([weight, height])

cnt_arr = []
for i in range(len(big_arr)):
    count = 1
    cur_weight = big_arr[i][0]
    cur_height = big_arr[i][1]
    for j in range(len(big_arr)):
        comparison_weight = big_arr[j][0]
        comparison_height = big_arr[j][1]
        if cur_weight < comparison_weight and cur_height < comparison_height:
            count += 1
    cnt_arr.append(str(count))

cnt_arr = " ".join(cnt_arr)
print(cnt_arr)
