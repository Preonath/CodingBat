def monkey_trouble(a_smile,b_smile):
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    else:
        return False
a,b = input().split()
print(monkey_trouble(a,b))
