kezd=int(input())
veg=int(input())

szam=0

for i in range(kezd, veg):
    if i%3==0:
        szam+=1
        print(szam)