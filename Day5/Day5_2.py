import re

REGEX_SEARCH_STRING = r'\d+'
total_full_overlaps = 0
# stack_1 = (1, ['D', 'T', 'R', 'B', 'J', 'L', 'W', 'G'])
# stack_2 = (2, ['S', 'W', 'C'])
# stack_3 = (3, ['R', 'Z', 'T', 'M'])
# stack_4 = (4, ['D', 'T', 'C', 'H', 'S', 'P', 'V'])
# stack_5 = (5, ['G', 'P', 'T', 'L', 'D', 'Z'])
# stack_6 = (6, ['F', 'B', 'R', 'Z', 'J', 'Q', 'C', 'D'])
# stack_7 = (7, ['S', 'B', 'D', 'J', 'M', 'F', 'T', 'R'])
# stack_8 = (8, ['L', 'H', 'R', 'B', 'T', 'V', 'M'])
# stack_9 = (9, ['Q', 'P', 'D', 'S', 'V'])


stack = [['D', 'T', 'R', 'B', 'J', 'L', 'W', 'G'],
         ['S', 'W', 'C'],
         ['R', 'Z', 'T', 'M'],
         ['D', 'T', 'C', 'H', 'S', 'P', 'V'],
         ['G', 'P', 'T', 'L', 'D', 'Z'],
         ['F', 'B', 'R', 'Z', 'J', 'Q', 'C', 'D'],
         ['S', 'B', 'D', 'J', 'M', 'F', 'T', 'R'],
         ['L', 'H', 'R', 'B', 'T', 'V', 'M'],
         ['Q', 'P', 'D', 'S', 'V']
        ]
with open("stacks.txt") as rpsFile:
    lines = []

    for line in rpsFile:
        line = line.rstrip()
        num_list = re.findall(REGEX_SEARCH_STRING, line)
        move_amount = int(num_list[0])
        from_stack_number = int(num_list[1])-1

        to_stack_number = int(num_list[2])-1
        print('-------------------')
        for list in stack:
            print(list)
        new_stack_list_add_elements = stack[from_stack_number][-move_amount:]
        stack[from_stack_number] = stack[from_stack_number][:-move_amount]
        stack[from_stack_number].remove
        stack[to_stack_number].extend(new_stack_list_add_elements)

        # while move_counter < move_amount:
        #     new_stack_list = stack[from_stack_number][-move_amount:]
        #     item_to_be_moved = stack[from_stack_number].pop()
        #     stack[to_stack_number].append(item_to_be_moved)
        #     move_counter +=1
        




    for list in stack:
        print(list.pop())