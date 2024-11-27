# son1=int(input("son1 ni kirit : "))
# son2=int(input("son2 ni kirit : "))
# while son1<=son2:
#     print(son1)
#     son1+=1

son1=int(input("son1 ni kirit : "))
son2=int(input("son2 ni kirit : "))
if son1<son2:
    while son1<=son2:
        print(son1)
        son1+=1
if son1>son2:
    while son2<=son1:
        print(son1)
        son1-=1
