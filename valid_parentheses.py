def isValid( s: str) -> bool:
    res = []
    d = {
        ']': '[',
        ')': '(',
        '}': '{',
    }
    for i in s:
        if i in d.values():
            res.append(i)
        elif (i in d) and (res) and (d[i] == res[-1]):
            res.pop()
        else:
            return False
    if not res:
        return True
