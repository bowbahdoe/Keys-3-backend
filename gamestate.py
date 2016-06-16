'''
This defines an object to keep track of the game

This allows us to abstract the game logic from the rendering
'''
from board import Board
from key import Team
from key import Orientation
import enum
import itertools


class States(enum.Enum):
    gold_play             = 0
    silver_play           = 1
    gold_respawning       = 2
    silver_respawning     = 3
    game_over             = 4
    gold_piece_selected   = 5
    silver_piece_selected = 6

class GameState(object):
    '''
    defines game actions and keeps track of the state of the game
    '''
    def __init__(self):
        '''
        Default constructor
        '''
        self._gameboard = Board.default_board()
        self._state = States.gold_play
        #_piece_selected is a location tuple or None
        self._piece_selected = None

    def is_a_team_respawning(self):
        '''
        returns True if a team is currently responding
        '''
        if self._state == States.gold_respawning:
            return True
        elif self._state == States.silver_respawning:
            return True
        else:
            return False

    def get_possible_moves_of_key(self, location):
        '''
        returns a list of tuples that represent the allowable moves of a key
        at the given location

        returns an empty list if there is no piece at the location
        '''
        piece = self._gameboard.get_piece_at_location(location)
        if not piece:
            return []

        possible_moves = []

        #we create a small lambda function depending on orientation of the key
        #this says how we step through the locations of the board
        if piece.orientation == Orientation.north:
            stepper_function = lambda x, y: (x, y+1)
        elif piece.orientation == Orientation.northeast:
            stepper_function = lambda x, y: (x+1, y+1)
        elif piece.orientation == Orientation.east:
            stepper_function = lambda x, y: (x+1, y)
        elif piece.orientation == Orientation.southeast:
            stepper_function = lambda x, y: (x+1, y-1)
        elif piece.orientation == Orientation.south:
            stepper_function = lambda x, y: (x, y-1)
        elif piece.orientation == Orientation.southwest:
            stepper_function = lambda x, y: (x-1, y-1)
        elif piece.orientation == Orientation.west:
            stepper_function = lambda x, y: (x-1, y)
        elif piece.orientation == Orientation.northwest:
            stepper_function = lambda x, y: (x-1, y+1)

        #uses 0 and 1 as indexes even though a location will usually
        #have attributes accessable through loc.x and loc.y
        possible_location = stepper_function(piece.location[0],
                                             piece.location[1])

        while self._gameboard.is_location_in_bounds(possible_location):
            piece_at_location = self._gameboard.get_piece_at_location(location)

            if not piece_at_location:
                possible_moves.append(possible_location)
            elif piece_at_location.team = piece.team
                break
            else:
                possible_moves.append(possible_location)
                break

            possible_location = stepper_function(possible_location[0],
                                                 possible_location[1])

        return possible_moves

    def get_rotation_points_of_key(self, location):
        '''
        returns a list of tuples that represent the allowable rotation points
        of a key at a given location

        returns an empty list of there is no piece at the location
        '''
        piece = self._gameboard.get_piece_at_location(location)

        if not piece:
            return []

        modifiers = (-1, 0, 1)
        rotation_points = []

        for x_modifier in modifiers:
            for y_modifier in modifiers:
                rotation_points.append((piece.location[0] + x_modifier,
                                        piece.location[1] + y_modifier))


        rotation_points = itertools.ifilter(self._gameboard.is_location_in_bounds,
                                            rotation_points)

        #we eliminate the possible moves from the rotation points
        #and also the piece's current location
        possible_moves = self.get_possible_moves_of_key(location)
        rotation_points = [i for i in rotation_points if i not in possible_moves]
        rotation_points.remove(location)

        return rotation_points

    def location_clicked(self, location):
        '''
        performs the proper action if a location is clicked

        Will be a large method unless I can break it better
        '''
        #If we have a team playing then we allow for selecting a piece to move
        if self._state == States.gold_play:
            if self._gameboard.is_gold_piece_at_location(location):
                self._piece_selected = location
                self._state = States.gold_piece_selected

        elif self._state == States.silver_play:
            if self.is_silver_piece_at_location(location):
                self._piece_selected = location
                self._state = States.silver_piece_selected

        #if a piece is selected already we have to handle moving
        elif self._state == States.gold_piece_selected:
            if location in self.get_possible_moves_of_key(self._piece_selected):
                if self._gameboard.is_piece_at_location(location):
                    pass
                if self._gameboard.is_locked_piece_at_location(location):
                    locked_piece = self._gameboard.get_piece_at_location(location)
                else:
                    self._gameboard.move_piece_to_location()
            else:
                self._piece_selected = None
                self._state = States.gold_play

        elif self._state == States.silver_piece_selected:
            pass
        elif self._state == States.gold_respawning:
            pass
        elif self._state == States.silver_respawning:
            pass
