
num1 = '9'
num2 = '9'


def multiply(num1, num2):
    sums = []
    l1 = len(num1)
    l2 = len(num2)

    if l1 < l2:
        small = num1[::-1]
        big = num2[::-1]
    else:
        small = num2[::-1]
        big = num1[::-1]

    for index, factor in enumerate(small):
        temp_sum = ""
        carry = 0
        for num in big:
            rlt = int(num) * int(factor) + carry
            carry = rlt // 10 if rlt >= 10 else 0
            temp_sum += str(rlt % 10)

        if carry != 0:
            temp_sum += str(carry)
        temp_sum = "0" * index + temp_sum
        sums.append(temp_sum)

    base = '0'
    for temp in sums:
        base = addTwoReverseNums(base, temp)

    if len(set(base)) == 1 and set(base) == {'0'}:
        base = '0'
    return base[::-1]


def addTwoReverseNums(n1, n2):
    # zero-padding
    pad = abs(len(n1) - len(n2))

    if pad == 0:
        pass
    elif len(n1) > len(n2):
        n2 += '0' * pad
    else:
        n1 += '0' * pad

    carry = 0
    rlt = ''
    for i, j in zip(n1, n2):
        temp_sum = int(i) + int(j) + carry

        carry = 1 if temp_sum >= 10 else 0
        rlt += str(temp_sum % 10)

    if carry == 1:
        rlt += '1'

    return rlt


print(multiply(num1, num2))
