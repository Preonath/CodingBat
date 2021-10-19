def double_char(str):
    new_str = "".join([i + j for i, j in zip(list(str), list(str))])
    return(new_str)
s=input()
print(double_char(s))