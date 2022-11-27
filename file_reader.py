# координаты и масса для заказов в текстовом документе расположены через пробел друг под другом(x y m).
# координаты, грузоподьемность и имя для курьера в текстовом документе через пробел
orders = open("orders.txt", "r")         # Открытие файлов с координатами курьеров и заказов
couriers = open("courier.txt", "r")
order = orders.readlines()
courier = couriers.readlines()

# операции с заказами
order = [line.rstrip() for line in order]
arr_orders = []
for i in order:
    a = i.split()
    arr_orders.append(a)


print(arr_orders)





