"""
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
"""

s = ["h", "e", "l", "l", "o"]

# list method start


def reverseString(s):
    i, j = 0, len(s) - 1

    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s
# print(reverseString(s))
# list method end


# recursive method start
# Notice: input is list not string
def reverseString_recur(s):

    # End condition
    if len(s) == 1:
        return s
    # recursive part: decompose big problem into subs
    else:
        new_s = reverseString_recur(s[1:]) + [s[0]]
        return new_s


print(reverseString_recur(s))

# recursive method start
