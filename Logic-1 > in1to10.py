def in1to10(n, outside_mode):
    if(outside_mode==True):
        if(n<=1 or n>=10):
            return True
    if(outside_mode==False):
        if(n>=1 or n<=1):
            return True
    return False