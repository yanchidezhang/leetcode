from time import time
# start = time()
# end = time()
# print(end - start)

# 帕斯卡三角（Pascal's Triangle）:
# 递归关系 f(i,j) = f(i-1,j-1) + f(i-1,j);
# f(i,j) = 1 where j = 1 or i=j
targetRow = 5


# def triangle(n):
#     if n == 0:
#         return [1]
#     else:
#         return [([0] + row(n - 1))[index] + (row(n - 1) + [0])[index] for index in range(n + 1)]


# start = time()
# print(row(targetRow))
# end = time() # 0.03157806396484375
# print(end - start)


def triangle(row):
    a = [1]

    for x in range(row + 1):
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]


start = time()
rows = triangle(targetRow)
counter = 0

for row in rows:
    counter += 1
    if counter == targetRow + 1:
        print(row)
end = time()  # 0.00008797645568847656
print(end - start)
