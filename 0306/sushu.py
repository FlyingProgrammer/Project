def is_sushu(num):
    x=2
    while x<num :
        if(not num%x):
            return 0;
        x+=1
    return 1

# py3 range return a object
L= list(filter(is_sushu,list(range(1000,1500))))
print(L)
