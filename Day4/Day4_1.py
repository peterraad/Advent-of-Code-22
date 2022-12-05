import re

REGEX_SEARCH_STRING = r'\d+'
total_full_overlaps = 0

with open("overlaps.txt") as rpsFile:
    lines = []
    for line in rpsFile:
        line = line.rstrip()

        num_list = re.findall(REGEX_SEARCH_STRING, line)

        first_elf_first_num = int(num_list[0])
        first_elf_second_num = int(num_list[1])

        second_elf_first_num = int(num_list[2])
        second_elf_second_num = int(num_list[3])

        if first_elf_second_num <= second_elf_second_num and first_elf_first_num >= second_elf_first_num:
            total_full_overlaps += 1

        elif first_elf_second_num >= second_elf_second_num and first_elf_first_num <= second_elf_first_num:
            total_full_overlaps += 1

    print(total_full_overlaps)