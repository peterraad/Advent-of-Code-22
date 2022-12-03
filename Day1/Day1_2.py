
biggest_total = 0
current_total = 0
biggest_list = [0, 0, 0]

with open("cal.txt") as calFile:
    lines = []
    for line in calFile:
        if not line in ('\n', '\r\n'):
            current_total = current_total + int(line)
        else:
            if current_total > min(biggest_list):
                min_pos = biggest_list.index(min(biggest_list))
                biggest_list[min_pos] = current_total
                
            current_total = 0

for value in biggest_list:
    biggest_total += value
print("BIGGEST: ", biggest_total)
