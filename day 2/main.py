import os

# Memory Complexity: O(1)
# Runtime Complexity: O(n)

if __name__ == "__main__":

    # Set working directory to file location
    path_dir = os.path.dirname(os.path.abspath(__file__))  
    os.chdir(path_dir)

    convert_code_1 ={
        'A': 'rock',
        'B': 'paper',
        'C': 'scissors',
    }

    convert_code_2_problem_1 ={
        'X': 'rock',
        'Y': 'paper',
        'Z': 'scissors',
    }

    convert_code_2_problem_2 ={
        'X': 'lose',
        'Y': 'draw',
        'Z': 'win',
    }

    rock_paper_scissors ={
        'rock': {'paper':False,'scissors':True},
        'paper': {'rock':True,'scissors':False},
        'scissors': {'rock':False,'paper':True},
    }


    def outcome_score(player,opponent):
        if opponent == player:
            return 3
        elif rock_paper_scissors[player][opponent]:
            return 6
        else:
            return 0
        
    def shape_score(hand):
        if hand == 'rock':
            return 1
        elif hand == 'paper':
            return 2
        elif hand == 'scissors':
            return 3
        else:
            return None

    def score(player,opponent):
        score_player = shape_score(player) + outcome_score(player,opponent)
        score_opponent = shape_score(opponent) + outcome_score(opponent,player)
        return score_player,score_opponent
    
    def find_player(opponent,outcome):
        if outcome == 'draw':
            return opponent
        for key,item in rock_paper_scissors[opponent].items():
            if item == (outcome == 'lose'):
                return key

    # Problem 1 
    file = open('input.txt', 'r')
    Lines = file.readlines()
    total_score_player = 0
    total_score_opponent = 0
    for line in Lines:
        opponent= convert_code_1[line[0]]
        player =  convert_code_2_problem_1[line[2]]
        score_player,score_opponent = score(player,opponent)
        total_score_player += score_player
        total_score_opponent += score_opponent
    print('Problem 1')
    print('Score player: ' + str(total_score_player))
    print('Score opponent: ' + str(total_score_opponent))

    # Problem 2
    file = open('input.txt', 'r')
    Lines = file.readlines()
    total_score_player = 0
    total_score_opponent = 0
    for line in Lines:
        opponent= convert_code_1[line[0]]
        outcome =  convert_code_2_problem_2[line[2]]
        player = find_player(opponent,outcome)
        score_player,score_opponent = score(player,opponent)
        total_score_player += score_player
        total_score_opponent += score_opponent
    print('Problem 2')
    print('Score player: ' + str(total_score_player))
    print('Score opponent: ' + str(total_score_opponent))




        

   
