#!/usr/bin/env python
#simple calculcation done for Stellaris key contest among friends
#optimistic_const was question about number from 1 to 5
#quiz score from 0-100 here https://www.space.com/17791-milky-way-galaxy-quiz-trivia.html
#bad_luck was question about number from 1 to 1000
#also on https://repl.it/I59h/2 so every friend could launch it themselv

input_data = {
    "_CJ_": {
        "optimistic_const": 3,
        "quiz": 73,
        "bad_luck": 666
    },
    "paucto": {
        "optimistic_const": 3,
        "quiz": 82,
        "bad_luck": 720
    },
    "dwi": {
        "optimistic_const": 3,
        "quiz": 55,
        "bad_luck": 42
    },
    "Lance": {
        "optimistic_const": 3,
        "quiz": 73,
        "bad_luck": 609
    },
    "Skodak": {
        "optimistic_const": 4,
        "quiz": 45,
        "bad_luck": 256
    }
}

def calculate(data):
    result = {}
    print('Let\'s find a winner!\n')
    for hero in data:

      print('Calcaluting optimism and knowledge about Milky way.')
      score = data[hero]['optimistic_const'] * data[hero]['quiz']
      print(data[hero]['optimistic_const'], '*', data[hero]['quiz'], '=', score)
      
      print('Minus bad luck!')
      print(score, '-', data[hero]["bad_luck"]/10, '=', score-data[hero]["bad_luck"]/10)
      score -= (data[hero]["bad_luck"]/10)
      
      score_msg = '\n{} : {}'.format(hero, score)
      print(score_msg)
      print('=' * (len(score_msg)-1),'\n') #-1 because of \n from score_msg
      result[hero] = score

    #magic use of lambda I have no idea how works
    #but it will get the highest score
    winner = max(result.keys(), key=(lambda key: result[key]))
    
    #just to be sure
    highest_score = max(result.values())
    if result[winner] == highest_score:
        #highest scores belons to the winner
        winner_msg = '!The winner is {} with score: {}!'.format(winner, highest_score)
        print('!' * len(winner_msg))
        print(winner_msg)
        print('!' * len(winner_msg))
        return winner
    else:
        print('something went very wrong!')
        return False
    
calculate(input_data)
