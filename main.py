alphabet = [chr(i) for i in range(97, 97 + 26)]     # 알파벳 정의
total_count = int(input())

str_arr = []    # 입력값
for i in range(total_count):
    input_str = input()
    str_arr.append(input_str)

result = 0
for string in str_arr:
    checker_dict = dict.fromkeys(alphabet, [])      # 알파벳 카운트 dict 정의
    for i in range(len(string)):                    # 입력 문자열의 문자를 나눠서 해당 문자의 위치를 배열에 추가
        val = checker_dict[string[i]].copy()
        val.append(i)
        checker_dict[string[i]] = val

    err = 0
    val_arr = checker_dict.values()
    for val in val_arr:                             # 알파벳의 위치 배열
        if len(val) == 0 or len(val) == 1:          # 없거나 길이가 1이면 연속
            pass
        else:                                       # 길이가 2 이상이면 연속성 체크
            prev = val[0]
            for i in range(1, len(val)):
                if val[i]-prev != 1:                # ex)위치 배열 값이 [1,4,5] 일 때, 인접한 수의 차이가 1이 아니면 그룹x
                    err = 1
                else:                               # 해당하지 않으면 prev 변경
                    prev = val[i]

    if err == 0:
        result += 1

print(result)
