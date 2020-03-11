"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

字符串 动态规划

回文的意思是正着念和倒着念一样，如：上海自来水来自海上
"""

# approach 1 中心扩散法
"""
首先往左寻找与当期位置相同的字符，直到遇到不相等为止。
然后往右寻找与当期位置相同的字符，直到遇到不相等为止。
最后左右双向扩散，直到左和右不相等
"""


def longestPalindrome(s):
    strLen = len(s)
    left = 0
    right = 0
    length = 1
    maxStart = 0
    maxLen = 0

    for i in range(strLen):
        left = i - 1
        right = i + 1

        while left >= 0 and s[left] == s[i]:
            length += 1
            left -= 1

        while right < strLen and s[right] == s[i]:
            length += 1
            right += 1

        while left >= 0 and right < strLen and s[left] == s[right]:
            length += 2
            left -= 1
            right += 1

        if length > maxLen:
            maxLen = length
            maxStart = left

        length = 1

    return s[maxStart + 1: maxStart + maxLen + 1]


mystr = "abba"
# print(longestPalindrome(mystr))

# dynamic programming approach
"""
我们用一个boolean dp[l][r]表示字符串从i到j这段是否为回文。
试想如果dp[l][r]=true，我们要判断dp[l-1][r+1]是否为回文。
只需要判断字符串在(l-1)和（r+1)两个位置是否为相同的字符，
是不是减少了很多重复计算。
"""


def dynamic_longestPalindrome(s):
    strLen = len(s)
    maxStart = 0
    maxEnd = 0
    maxLen = 1

    dp = []
    for l in range(strLen):
        row = []
        for r in range(strLen):
            if l == r:
                row.append(True)
            else:
                row.append(False)
        dp.append(row)

    for right in range(1, strLen):
        for left in range(0, right):
            if s[left] == s[right] and (r - l <= 2 or dp[left + 1][right - 1]):
                dp[left][right] = True
                if right - left + 1 > maxLen:
                    maxLen = right - left + 1
                    maxStart = left
                    maxEnd = right

    return s[maxStart:maxEnd + 1]


# print(dynamic_longestPalindrome(mystr))


# 中心扩散法Spread From Center
def spread(s, left, right):
    """
    left = right 的时候，此时回文中心是一条线，回文串的长度是奇数
    right = left + 1 的时候，此时回文中心是任意一个字符，回文串的长度是偶数
    """

    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    # 这里+1的原因是因为，每次while运行完
    # left都要-1。right不+1的原因是因为，
    # right位的数字不会被取出来
    return s[left + 1:right]


# 动态规划法-中心扩散法Spread From Center
def spread_from_center(s: str) -> str:

    if s == s[::-1]:
        return s
    res = s[:1]
    for i in range(len(s)):
        palindrome_odd = spread(s, i, i)
        palindrome_even = spread(s, i, i + 1)
        # 当前找到的最长回文子串
        res = max(palindrome_odd, palindrome_even, res, key=len)
    return res


ss = 'abaaaa'
print(spread_from_center('abaa'))
