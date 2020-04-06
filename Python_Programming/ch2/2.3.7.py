a = int(input())
b = int(input())

sum = 0
j = 0

for i in range(a,b+1):
    if i % 3 == 0:
        sum += i
        j += 1
print(sum / j)

print("============================================")

a,b=(int(i) for i in input().split())
sum = 0
j = 0
for i in range (a,b+1):
    if i % 3 == 0:
        sum+=i
        j+=1
        print(i)
print("Сумма чисел  = ", sum)
print("Количество чисел = ", j)
print(sum/j)
