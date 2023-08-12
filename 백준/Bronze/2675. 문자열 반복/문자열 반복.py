import sys
input = sys.stdin.readline
# 문자열을 입력받고 문자열 각 인덱스 x 5회 후 출력

T = int(input()) # 테스트 케이스 개수

for _ in range(T):
    num, S = input().split()
    num = int(num)

    word = ""
    
    for i in S:
        word += i * num
    print(word)