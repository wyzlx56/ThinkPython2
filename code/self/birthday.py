import random
count=0
for i in range(1000):
    b=[random.randint(1,31) for _ in range(23)]
    sorted(b)
    for j in range(len(b)-1):
        if b[j]==b[j+1]:
            count=count+1
            break
print(count*100/1000)
