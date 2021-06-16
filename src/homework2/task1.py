rub = int(input("Укажите стоимость, руб: "))
penny = int(input("Укажите стоимость, коп: "))
q = int(input("Укажите количество: "))

price_q = (rub * 100 + penny) * q
price_rub = price_q // 100
price_penny = price_q % 100

print("Общая ст-ть: " + str(price_rub) + "руб. " + str(price_penny) + "коп.")
