import sys
import numpy
import math

l, h = [int(i) for i in input().split()]
mayan_digits = []
for i in range(h):
    mayan_digits.append(input())
mayan_digits = numpy.array(mayan_digits)


def get_mayan_digit(digit):
    result = []
    for i in range(0, h):
        result.append(mayan_digits[i][digit * l:digit * l + l])
    return result


def get_number_for_digits(digits):
    number = 0
    for i in range(len(digits)):
        number += digits[i] * math.pow(20, i)
    return number


def get_number(number):
    mayan_digit = []
    digits = []
    for i in range(len(number)):
        mayan_digit.append(number[i])
        if len(mayan_digit) == h:
            for j in range(0, 20):
                if mayan_digit == get_mayan_digit(j):
                    digits.insert(0, j)
            mayan_digit = []
    return get_number_for_digits(digits)


def number_to_base(start_number, base):
    digits = []
    number = start_number
    if number == 0:
        digits.insert(0, 0)
    while number > 0:
        digits.insert(0, number % base)
        number = number // base
    print("Converter number", start_number, "to base",
          base, "with result", digits, file=sys.stderr)
    return digits


def perform_operation(num_1, num_2, operation):
    num_result = 0
    if operation == '+':
        num_result = num_1 + num_2
    elif operation == '-':
        num_result = num_1 - num_2
    elif operation == '*':
        num_result = num_1 * num_2
    elif operation == '/':
        num_result = num_1 / num_2
    print("Performed operation", num_1, operation, num_2,
          "with result", num_result, file=sys.stderr)
    return num_result


num_1_arr = []
num_2_arr = []

s1 = int(input())
for i in range(s1):
    num_1_arr.append(input())
s2 = int(input())
for i in range(s2):
    num_2_arr.append(input())
operation = input()

num_1 = get_number(num_1_arr)
num_2 = get_number(num_2_arr)
num_result = int(perform_operation(num_1, num_2, operation))
result_digits = number_to_base(num_result, 20)

result_mayan_number = ""
for digit in result_digits:
    result_mayan_number += "\n".join(get_mayan_digit(digit))
    result_mayan_number += "\n"

print(result_mayan_number.strip())
