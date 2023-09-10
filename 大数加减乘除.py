def add_large_numbers(num1, num2):
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)

    carry = 0
    result = []

    for i in range(max_len - 1, -1, -1):
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        carry = digit_sum // 10
        result.append(str(digit_sum % 10))

    if carry:
        result.append(str(carry))

    return ''.join(result[::-1])


num1 = "123456789012345678901234567890"
num2 = "987654321098765432109876543210"
result = add_large_numbers(num1, num2)
print(result)


def subtract_large_numbers(num1, num2):
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)

    borrow = 0
    result = []

    for i in range(max_len - 1, -1, -1):
        digit_diff = int(num1[i]) - int(num2[i]) - borrow
        if digit_diff < 0:
            digit_diff += 10
            borrow = 1
        else:
            borrow = 0
        result.append(str(digit_diff))

    return ''.join(result[::-1])


num1 = "123456789012345678901234567890"
num2 = "987654321098765432109876543210"
result = subtract_large_numbers(num1, num2)
print(result)


def multiply_large_numbers(num1, num2):
    num1 = num1[::-1]
    num2 = num2[::-1]

    product = [0] * (len(num1) + len(num2))

    for i in range(len(num1)):
        for j in range(len(num2)):
            product[i + j] += int(num1[i]) * int(num2[j])
            if product[i + j] >= 10:
                product[i + j + 1] += product[i + j] // 10
                product[i + j] %= 10

    while len(product) > 1 and product[-1] == 0:
        product.pop()

    return ''.join(map(str, product[::-1]))


num1 = "123456789012345678901234567890"
num2 = "987654321098765432109876543210"
result = multiply_large_numbers(num1, num2)
print(result)


def divide_large_numbers(dividend, divisor):
    dividend = int(dividend)
    divisor = int(divisor)

    quotient = dividend // divisor
    remainder = dividend % divisor

    return quotient, remainder


dividend = "123456789012345678901234567890"
divisor = "9876543210"
quotient, remainder = divide_large_numbers(dividend, divisor)
print("商:", quotient)
print("余数:", remainder)
