# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import fractions

string1 = input("Введите первую дробь: ")
string2 = input("Введите вторую дробь: ")

fraction1 = string1.split("/")
fraction2 = string2.split("/")

multFractionsNumerator = int(fraction1[0]) * int(fraction2[0])
multFractionsDenominator = int(fraction1[1]) * int(fraction2[1])
print(f"{multFractionsNumerator}/{multFractionsDenominator}")

summFractionsNumerator = int(fraction1[0]) * int(fraction2[1]) + int(fraction2[0]) * int(fraction1[1])
summFractionsDenominator = int(fraction1[1]) * int(fraction2[1]) + int(fraction1[1]) * int(fraction2[1])
print(f"{summFractionsNumerator}/{summFractionsDenominator}")

f1 = fractions.Fraction(int(fraction1[0]), int(fraction1[1]))
f2 = fractions.Fraction(int(fraction2[0]), int(fraction2[1]))

print(f1, f2, f1 * f2, sep=",")
print(f1, f2, f1 + f2, sep=",")