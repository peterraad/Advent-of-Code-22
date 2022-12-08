with open("signal.txt") as rpsFile:
    lines = []
    
    start_packet_position = 0
    end_packet_position = 14
    
    for line in rpsFile:
        line = line.rstrip()
        
        potential_signal = line[start_packet_position:end_packet_position]

        while len(set(potential_signal)) != len(potential_signal):
            start_packet_position +=1
            end_packet_position +=1

            potential_signal = line[start_packet_position:end_packet_position]

        print(end_packet_position)