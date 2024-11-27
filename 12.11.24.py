# x=int(input("x: "))
# summa=''
# while x>=1:
#     qoldiq=x%2
#     summa=str(qoldiq)+summa
#     x//=2
# print(summa)

# konfet=int(input("100gr konfet narxi :"))
# i=100
# for x in range(i,1000,100):
#     nat=i*konfet
#     print(nat)

# list=[47,82,24,36,]
# list1=[]
# i=0
# while i<len(list):
#     print(list[i])
#     b=list[i]//10
#     o=list[i]%10
#     list1.append(b+o)
#     i+=1
# print(list1)
# 1-masala
# i=1
# summa=0
# for x in range(i,101):
#     summa+=i
#     print(i)
#     i+=1
# print(summa)


# 2-masala
# i=2
# juft=0
# for x in range(i,50):
#     juft+=i
#     print(i)
#     i+=2
# print(juft)


# i=1
# toq=0
# for x in range(i,50):
#     toq+=i
#     print(i)
#     i+=2
# print(toq)

# 3-masala
# i=-80
# sanoq=0
# for x in range(i,81):
#     if i%7==0:
#         sanoq+=1
#         print(i)
#     i+=1
# print(F"{sanoq} ta bo'linadi")


# 4-masala
# mevalar=['olma','banan','apelsin','olma']
# sanoq=0
# for i in mevalar:
#     if 'olma'==i:
#         sanoq+=1
# print(sanoq)

# 5-masala
# A=int(input("A son kiriting: "))
# B=int(input("B son kiriting: "))
# toq=0
# juft=0
# for i in range(A,B):
#     if i%2==0:
#         juft+=1
#         print(i)
#     else:
#         toq+=1
#         print(i)
# print(f"{juft} ta juft son bor")
# print(f"{toq} ta toq son bor")

# for i in range(3,101):
#     if i%3==0:
#         continue
#     print(i)
    
# for i in range(-99,100):
#     if i>-10 and i<10:
#         continue
#     print(i)

# i=1
# while i<=10:
#     if i==5:
#         i+=1
#         continue
#     print(i)
#     i+=1

# check=False
# list=[5,8,6,2,4]
# for i in list:
#     if i==6:
#         break
# print(i)

# son=int (input("son kiritiing:"))
# check=True
# sanoq=0
# for i in range(1,son+1):
#     if i%2==0:
#         sanoq+=1
#         if sanoq>2:
#             check=False
#             break
# if check:
#     print(f"{son} tub")
# else:
#     print(f"{son} tub emas")

# 6-masala
# list=[1,2,3,4,5,6,6,7,8,9,10]
# sanoq=0
# for i in list:
#     if i%2==0:
#         sanoq+=1
#         print(i)
# print(f"2 ga bo'linadganlar soni {sanoq} ta")        

# 7-masala
str=(input("satr kiriting : "))
sanoq=0
for i in str:
    if 64< chr(str[i]) <91:
        sanoq += i
print (sanoq)