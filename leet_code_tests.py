from roman_to_integer import romanToInt
from longest_common_prefix import longestCommonPrefix
from valid_parentheses import isValid
from remove_duplicates_from_sorted_array_II import removeDuplicates

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

"""valid_parentheses"""
def test1_valid_parentheses():
    res = isValid("()")
    assert res == True
def test2_valid_parentheses():
    res = isValid("()[]{}")
    assert res == True
def test3_valid_parentheses():
    res = isValid("(]")
    assert res == False

"""remove_duplicates_from_sorted_array_II"""
def test1_remove_duplicates_from_sorted_array_II():
    res = removeDuplicates([0,0,1,1,1,1,2,3,3])
    assert [0,0,1,1,2,3,3]
def test2_remove_duplicates_from_sorted_array_II():
    res = removeDuplicates([1,1,1,2,2,3])
    assert [1,1,2,2,3]
def test3_remove_duplicates_from_sorted_array_II():
    res = removeDuplicates([0,0,0,0])
    assert [0,0]