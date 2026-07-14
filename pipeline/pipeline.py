import sys
import pandas as pd

print("arguments:", sys.argv)

month=int(sys.argv[1])

df=pd.DataFrame({"A":[1,2,3],"B":[4,5,6]})
print(df)
print(f"hello pipeline month: {month}")