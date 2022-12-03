LOWERCASE_ASCII_VALUE_OFFSET = 96
UPPERCASE_ASCII_VALUE_OFFSET = 38

CHUNKED_LINE_AMOUNT = 3
total_priority = 0
with open("priority.txt") as rpsFile:
    lines = []
    for line in rpsFile:
        lines.append(line.rstrip())
        if len(lines) == CHUNKED_LINE_AMOUNT:
            common_character = list(set(lines[0]) & set(lines[1]) & set(lines[2]))[0]
            
            if ord(common_character) <= 122 and ord(common_character) >= 97:
                priority_value = ord(common_character) - LOWERCASE_ASCII_VALUE_OFFSET
                total_priority += priority_value
            else:
                priority_value = ord(common_character) - UPPERCASE_ASCII_VALUE_OFFSET
                total_priority += priority_value
            
            lines = []

    print(total_priority)
