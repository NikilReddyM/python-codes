n = int(input())
arr = sorted(list(set(map(int, input().split()))),reverse = True)
print(arr[1])