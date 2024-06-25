from roman_to_integer import romanToInt
from longest_common_prefix import longestCommonPrefix

"""roman_to_integer"""
def test1_romanToInt():
    res = romanToInt("III")
    assert 3
def test2_romanToInt():
    res = romanToInt("LVIII")
    assert 58
def test3_romanToInt():
    res = romanToInt("MCMXCIV")
    assert 1994

"""longest_common_prefix"""
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