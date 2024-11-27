qator=int(input("qatorlar soni: "))
ustun=int(input("ustublar soni: "))
ortaQator=qator//2+1
ortaUstun=ustun//2+1


# for i in range(1,qator+1):
#     for j in range(1,ustun+1):
#             print("*",end=' ')
#     print()
# print("\n")


# for i in range(1,qator+1):
#     for j in range(1,ustun+1):
#         if j==1:
#             print("#",end=' ')
#         else:
#             print("*",end=' ')
#     print()
# print("\n")
    

# for i in range(1,qator+1):
#     for j in range(1,ustun+1):
#         if j==1 or i==1:
#             print("#",end=' ')
#         else:
#             print("*",end=' ')
#     print()
# print("\n")
    

for i in range(1,qator+1):
    for j in range(1,ustun+1):
        if j==1 or i==1 or j==ustun:
            print("#",end=' ')
        else:
            print("*",end=' ')
    print()
print("\n")

for i in range(1,qator+1):
    for j in range(1,ustun+1):
        if j==1 or i==1 or j==ustun or i==qator:
            print("#",end=' ')
        else:
            print("*",end=' ')
    print()
print("\n")


for i in range(1,qator+1):
    for j in range(1,ustun+1):
        if (j==1 or i==1 
            or(j==ustun or i==qator)
            or(i==ustun//2+1)):
            print("#",end=' ')
        else:
            print("*",end=' ')
    print()
print("\n")

for i in range(1,qator+1):
    for j in range(1,ustun+1):
        if (j==1 or i==1 
            or(j==ustun or i==qator)
            or(i==ustun//2+1 or j==qator//2+1)):
            print("#",end=' ')
        else:
            print("*",end=' ')
    print()
print("\n")

for i in range(1,qator+1):
    for j in range(1,ustun+1):
        if ( i==j):
            print("0",end=' ')
        else:
            print("*",end=' ')
    print()
print("\n")



for i in range(1,qator+1):
    for j in range(1,ustun+1):
        if ( i>=j ):
            print("0",end=' ')
        else:
            print("*",end=' ')
    print()
print("\n")

for i in range(1,qator+1):
    for j in range(1,ustun+1):
        if (i+j)%2==0:
            print("0",end=' ')
        else:
            print("1",end=' ')
    print()
print("\n")


for i in range(1,qator+1):
    for j in range(1,ustun+1):
        if (i+j)==ustun+1 or i==j:
            print("0",end=' ')
        else:
            print("1",end=' ')
    print()
print("\n")

for i in range(1,qator+1):
    for j in range(1,ustun+1):
        if ((i==ortaQator-1 or i==ortaQator+1)):
            print(j,end=' ')
        else:
            print("0",end=' ')
    print()
print("\n")


for i in range(0,qator):
    for j in range(0,ustun):
        print(chr(i+65),end=' ')
    print()
print("\n")

    
for i in range(0,qator):
    for j in range(0,ustun):
        print(i+j,end=' ')
    print()
print("\n")

for i in range(1,qator+1):
    for j in range(1,ustun+1):
        print(1,end=' ')
    print()
print("\n")



for i in range(0,qator):
    for j in range(0,ustun):
        if (
            j == i
            ):
            print('#', end=' ')
        else:
            print(0, end=' ')
    print()
print("\n")

for i in range(0,qator):
    for j in range(0,ustun):
        if (
            j == i or i > j
            ):
            print('0', end=' ')
        else:
            print('*', end=' ')
    print()
print("\n")

for i in range(0,qator):
    for j in range(0,ustun):
        if (
            (i + j) % 2 == 0
            ):
            print('0', end=' ')
        else:
            print('1', end=' ')
    print()
print("\n")

for i in range(0,qator):
    for j in range(0,ustun):
        if (
            i == j or i + j == ustun - 1
            ):
            print('0', end=' ')
        else:
            print('1', end=' ')
    print()
print("\n")

for i in range(0,qator):
    for j in range(0,ustun):
        if (
                (
                    (
                    i == ortaQator - 1 or i == ortaQator + 1) 
                    and (j == ortaUstun - 1 or j == ortaUstun + 1) 
                )
            ):
            print('0', end=' ')
        else:
            print('1', end=' ')
    print()
print("\n")

for i in range(0,qator):
    for j in range(0,ustun):
        print(chr(i + 65), end=' ')
    print()
print("\n")


k = 1
for i in range(0,qator):
    for j in range(0,ustun):
        print(k, end=' ')
        k += 1
    print()
print("\n")


k = 1
sum = 0
for i in range(0,qator):
    for j in range(0,ustun):
        print(k, end=' ')
        if j == 0 or j == ustun-1 or i == ortaQator:
            sum += k
        k += 1
    print()
print(sum)
print("\n")


k = 1
sum = 0
for i in range(0,qator):
    for j in range(0,ustun):
        print(k, end=' ')
        if j == 0 or j == ustun-1 or i == ortaQator or j == ortaUstun:
            sum += k
        k += 1
    print()
print(sum)
print("\n")


k = 1
sum = 0
for i in range(0,qator):
    for j in range(0,ustun):
        print(k, end=' ')
        if i >=j:
            sum += k
        k += 1
    print()
print(sum)
print("\n")


k = 1
sum = 0
for i in range(0,qator):
    for j in range(0,ustun):
        print(k, end=' ')
        if i == j or i + j == ustun -1:
            sum += k
        k += 1
    print()
print(sum)
print("\n")


for i in range(0,qator):
    for j in range(0,ustun):
        if i >=j:
            print('*',end=' ')
        else:
            print(' ', end=' ')
    print()
print("\n")




for i in range(0,qator):
    for j in range(0,ustun):
        if i >=j:
            print( j +1,end=' ')
        else:
            print(' ', end=' ')
    print()
print("\n")

for i in range(0,qator):
    for j in range(0,ustun):
        if i >=j:
            print( i +1,end=' ')
        else:
            print(' ', end=' ')
    print()
print("\n")

