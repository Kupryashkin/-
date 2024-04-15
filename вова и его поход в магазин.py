import random
money = random.randint(0, 120)
def shop():
    global money
    print("У Вовы есегодня {} денег".format(money))
    products =  t1 = "Вода - 20 рублей"; t2 = "Шоколадка - 40 рубей"; t3 = "Сок - 60 рублей"

    while True:
        choice = input("Что хочешь купить?(Вода, Шоколадка, Сок, или 'выход' для завершения покупки): ").lower()
        if choice == 'выход':
            print("До свидания")
            break
        if choice in products:
            if money >=products[choice]:
                print(f"Покупаем {choice}")
                money -=products[choice]
            else:
                print("Не хватает денег")
        else:
            print("Извините, такого товара нет в магазе")
shop()
