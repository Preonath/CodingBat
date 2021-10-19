def sleep_in(weekday,vacation):
    if not weekday or vacation:
        return True
    else:
        return False
w,v = input().split()
print(sleep_in(w,v))