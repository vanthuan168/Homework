
def Dem_Capso (list, n):
    dem = 0
    for i in range(n):
        for j in range(i + 1, n):
            if list[i] == list[j]:
                dem = dem + 1
    return dem

n = int(input())
l = [int(x) for x in input().split()]
print(Dem_Capso(l, n))
