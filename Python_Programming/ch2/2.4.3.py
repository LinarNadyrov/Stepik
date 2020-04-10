genom = input().lower()

print((genom.count('c') + genom.count('g')) * 100 / len(genom))

print("======================================================")
s=input()
sum=0
for i in s.upper():
    if i == "G" or i == "C":
        sum+=1
d=len(s)
c=(sum/d)*100
print(c)