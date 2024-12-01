def pyramid(rows):
    for i in range(rows):
        print(' '*(rows-i-1)+'* '*(i+1))
    for j in range(rows-1,0,-1):
        print(' '*(rows-j)+'* '*(j))

pyramid(4)

# if __name__ == '__main__':
#     n = int(input())
# arr = map(int, input().split())

# arr = list(arr)

# max_score = max(arr)

# while max_score in arr:
#     arr.remove(max_score)

# runner_up = max(arr)

# print(runner_up)