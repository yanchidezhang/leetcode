"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""

'''
算法说明：
用两个指针(A,B)同时指向list首元素，用一个字典来记录遍历过的字母
及其位置。如果遇到新字母，则添加到字典中，更新最大长度，并且向右移
动指针B。如果遇到的字母已经在字典中出现，那么更新指针A，将其指向当
前重复字母在字典中的后一个位置。

'''
def lengthOfLongestSubstring(s):
    if len(s) <= 1:
        return len(s)

    used = dict()
    start, maxLen = 0, 0

    for end, char in enumerate(s):

        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            maxLen = max(maxLen, end - start + 1)

        used[char] = end
        print(start, end, maxLen)
    return maxLen


mystr = "abcabcbb"
print(lengthOfLongestSubstring(mystr))
