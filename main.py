def microfactorization(num):
    if num == 1:
        return 0
    for i in range(2, num + 1):
        if num % i == 0:
            print(i)
            microfactorization(int(num / i))
            break


num = int(input())
microfactorization(num)
