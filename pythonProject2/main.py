import pandas as pd
money = pd.read_csv("money.csv",encoding='cp949')

print("<<<<<<<<<<<<<법인의 측면>>>>>>>>>>>")

#사고원인별 법인사고건수의 평균
Aver_by_region = money.groupby(['사고원인'])['법인사고건수'].mean()
print(Aver_by_region)

#사고원인별 법인사고금액(억원)
Aver_by_region = money.groupby(['사고원인'])['법인사고금액(억원)'].mean()
print(Aver_by_region)

#보증종류별 법인 사고 건수
Aver_by_region = money.groupby(['보증종류'])['법인사고건수'].mean()
print(Aver_by_region)

#보증종류별 법인사고금액(억원)
Aver_by_region = money.groupby(['보증종류'])['법인사고금액(억원)'].mean()
print(Aver_by_region)

#법인 사고 건수 10순위
print(money.sort_values(by=['법인사고건수'],ascending=False).head(10))

#법인 사고 금액 10순위
print(money.sort_values(by=['법인사고금액(억원)'],ascending=False).head(10))

print("<<<<<<<<<<<<<<<<<<<<개인의 문제>>>>>>>>>>>>>>>>>>")

#사고원인별 개인 사고건수의 평균
Aver_by_region = money.groupby(['사고원인'])['개인사고건수'].mean()
print(Aver_by_region)

#사고원인별 개인사고금액(억원)
Aver_by_region = money.groupby(['사고원인'])['개인사고금액(억원)'].mean()
print(Aver_by_region)

#보증종류별 개인사고건수
Aver_by_region = money.groupby(['보증종류'])['개인사고건수'].mean()
print(Aver_by_region)

#보증종류별 개인사고금액(억원)
Aver_by_region = money.groupby(['보증종류'])['개인사고금액(억원)'].mean()
print(Aver_by_region)

#개인 사고 건수 10순위
print(money.sort_values(by=['개인사고건수'],ascending=False).head(10))

#개인 사고 금액 10순위
print(money.sort_values(by=['개인사고금액(억원)'],ascending=False).head(10))