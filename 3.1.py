# a = list(range(0,10))
#
# print(a)
#
# print(a[-1])
#
# print(a[-5:-1])
#
# print(a[2:4])

# some_tuples = [((1,2), (3,4)), ((5,6), (7,8))]
# flattened = [z for tup in some_tuples for x in tup for z in x]
# print(flattened)

# f = lambda n: n % 2
#
# L = [x for x in range(1, 20) if f(x) == 1]
#
# print(L)

import numpy as np

arr = np.random.randn(5, 3)
print(arr)

arr.sort(0)

print(arr)