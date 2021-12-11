import pandas as pd
accident = pd.read_csv("accident.csv" , encoding='cp949')

print(accident["공사비"].max())