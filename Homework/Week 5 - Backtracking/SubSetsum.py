
def SubSetSum(A, sum, d):
    global count
    if sum == d:
        count += 1
    else:
        if sum > d or len(A) == 0:
            return 
        else:
            SubSetSum(A[1:], sum, d)
            SubSetSum(A[1:], sum + A[0], d)

n,d = map(int, input().split())
A = [int(x) for x in input().split()]

sum = 0
count = 0
SubSetSum(A, sum, d)
print(count)
