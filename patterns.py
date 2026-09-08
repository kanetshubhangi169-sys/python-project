for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()



for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()



for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()



for i in range(5,0,-1):
    for j in range(5-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()



for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()



for i in range(5,0,-1):
    for j in range(5-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()



for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()
for i in range(5,0,-1):
    for j in range(5-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()


for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print("*",end="")
        else:
            print(" ",end="")
    print()



for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for j in range(1,2*i):
        if i==5 or j==1 or j==2*i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()



for i in range(5):
    for j in range(5):
        if j==i or j==4-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()



for i in range(1,6):
    for j in range(i):
        print("*",end="")
    for j in range(2*(5-i)):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()
for i in range(4,0,-1):
    for j in range(i):
        print("*",end="")
    for j in range(2*(5-i)):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()



#numbers pattern
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()



for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()



num = 1
for i in range(1,6):
    for j in range(i):
        print(num,end="")
        num = num + 1
    print()




for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end="")
    print()



for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()




for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for j in range(1,2*i):
        print(j,end="")
    print()




for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()
for i in range(4,0,-1):
    for j in range(i):
        print(i,end="")
    print()



for i in range(1,6):
    for j in range(i):
        if(i+j) % 2 == 0:
            print("1",end="")
        else:
            print("0",end="")
    print()



for i in range(1,6):
    for j in range(i):
        if j%2==0:
            print("1",end="")
        else:
            print("0",end="")
    print()




for i in range(1,5):
    for j in range(1,5):
        if j == i:
            print(j,end="")
        elif j > i:
            print("#",end="")
        else:
            print("*",end="")
    print()