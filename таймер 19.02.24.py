import time

while True:
        seconds = int(input("Скок хочешь таймер делать?: "))
        if seconds <= 0:
            print("Введите число больше 0")
        else:
            break


while seconds > 0:
    print(f"Осталось {seconds} секунд")
    if seconds == 10:
        print("О!")

    time.sleep(1)
    seconds -= 1

print("Время вышло.")
