# Exercise Address https://www.acmicpc.net/problem/2577
from collections import Counter

def countOfNumber():
    multiArray = []
    for i in range(len(multi)):
        multiArray += multi[i]

    result = Counter(multiArray)

    for j in range(10):
        if(str(j) in result):
            print(result[str(j)])
        else:
            print(0)

if __name__ == "__main__":
    A = int(input())
    B = int(input())
    C = int(input())
    if(A > 100 and A >= 1000):
        print('A의 범위를 잘못입력하셨습니다.')
    if(B > 100 and B >= 1000):
        print('B의 범위를 잘못입력하셨습니다.')
    if(C > 100 and C >= 1000):
        print('C의 범위를 잘못입력하셨습니다.')

    multi = str(A * B * C)

    countOfNumber()
