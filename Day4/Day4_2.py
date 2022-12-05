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
        
        section_length = 0
        
        if first_elf_second_num >= second_elf_second_num:
            section_length = first_elf_second_num
        else:
            section_length = second_elf_second_num
        
        first_elf_section = [None] * (section_length+1)
        
        for num in range(first_elf_first_num, first_elf_second_num+1):
            first_elf_section[num] = num        

        second_elf_section = [None] * (section_length+1)

        for num in range(second_elf_first_num, second_elf_second_num+1):
            second_elf_section[num] = num

        for first_num, second_num in zip(first_elf_section, second_elf_section):
            if first_num and second_num != None:
                total_full_overlaps += 1
    
    print(total_full_overlaps)
