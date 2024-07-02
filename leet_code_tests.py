from roman_to_integer import romanToInt
from longest_common_prefix import longestCommonPrefix
from valid_parentheses import isValid
from remove_duplicates_from_sorted_array_II import removeDuplicates
from valid_palindrome import isPalindrome
from minimum_size_subarray_sum import minSubArrayLen
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

"""valid_palindrome"""
def test1_valid_palindrome():
    res = isPalindrome("A man, a plan, a canal: Panama")
    assert res == True
def test2_valid_palindrome():
    res = isPalindrome("race a car")
    assert res == False
def test3_valid_palindrome():
    res = isPalindrome(" ")
    assert res == True

"""minimum_size_subarray_sum"""
def test1_minimum_size_subarray_sum():
    res = minSubArrayLen(7, [2,3,1,2,4,3])
    assert res == 2
def test2_minimum_size_subarray_sum():
    res = minSubArrayLen(4, [1,4,4])
    assert res == 1
def test3_minimum_size_subarray_sum():
    res = minSubArrayLen(11, [1,1,1,1,1,1,1,1])
    assert res == 0
def test4_minimum_size_subarray_sum():
    res = minSubArrayLen(15, [5,1,3,5,10,7,4,9,2,8])
    assert res == 2
def test5_minimum_size_subarray_sum():
    res = minSubArrayLen(7, [8])
    assert res == 1
