def convert_string_to_ascii(s):
    """Convert a string to its ASCII representation"""
    return [ord(c) for c in s]


def convert_decimal_to_binary(decimal):
    """Convert a decimal number to binary"""
    return bin(decimal)


def convert_decimal_to_hexadecimal(decimal):
    """Convert a decimal number to hexadecimal"""
    return hex(decimal)


def convert_decimal_to_octal(decimal):
    """Convert a decimal number to octal"""
    return oct(decimal)


# Loop to repeat the program
while True:
    # Get user input
    input_type = input("What would you like to convert? Enter 'string' or 'decimal', or 'exit' to quit: ")

    if input_type == "string":
        # Convert string to ASCII
        s = input("Enter a string to convert to ASCII: ")
        ascii_values = convert_string_to_ascii(s)
        print("ASCII representation:", ascii_values)
    elif input_type == "decimal":
        # Convert decimal to binary, hexadecimal, and octal
        decimal = int(input("Enter a decimal number to convert: "))
        binary = convert_decimal_to_binary(decimal)
        hexadecimal = convert_decimal_to_hexadecimal(decimal)
        octal = convert_decimal_to_octal(decimal)
        print("Binary representation:", binary)
        print("Hexadecimal representation:", hexadecimal)
        print("Octal representation:", octal)
    elif input_type == "exit":
        # Exit the program if the user enters 'exit'
        break
    else:
        print("Invalid input type. Please enter 'string', 'decimal', or 'exit'.")
