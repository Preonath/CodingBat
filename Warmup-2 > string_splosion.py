def string_splosion(str):
    r=""
    for i in range(len(str)):
        r+=str[:i+1]
    return r
s= input()
print(string_splosion(s))
