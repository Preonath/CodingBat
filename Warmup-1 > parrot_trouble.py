def parrot_trouble(talking, hour):
    hour=int(hour)
    if talking and hour<7:
        return True
    elif talking and hour > 20:
        return True
    else:
        return False
a,b = input().split()
print(parrot_trouble(a,b))

