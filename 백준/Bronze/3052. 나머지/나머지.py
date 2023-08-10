import sys
input = sys.stdin.readline

arr= []
count = 0
for _ in range(10): 
    n = int(input())
    arr.append(n%42)

list = set(arr)

print(len(list))


# 왜 안될까?
# for i in range(9): 
#     if arr[i] != arr[i+1]: # 마지막에 arr[8]비교
#      count += 1

# if arr[8] != arr[9]: # arr[9]비교
#     count += 1

# print(count)
