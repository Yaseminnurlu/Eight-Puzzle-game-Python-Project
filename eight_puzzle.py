#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: Yasemin Nurluoglu
# email: yaseminn@bu.edu
#
#

from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()
            
            
def process_file(filename, algorithm, param):
    """open the file with the specified filename for reading,
    and process it using the specified algorithm and param"""
    file = open(filename, 'r')
    text = file.read()
    file.close()
    states = []
    words = text.split()
    solved = 0
    avg = 0
    total = 0
    av_moves = 0    
    for word in words:
        init_board = Board(word)
        init_state = State(init_board, None, 'init')
        searcher = create_searcher(algorithm, param)
        soln = None
        try:
            soln = searcher.find_solution(init_state)

            if soln == None:
                print(str(word + ':'), 'no solution', end='')
                print()
                solved = 0
            else:
                print(str(word + ':'), soln.num_moves, 'moves', str(searcher.num_tested), 'states tested')
                total += searcher.num_tested
                av_moves += soln.num_moves
                solved += 1
        except KeyboardInterrupt:
            print(str(word + ':'), 'search terminated,', 'no solution', end='')
            print()
    if solved > 0:
        avg = total/solved
        print()
        print('solved', solved, 'puzzles')
        print('averages:', str(av_moves/solved), 'moves,', avg, 'states tested')
    else:
        print()
        print('solved ' + str(solved) + ' ' + 'puzzles')
    


        
    

    
    
    
