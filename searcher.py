#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Yasemin Nurluoglu
# email: yaseminn@bu.edu
#
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    def __init__(self, depth_limit):
        """constructs a new Searcher object by initializing the following 
        attributes: the Searcher‘s list of untested state, num_tested that will 
        keep track of how many states the Searcher tests; it should be 
        initialized to 0, depth_limit that specifies how deep in the 
        state-space search tree the Searcher will go."""
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit
        

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s

    def add_state(self, new_state):
        """takes a single State object called new_state and adds it to the 
        Searcher‘s list of untested states. """
        self.states += [new_state]
        
        
    def should_add(self, state):
        """ takes a State object called state and returns True if the called 
        Searcher should add state to its list of untested states, and False 
        otherwise."""
        if self.depth_limit != -1 and self.depth_limit < state.num_moves:
            return False
        elif state.creates_cycle() == True:
            return False
        else:
            return True
        
        
    def add_states(self, new_states):
        """ takes a list State objects called new_states, and that processes 
        the elements of new_states one at a time as follows:"""
        for new_s in new_states:
            if self.should_add(new_s) == True:
                self.add_state(new_s) 
        
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
            """
        s = random.choice(self.states)
        self.states.remove(s)
        return s

    def find_solution(self, init_state):
        """performs a full state-space search that begins at the specified 
        initial state init_state and ends when the goal state is found or when 
        the Searcher runs out of untested states."""
        self.add_state(init_state)
        while self.states != []:
            s = self.next_state()
            self.num_tested += 1
            if s.is_goal() == True:
                return s
            else:
                self.add_states(s.generate_successors())
        return None
    
class BFSearcher(Searcher):
    
    def next_state(self):
        """ choosing the state that has been in the list the longest 
        for untested states."""
        s = self.states[0]
        self.states.remove(s)
        return s
    
class DFSearcher(Searcher):
    
    def next_state(self):
        """ choosing the state that has been in the list the shortest 
        for untested states."""
        s = self.states[-1]
        self.states.remove(s)
        return s

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0


class GreedySearcher(Searcher):
    
    def next_state(self):
        """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
        """
    def  __init__(self, heuristic):
        """constructs a new GreedySearcher object."""
        super().__init__(-1)
        self.heuristic = heuristic
        
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)
        

    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s

    def add_state(self, state): 
        """Rather than simply adding the specified state to the list of untested 
        states, the method should add a sublist that is a [priority, state] pair, 
        where priority is the priority of state that is determined by calling 
        the priority method. Pairing each state with its priority will allow a 
        GreedySearcher to choose its next state based on the priorities of the 
        states."""
        self.states += [[self.priority(state), state]]
        
    def next_state(self):
        """Chooses the states with the highest priority."""
        next_move = max(self.states)
        self.states.remove(next_move)
        return next_move[-1]

def h1(state):
    """returns an estimate of how many additional moves are needed 
    to get from state to the goal state."""
    return state.board.num_misplaced()
    
                
                
class AStarSearcher(GreedySearcher):
    
    def  __init__(self, heuristic):
        """Initialises the class AStarSearcher"""
        super().__init__(-1)
        self.heuristic = heuristic
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * (self.heuristic(state) + state.num_moves)
    
def h2(state):
    """This heuristic function calculates the distance between the current 
    place of the tile and the goal place for the tile. For this it sums up the 
    number of rows and columns it is from goal state, and adds up the result 
    for each tile. (Not accounting for empty space)"""
    return state.board.total_distance()


    
        





                