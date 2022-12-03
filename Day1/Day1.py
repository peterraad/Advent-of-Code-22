
biggest_total = 0
current_total = 0

with open("cal.txt") as calFile:
    lines = []
    for line in calFile:
        print(line)
        if not line in ('\n', '\r\n'):
            current_total = current_total + int(line)
        else:
            if current_total > biggest_total:
                biggest_total = current_total
            
            current_total = 0

    
print("BIGGEST: ", biggest_total)
