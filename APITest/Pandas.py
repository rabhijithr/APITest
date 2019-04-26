import pandas as pd

A = pd.read_csv("c1.csv", header=None).drop_duplicates()
B = pd.read_csv("c2.csv", header=None).drop_duplicates()
# print(A + B)
# print(A)

# A - B
print(pd.merge(A, B, how='left', indicator=True).query("_merge == 'left_only'"))
# B - A
# print(pd.merge(A, B, on='col', how='right', indicator=True).query("_merge == 'right_only'"))


# A = pd.DataFrame({'product id':   [1455,5452,3775],
#                     'serial number':[44,55,66]})
#
# print (A)
#
# B = pd.DataFrame({'product id':   [7000,2000,1000],
#                     'serial number':[44,55,77]})
#
# print (B)
#
# print (pd.merge(A, B, on='serial number'))
