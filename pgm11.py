def maximum(a,b,c):
    if(a>=b)and(a>=c):
        largest=a
    elif(b>=a)and(b>=c):
            largest=b
    else:
            largest=c
    return largest
#driver code
a=10
b=14
c=12
print("Largest is:",maximum(a,b,c))
