'''
contains the logic for the Key object
'''
import enum

class Orientation(enum.Enum):
    '''
    enum implementation of Key orientation
    '''
    north     = 0
    northeast = 1
    east      = 2
    southeast = 3
    south     = 4
    southwest = 5
    west      = 6
    northwest = 7

class Team(enum.Enum):
    '''
    enum implementation of the team
    '''
    gold = 0
    silver = 1

class Key(object):
    def __init__(self,
                 team = Team.gold,
                 orientation = Orientation.north,
                 is_locked = False):
        '''
        default constructor, sets up a new key object
        '''
        self._team = team
        self._orientation = orientation
        self._is_locked = is_locked

    def _get_is_locked(self):
        '''
        Hidden method

        returns if the key is locked
        '''
        return self.is_locked

    def _set_is_locked(self, is_locked):
        '''
        Hidden method

        sets if the key is locked

        is_locked is a bool

        raises a TypeError if a bool is not passed
        '''

        if not isinstance(is_locked, bool):
            raise TypeError("is_locked must be a bool")

        self._is_locked = is_locked

    def _get_team(self):
        '''
        Hidden method

        returns the team of the key
        '''

        return self._team

    def _set_team(self, new_team):
        '''
        Hidden method

        sets the team of the key

        raises a TypeError if a Team object is not passed
        '''

        if not isinstance(new_team, Team):
            raise TypeError("Team must be an actual team")
        else:
            self._team = new_team

    def _get_orientation(self):
        '''
        Hidden method

        returns the orientation of the key
        '''

        return self._orientation

    def _set_orientation(self, new_orientation):
        '''
        Hidden method

        sets the orientation of the key

        raises a TypeError if an Orientation object is not passed
        '''
        if not isinstance(new_orientation, Orientation):
            raise TypeError("Orientation must be an actual orientation")
        else:
            self._orientation = new_orientation

    team = property(fget = _get_team,
                    fset = _set_team)

    orientation = property(fget = _get_orientation,
                           fset = _set_orientation)

    is_locked = property(fget = _get_is_locked,
                         fset = _set_is_locked)
