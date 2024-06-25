
def longestCommonPrefix(strs: list[str]) -> str:
    res = ""
    for ind, val in enumerate(strs[0]):
        for j in strs:
            if ind+1 > len(j) or j[ind] != val:
                return res
        else:
            res = res + val
    return str(res)


def test1_longestCommonPrefix():
    res = longestCommonPrefix(["flower","flow","flight"])
    assert "fl"

def test2_longestCommonPrefix():
    res = longestCommonPrefix(["dog","racecar","car"])
    assert len(res) == 0

def test3_longestCommonPrefix():
    res = longestCommonPrefix(["dog","door","dodge",'doubt'])
    assert "do"

def test4_longestCommonPrefix():
    res = longestCommonPrefix(["flower","flow","flight","fl"])
    assert "fl"

def test5_longestCommonPrefix():
    res = longestCommonPrefix(["cir","car"])
    assert "c"
