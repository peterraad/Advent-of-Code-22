opponent_rps_dict = {'A': 'ROCK', 'B': 'PAPER', 'C': 'SCISSORS'}
my_rps_dict = {'X': 'LOSE', 'Y': 'DRAW', 'Z': 'WIN'}
outcome_dict = {'ROCKWIN': 8, 'PAPERWIN': 9, 'SCISSORSWIN': 7, 'PAPERLOSE': 1,
                'SCISSORSLOSE': 2, 'ROCKLOSE': 3, 'ROCKDRAW': 4, 'PAPERDRAW': 5, 'SCISSORSDRAW': 6}
my_total_score = 0

with open("rps.txt") as rpsFile:
    lines = []
    for line in rpsFile:
        if len(line) >= 3:
            opponent_encrypted_choice = line[0]
            my_encrypted_choice = line[2]


            opponent_choice = opponent_rps_dict[opponent_encrypted_choice]
            my_choice = my_rps_dict[my_encrypted_choice]

            outcome_key = opponent_choice+my_choice

            my_round_score = outcome_dict[outcome_key]

            my_total_score += my_round_score



print("my score: ", my_total_score)
