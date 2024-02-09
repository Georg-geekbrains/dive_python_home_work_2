# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions

from fractions import Fraction

def add_and_multiply_fractions(fraction1, fraction2):
    
    num1, den1 = map(int, fraction1.split('/'))
    num2, den2 = map(int, fraction2.split('/'))

    f1 = Fraction(num1, den1)
    f2 = Fraction(num2, den2)

    sum_fraction = f1 + f2
    product_fraction = f1 * f2

    return sum_fraction, product_fraction

fraction1 = input("Введите первую дробь в формате a/b: ")
fraction2 = input("Введите вторую дробь в формате a/b: ")
sum_result, product_result = add_and_multiply_fractions(fraction1, fraction2)

print(f"Сумма дробей: {sum_result}")
print(f"Произведение дробей: {product_result}")