money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

budget = money_capital
COUNT = 1
cur_expenses = spend

while budget >= cur_expenses:
    budget = budget + salary - cur_expenses
    # умножаем траты на множитель наращения каждый месяц
    cur_expenses *= (1 + increase)
    COUNT += 1

print("Количество месяцев, которое можно протянуть без долгов:", COUNT)
