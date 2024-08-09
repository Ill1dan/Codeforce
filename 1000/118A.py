def String(s):
    vowels = {"a", "e", "i", "o", "u", "y"}
    consonents = ""

    for x in s:
        x = x.lower()
        if x not in vowels:
            consonents += x

    res = ""
    for i in consonents:
        res += f".{i}"

    return res

s = input()
print(String(s))