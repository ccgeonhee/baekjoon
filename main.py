input_string = input()

num, max_sum = int(input_string.split()[0]), int(input_string.split()[1])

card = input()
card_arr = [int(i) for i in card.split()]

sum_val = 0
for i in range(len(card_arr) - 2):
    for k in range(i+1, len(card_arr)):
        bundle = card_arr[i] + card_arr[k]
        for j in range(k+1, len(card_arr)):
            if sum_val < bundle + card_arr[j] <= max_sum:
                sum_val = bundle + card_arr[j]

print(sum_val)

