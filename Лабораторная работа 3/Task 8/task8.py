money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0
sum_money = money_capital + salary

while sum_money > 0:
    sum_money -= spend
    spend += spend * increase
    month += 1



print(month)
