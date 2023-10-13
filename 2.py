binary_str = "10101110011"
decimal_num = 0
for digit in binary_str:
    decimal_num = decimal_num * 2 + int(digit)
print(decimal_num)
