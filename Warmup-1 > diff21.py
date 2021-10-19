def diff21(n):
    if (n < 21):
        return (21 - n)
    else:
        return (2 * (n - 21))
n=int(input())
print(diff21(n))