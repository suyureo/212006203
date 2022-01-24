kind = eval(input("请选择你的贷款类型：1.商业贷款、2.公积金贷款（只需要输入序号即可）"))
money = eval(input("请输入你的贷款金额（单位：万元）："))
year = eval(input("请输入你的贷款期限："))

rate=0

if kind == 1:
    if year<=5:
        rate=0.0475
    else :
        rate=0.0490
elif kind == 2:
    if year <= 5:
        rate = 0.0275
    else:
        rate = 0.0325

month_rate=rate/12


month_money= 10000*money * (month_rate*((1+month_rate)**(year*12)))/( ( (1+month_rate)**(year*12) ) -1)

total=month_money*year*12

more=total-money*10000

print("月供参考：%.0f元"%month_money)
print("还款总额：%.0f元"%total)
print("支付利息：%.0f元"%more)