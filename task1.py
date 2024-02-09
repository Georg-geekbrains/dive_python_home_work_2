# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое
# представление.
# Функцию hex используйте для проверки своего результата.

def int_to_hex(n):
    hex_chars = "0123456789abcdef"
    if n == 0:
        return "0"
    hex_str = ""
    while n > 0:
        hex_str = hex_chars[n % 16] + hex_str
        n = n // 16
    return hex_str


num = int(input("Введите целое число: "))
hex_num = int_to_hex(num)
print(f"Шестнадцатеричное представление числа {num} - {hex_num}")
print(f"Проверка с использованием функции hex: {hex(num)}")