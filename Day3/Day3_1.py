LOWERCASE_ASCII_VALUE_OFFSET = 96
UPPERCASE_ASCII_VALUE_OFFSET = 38

total_priority = 0
with open("priority.txt") as rpsFile:
    lines = []
    for line in rpsFile:
        line = line.rstrip()

        first_half, second_half = line[:len(line)//2], line[len(line)//2:]

        common_character = list(set(first_half) & set(second_half))[0]
        
        if ord(common_character) <= 122 and ord(common_character) >= 97:
            priority_value = ord(common_character) - LOWERCASE_ASCII_VALUE_OFFSET
            total_priority += priority_value
        else:
            priority_value = ord(common_character) - UPPERCASE_ASCII_VALUE_OFFSET
            total_priority += priority_value

    print(total_priority)
