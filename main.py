N, M = map(int, input().split())
input_val = []
cnt = []

origin_start_w = []
origin_start_b = []


for _ in range(N):
    txt = input()
    input_val.append(txt)
w_prev = "B"
b_prev = "W"

for i in range(N+8):
    w_txt = ""
    b_txt = ""
    w_prev = "W" if w_prev == "B" else "B"
    b_prev = "W" if b_prev == "B" else "B"
    for j in range(M+8):
        if j == 0:
            w_start = w_prev
            b_start = b_prev
        w_start = "W" if w_start == "B" else "B"
        b_start = "W" if b_start == "B" else "B"
        w_txt += w_start
        b_txt += b_start
    origin_start_w.append(w_txt)
    origin_start_b.append(b_txt)


for start_w in range(N-7):
    for start_h in range(M-7):
        cnt1 = 0
        cnt2 = 0
        for w in range(start_w, start_w+8):
            for h in range(start_h, start_h+8):
                if input_val[w][h] != origin_start_w[w][h]:
                    cnt1 += 1
                if input_val[w][h] != origin_start_b[w][h]:
                    cnt2 += 1
        cnt.append(min(cnt1, cnt2))

print(min(cnt))

