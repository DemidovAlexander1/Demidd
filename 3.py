def string_to_int(s):
    s = s.strip()
    sign = 1

    if s and s[0] == '-':
        sign = -1
        s = s[1:]

    result = 0
    for char in s:
        if '0' <= char <= '9':
            result = result * 10 + (ord(char) - ord('0'))
        else:
            break

    return result * sign


print(string_to_int('69'))
print(string_to_int('-69'))
print(string_to_int('6969 words'))
