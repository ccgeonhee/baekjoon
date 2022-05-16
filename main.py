total_input = int(input())
input_string = input()

input_arr = input_string.split()

result = 0

for num in input_arr:
    num = int(num)
    if num <= 1:
        continue
    else:
        err = 0
        for i in range(2, num):
            if num % i == 0:
                err = 1
                break
            else:
                pass
        if err == 0:
            result += 1

print(result)
