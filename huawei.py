'''
1. 字符串去重
输入：12ere2

输出：12er
'''


def remove_dup(mystr):

    mydict = dict()

    for i in range(len(mystr)):
        if mystr[i] not in mydict:
            mydict[mystr[i]] = i

    return ''.join(list(mydict.keys()))


print(remove_dup('12ere2'))
