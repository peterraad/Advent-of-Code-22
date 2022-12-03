opponent_rps_dict = {'A': 'ROCK', 'B': 'PAPER', 'C': 'SCISSORS'}
my_rps_dict = {'X': 'ROCK', 'Y': 'PAPER', 'Z': 'SCISSORS'}
outcome_dict = {'ROCKPAPER': ('ME', 8), 'PAPERSCISSORS': ('ME', 9), 'SCISSORSROCK': ('ME', 7), 'PAPERROCK': ('OPPONENT', 1), 'SCISSORSPAPER': (
    'OPPONENT', 2), 'ROCKSCISSORS': ('OPPONENT', 3), 'ROCKROCK': ('DRAW', 4), 'PAPERPAPER': ('DRAW', 5), 'SCISSORSSCISSORS': ('DRAW', 6)}
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

            my_round_score = outcome_dict[outcome_key][1]

            my_total_score += my_round_score


print("my score: ", my_total_score)
