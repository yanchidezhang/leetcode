
n = 10  # NO.n element in the fib array
# Expecting result: 55

# recursive method start


def fib_re(n):

    # if n equals to 0
    if n == 0:
        # return 0, which means the head of the fib array is 0
        return 0
    if n == 1:
        # return 1, which means the second element of the fib array is 1
        return 1

    # do recursive math here, until we reach the head
    return fib_re(n - 1) + fib_re(n - 2)

# print(fib_re(n))

# recursive method end

# dynamic programming (top_down) method start
# it is also known as recursive method with memory


# memo for keeping the result of traversed nodes
# why n+1? it because 0 will be put at the head of array
# t0 simplify the calculation
memo = [-1] * (n + 1)


def fib_top_down(n):

    # if the current node was calculated
    if memo[n] != -1:
        # return the result directly
        return memo[n]

    # calculate the current node against 'n'
    if n == 0:
        temp = 0
    if n == 1:
        temp = 1
    if n > 1:
        temp = fib_top_down(n - 1) + fib_top_down(n - 2)

    # update the memo
    memo[n] = temp

    return memo[n]

# print(fib_top_down(n)) #print out result
# dynamic programming (top_down) method end

# dynamic programming (bottom_top) method start


def fib_bottom_top(n):
    # create memo for keeping the calcualtion result
    # again, we make the length of memo as 'n+1', cuz
    # 0 will be put at the head of fib array
    memo = [-1] * (n + 1)
    memo[0] = 0
    memo[1] = 1

    # populate the memo from bottom to the top
    # bottom -> top = sub-result -> final result
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]


print(fib_top_down(10))
# dynamic programming (bottom_top) method end
