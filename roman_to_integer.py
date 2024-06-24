def romanToInt(s: str) -> int:
    res = 0
    d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    for i in range(len(s)-1):
        if d[s[i]] < d[s[i+1]]:
            res -= d[s[i]]
        elif d[s[i]] >= d[s[i+1]]:
            res += d[s[i]]
    res += d[s[-1]]
    return res

if __name__ == "__main__":
    print(romanToInt(input()[1:-1]))

def test_first():
    res = romanToInt("III")
    assert 3
def test_second():
    res = romanToInt("LVIII")
    assert 58
def test_third():
    res = romanToInt("MCMXCIV")
    assert 1994
