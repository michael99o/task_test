#необходимо узнать на какой год сумма твоего вклада превысит 3000 руб. и вывести данные о капитализации за каждый год
money = int(input('Введите сумму вклада: '))
percent = float(input('Введите процентную ставку: '))/100+1
stop_year = int(input('Введите длительность вклада в годах: '))
year = 0
god1 = [1]
god2 = [2, 3, 4]
god3 = list(range(5,16))

while year < stop_year:
    money *= percent
    year += 1
    if year in god1:
        god = 'год'
    if year in god2:
        god = 'года'
    if year in god3:
        god = 'лет'
    print(f'Через {year} {god}, сумма вклада составит {round(money, 2)} руб.')