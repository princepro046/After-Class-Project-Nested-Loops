def decimal_to_binary_using_nested_loops(decimal_number):
    binary_number = ""
    
    # Outer loop to keep dividing the decimal number by 2
    while decimal_number > 0:
        # Inner loop handles the remainder and binary digit accumulation
        for _ in range(1):  # Inner loop runs only once per outer loop iteration
            remainder = decimal_number % 2
            binary_number = str(remainder) + binary_number  # Add the remainder at the front
            decimal_number = decimal_number // 2  # Integer division to halve the number
    
    return binary_number if binary_number else "0"  # Return "0" if the input was 0

# Taking input from the user
decimal_number = int(input("Enter a decimal number: "))

# Converting the decimal number to binary
binary_number = decimal_to_binary_using_nested_loops(decimal_number)

# Printing the binary number
print(f"The binary representation of {decimal_number} is: {binary_number}")
