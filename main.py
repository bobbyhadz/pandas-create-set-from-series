# How to Create a Set from a Series in Pandas

import pandas as pd

s = pd.Series([1, 2, 3, 3, 1, 4, 5, 5])

unique = s.unique()
print(unique)  # 👉️ [1 2 3 4 5]

# 👇️ <class 'numpy.ndarray'>
print(type(unique))

a_set = set(unique)
print(a_set)  # 👉️ {1, 2, 3, 4, 5}