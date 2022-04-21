def line(m, n, x, y, str):
    l = len(str)
    for i in range(l):
        if str[i] == 'U':
            x = x - 1
        elif str[i] == 'D':
            x = x + 1
        elif str[i] == 'L':
            y = y - 1
        elif str[i] == 'R':
            y = y + 1
        
        if x < 0 or y < 0 or x >= m or y >= n: 
            return -1
    return 1

def check(m, n, str):
    for i in range(m):
        for j in range(n):
            if line(m, n, i, j, str) == 1:
                return True
    return False

m , n = [int(x) for x in input().split()]
s = input()
if check(m, n, s) == True:
    print('Safe')
else:
    print('Unsafe')