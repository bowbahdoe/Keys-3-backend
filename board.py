'''
implementation of the backend logic for the gameboard

This time the board is generic to the data type within, though
methods are still named in terms of keys

Also, the entire board is not stored, but intstead the coordinates
of pieces within as tuples of the form (x, y) along with the reference to
the data stored with it in a two dimensional list

The board width and height are also variable in order to accomodate possible
other board sizes
'''
from key import Key
from key import Team
from key import Orientation


class Board(object):
    def __init__(self, width=8, height=8):
        '''
        default constructor, sets width and height of board

        8x8 by default
        '''
        self.width  = width
        self.height = height
        self._internal_board = {} #dict of unlocked keys
        self._internal_lock_board = {} #dict of locked keys

    def is_location_in_bounds(self, location):
        '''
        checks if the location is within the bounds of the board width and height
        '''
        #we do >= instead of > to accomodate zero indexing
        if location[0] >= self.width:
            return False
        elif location[1] >= self.height:
            return False
        else:
            return True

    def set_piece_at_location(self, location, piece):
        '''
        sets the piece at a location

        raises an error if it is out of bounds
        '''
        if self.is_location_in_bounds(location):
            self._internal_board[location] = piece
        else:
            raise BufferError("location not within bounds of board")

    def get_piece_at_location(self, location):
        '''
        gets a reference to the piece at the given location

        returns None if there is no piece there
        '''
        try:
            piece = self._internal_board[location]
            return piece
        except KeyError:
            return None


    def get_locked_piece_at_location(self, location):
        '''
        gets a reference to the piece at the given location

        returns None if there is no piece there
        '''
        try:
            piece = self._internal_lock_board[location]
            return piece
        except KeyError:
            return None

    def is_piece_at_location(self, location):
        '''
        Tells if a piece is at the given location
        '''
        if self.get_piece_at_location(location) == None:
            return False
        else:
            return True

    def is_locked_piece_at_location(self, location):
        '''
        Tells if a locked piece is at the given location
        '''
        if self.get_locked_piece_at_location(location) == None:
            return False
        else:
            return True

    def is_gold_piece_at_location(self, location):
        '''
        returns False if there is no piece at the location or if
        the piece is of a different team
        '''
        piece = self.get_piece_at_location(location)

        if piece: #if it exists
            if piece.team == Team.gold:
                return True
            else:
                return False
        else:
            return False

    def is_silver_piece_at_location(self, location):
        '''
        returns False if there is no piece at the location or if
        the piece is of a different team
        '''
        piece = self.get_piece_at_location(location)

        if piece: #if it exists
            if piece.team == Team.silver:
                return True
            else:
                return False
        else:
            return False

    def remove_piece_at_location(self, location):
        '''
        removes the piece at the given location
        '''
        try:
            self._internal_board.pop(location)
        except KeyError:
            #raised if piece not at location
            raise
    def remove_locked_piece_at_location(self, location):
        '''
        removes the piece at the given location
        '''
        try:
            self._internal_lock_board.pop(location)
        except KeyError:
            #raised if piece not at location
            raise

    def lock_piece_at_location(self, location):
        '''
        Tries to lock the piece at the given location

        Fails if there is already a locked piece at the location
        '''
        try:
            locked_piece = self._internal_board[location]
            piece = self._internal_board[location]
        except:
            raise

    def move_piece_to_location(self, location_1, location_2):
        '''
        Moves a piece from one location to another

        Fails if there is no piece at location_1 or if there is a piece at
        location_2
        '''
        if self.get_piece_at_location(location_2):
            raise Exception("Key already at location_2")
        if not self.get_piece_at_location(location_1):
            raise Exception("No key at location_1")

    @classmethod
    def default_board(cls):
        '''
        alternate constructor

        creates the default board with default piece placement
        '''
        self = cls()

        piece_1 = Key(team        = Team.gold,
                      orientation = Orientation.north)

        piece_2 = Key(team        = Team.gold,
                      orientation = Orientation.north)

        piece_3 = Key(team        = Team.gold,
                      orientation = Orientation.north)

        piece_4 = Key(team        = Team.silver,
                      orientation = Orientation.south)

        piece_5 = Key(team        = Team.silver,
                      orientation = Orientation.south)

        piece_6 = Key(team        = Team.silver,
                      orientation = Orientation.south)

        pieces    = [piece_1, piece_2, piece_3, piece_4, piece_5, piece_6]
        locations = [(0,1), (0,3), (0,5), (7,2), (7,4), (7,6)]

        for piece, location in zip(pieces, locations):
            self.set_piece_at_location(location, piece)

        return self
