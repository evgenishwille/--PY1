salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
need_money = 0  # количество денег, чтобы прожить 10 месяцев
# need_money = extra_money + salary - spend
salary_sum = 0
spend_sum = 0

for i in range(months):
    salary_sum = salary_sum + salary

    if i == 0:
        spend_sum = spend_sum + spend

    if i > 0:
        spend = spend + spend * increase
        spend_sum =  spend_sum + spend

need_money = spend_sum - salary_sum
print(round(need_money))
