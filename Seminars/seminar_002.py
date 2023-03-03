# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

print("Введите цифру действия(1 - Пополнить, 2 - Снять, 3 - Выйти: ")
number = int(input())
accountStatus = 10000
MIN_PERCENT = 30
MAX_PERCENT = 600
percent = 0
count = 0

match number:
    case 1:
        print("Пополнение счета (Процент за снятие — 1.5%, но не менее 30 и не более 600 у.е.)")
        temp = int(input("Введите сумму пополнения: "))
        if temp % 50 == 0:
            percent = temp * 1.5 / 100
            if percent <= MIN_PERCENT:
                accountStatus = temp - MIN_PERCENT
            elif percent >= MAX_PERCENT:
                accountStatus = temp - MAX_PERCENT
            elif MIN_PERCENT < percent < MAX_PERCENT:
                accountStatus = temp - percent
            print(f"Процент за пополнение: {percent}")
        else:
            print("Сумма пополнения должна быть кратна 50 у.е. ")
    case 2:
        print("Снятие со счета")
        summOut = int(input("Введите сумму снятия: "))
        if summOut < accountStatus:
            accountStatus -= summOut
        else:
            print("Недостаточно средств на счете.")
    case 3:
        print("Выход из программы")

print(f"На вашем счете {accountStatus} у.е.")