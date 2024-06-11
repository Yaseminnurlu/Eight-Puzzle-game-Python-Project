#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Yasemin Nurluoglu
# email: yaseminn@bu.edu
#
# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        n = 0
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                self.tiles[row][col] = digitstr[n]
                n += 1
                if self.tiles[row][col] == '0':
                    self.blank_r = row
                    self.blank_c = col
                

    
    def __repr__(self):
        """returns a string representation of a Board object."""
        s = ''
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                if self.tiles[row][col] == '0':
                    if (col)%3 != 0:
                        s += '_ ' 
                    elif (col)%3 == 0:
                        if self.tiles[0][0] == 0:
                            s += '_ ' 
                        elif self.tiles[0][0] != 0:
                            s += '\n'
                            s += '_ ' 
                else:
                    if (col) % 3 != 0:
                        s += str(self.tiles[row][col]) 
                        s += ' '
                    elif (col)%3 == 0:
                        if self.tiles[row][col] != self.tiles[0][0]:
                            s += '\n' + str(self.tiles[row][col])
                            s += ' '   
                        elif self.tiles[row][col] == self.tiles[0][0]:
                            s += str(self.tiles[row][col])
                            s += ' '   
        s += '\n'
        return s
    
    
    def move_blank(self, direction):
        """takes as input a string direction that specifies the direction
        in which the blank should move, and that attempts to modify the
        contents of the called Board object accordingly. The method should 
        return True or False to indicate whether the requested move was 
        possible."""
        new_r = self.blank_r 
        new_c = self.blank_c
        if direction != 'up' and direction != 'down' and \
            direction != 'left' and direction != 'right':
                return False
            
        else:
            if direction == 'up':
                new_r = (self.blank_r - 1)
            elif direction == 'down':
                new_r = (self.blank_r + 1)
            elif direction == 'left':
                new_c = (self.blank_c -1) 
            elif direction == 'right':
                new_c = (self.blank_c +1) 
        if new_r not in range(0, 3): 
            return False
        elif new_c not in range(0,3):
            return False
        else: 
           self.tiles[self.blank_r][self.blank_c]= self.tiles[new_r][new_c]
           self.tiles[new_r][new_c] = '0'
           self.blank_r = new_r
           self.blank_c = new_c
           return True
     
    def digit_string(self): 
        """returns a string of digits that corresponds to the current 
        contents of the called Board object’s tiles attribute."""
        digit_str = ''
        for r in range(3):
            for c in range(3):
                digit_str += str(self.tiles[r][c])
        return digit_str
                
    def copy(self):
        """returns a newly-constructed Board object 
        that is a deep copy of the called object."""
        copy_str = self.digit_string()
        b_copy = Board(copy_str)
        return b_copy 
    
    def num_misplaced(self):
        """ counts and returns the number of tiles in the called Board 
        object that are not where they should be in the goal state."""
        misplaced = 0 
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '0':
                    misplaced = misplaced
                elif GOAL_TILES[r][c] != self.tiles[r][c]:
                    misplaced += 1
        return misplaced 
        
    def  __eq__(self, other):
        """Returns True if the called object (self) and the argument (other)
        have the same values for the tiles attribute, and False otherwise."""
        if self.tiles == other.tiles:
            return True
        else:
            return False 

        
    def total_distance(self): 
        """calculates the distance between the current place of the tile and 
        the goal place for the tile. For this it sums up the number of rows and 
        columns it is from goal state, and adds up the result for each tile. 
        (Not accounting for empty space)"""
        goal_tiles = '012345678'
        s = self.digit_string()
        first = s[0]
        count = 0
        new_r = 0
        new_c = 0
        goal_r = 0
        goal_c = 0
        for x in range(9):
            for y in range(9):
                if s[x] == goal_tiles[y]:
                    if s[x] != '0' or goal_tiles[y] != '0':
                        new_r = x // 3
                        new_c = x % 3
                        goal_r = y // 3
                        goal_c = y % 3
                        count += abs(new_r - goal_r)
                        count += abs(new_c - goal_c)
        return count