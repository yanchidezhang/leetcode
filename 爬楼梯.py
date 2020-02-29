stairs = 5

# recursive method start


def claim_re(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        s1 = claim_re(n - 1)
        s2 = claim_re(n - 2)
    return s1 + s2


print(claim_re(stairs))
# recursive method end

# dynamic method start


def claim_dynamic(n):
    memo = [0] * (n + 1)
    memo[0], memo[1] = 1, 1

    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]


print(claim_dynamic(stairs))
# dynamic method end


def claim_dynamic(n):
    memo = [1, 1]

    for i in range(2, n + 1):
        memo.append(memo[i - 1] + memo[i - 2])

    return memo[n]


print(claim_dynamic(stairs))
