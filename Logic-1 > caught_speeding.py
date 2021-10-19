def caught_speeding(speed, is_birthday):
    if(is_birthday):
        speed-=5
    if(speed<=60):
        return 0
    if(speed<=80 and speed>=61):
        return 1
    if(speed>=81):
        return 2