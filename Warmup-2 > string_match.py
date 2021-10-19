def string_match(a,b):
    shorter=min(len(a),len(b))
    count=0
    for i in range(shorter-2+1):
        a_sb=a[i:i+2]
        b_sb=b[i:i+2]
        if(a_sb==b_sb):
            count+=1
    return count
a,b=input().split()
print(string_match(a,b))

