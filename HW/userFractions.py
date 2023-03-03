# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import fractions

string1 = input("Введите первую дробь: ")
string2 = input("Введите вторую дробь: ")

summFractions = 12 + 12
multiplicationFractions = 12 * 12

f1 = fractions.Fraction(2, 10)
f2 = fractions.Fraction(2, 12)

print(f1, f2, f1 * f2, sep=",")