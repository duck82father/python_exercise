# learn3.py

# 데이터 다듬기
import os
import pandas as pd

cwd = os.getcwd()

df = pd.read_csv(os.path.join(cwd, "data", "basketball_stat.csv"))

# 데이터에서 분별력이 없는 특징(feature) 제거
df.drop(['2P', 'AST', 'STL'], axis=1, inplace=True)

print(df.head())