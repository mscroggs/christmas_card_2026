from itertools import product

# 1
count = 0
for i in product(["0", "1"], repeat=17):
    n = int("".join(i))
    if n > 0:
        count += 1
print(count)

# 2
count = 0
for l in range(1, 18):
    for i in product(["1", "2"], repeat=l):
        count += 1
print(count)

# 3
count = 0
for tennis in range(1, 77):
    for cricket in range(1, 77):
        if tennis > cricket:
            count += 1
print(count)

# 4
count = 0
for tennis in range(1, 40):
    for cricket in range(1, 40):
        if [tennis, cricket].count(1) == [tennis, cricket].count(2):
            count += 1
print(count)

# 5
def two_tilings(n):
    if n == 0:
        return [""]
    if n == 1:
        return ["|"]
    return ["|" + i for i in two_tilings(n - 1)] + ["==" + i for i in two_tilings(n - 2)]

print(len(two_tilings(17)))

# 6
def three_tilings(n):
    if n == 0:
        return [""]
    if n == 1:
        return ["|"]
    if n == 2:
        return ["||"]
    return ["|" + i for i in three_tilings(n - 1)] + ["===" + i for i in three_tilings(n - 3)]

print(len(three_tilings(35)))

# 7
row = [1]
index = None
while index is None:
    n = len(row) + 2
    next = row[-1] + 1
    if 1042 in row:
        index = row.index(1042)
    row = list(range(next, next + n))
print(row[index + 1])

# 8
row = [1]
index = None
while len(row) != 19627:
    n = len(row) + 2
    next = row[-1] + 1
    row = list(range(next, next + n))
print(row[-1])

# 9
def numbers(n):
    if n == 0:
        return {0: 1}
    pre = numbers(n - 1)
    out = {i: 0 for i in range(min(pre) + 1, max(pre) + 7)}
    for i, n in pre.items():
        for j in range(1, 7):
            out[i + j] += n
    return out

{i: 1 for i in range(1, 6)}

m = (-1, 0)
for i, n in numbers(888).items():
    if n > m[1]:
        m = (i, n)
    elif n == m[1]:
        m = ([m[0], i], m[1])
print(m[0])

# 9
ndice = 0
counts = {0: 1}
while counts.get(1888, -1) != counts.get(6330, -2):
    ndice += 1
    new = {i: 0 for i in range(min(counts) + 1, max(counts) + 7)}
    for i, n in counts.items():
        for j in range(1, 7):
            new[i + j] += n
    counts = new
print(ndice)
