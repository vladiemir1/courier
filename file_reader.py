# координаты и масса для заказов в текстовом документе расположены через пробел друг под другом(x y m).
# координаты, грузоподьемность и имя для курьера в текстовом документе через пробел
orders = open("orders.txt", "r")         # Открытие файлов с координатами курьеров и заказов
couriers = open("courier.txt", "r")

orders = [line.rstrip() for line in orders]
# операции с заказами

arr_orders = []
for i in orders:
    for y in i:
        if y != ' ':
            arr_orders.append(y.split(' '))




print(arr_orders)

''''
arr_couriers = []
for i in courier:
    for y in i:
        if y != ' ':
            arr_couriers.append(y.split())

arr_couriers = []
couriers = [line.rstrip() for line in couriers]
for i in couriers:
    arr_couriers.append(int(couriers.readline()))
print(arr_couriers)
'''








