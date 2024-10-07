def binary_to_decimal(binary_number):
    """Converts a binary number to its decimal equivalent.

    Arguments:
        binary_number -- a binary number

    Returns:
        decimal_number -- a decimal number
    """

    decimal_number = 0
    power = 0

    while binary_number > 0:
        last_digit = binary_number % 10
        decimal_number += last_digit * (2 ** power)
        power += 1
        binary_number //= 10

    return decimal_number


binary_input = int(input("Enter a binary number: "))

decimal_output = binary_to_decimal(binary_input)

print("Decimal number: ", decimal_output)
