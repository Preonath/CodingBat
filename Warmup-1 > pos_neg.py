def pos_neg(a,b,negative):
    a=int(a)
    b=int(b)
    if ((a < 0 and b > 0) or (a > 0 and b < 0)):
        if (negative!=True):
            return True
        else:
            return False
    elif (negative):
        if(a<0 and b<0 ):
         return True
        else:
         return False
    else:
        return False


a,b,c = input().split(",")
print(pos_neg(a,b,c))