croatian_alphabet = [
    "dz=",
    "c=",
    "c-",
    "d-",
    "lj",
    "nj",
    "s=",
    "z=",
]

input_string = input()
cro_alpha_arr = []

result = 0
parse_alpha = input_string
for cro_alpha in croatian_alphabet:
    if input_string.count(cro_alpha) != 0:
        result += input_string.count(cro_alpha)
        input_string = input_string.replace(cro_alpha, " ")

result += len(input_string.replace(" ", ""))
print(result)

