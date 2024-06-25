def longestCommonPrefix(strs: list[str]) -> str:
    res = ""
    for ind, val in enumerate(strs[0]):
        for j in strs:
            if ind+1 > len(j) or j[ind] != val:
                return res
        else:
            res = res + val
    return str(res)

