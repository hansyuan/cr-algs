from enum import Enum

class Status(Enum):
    """ For ambulances """
    IDLE = 1
    ACTIVE = 2

class DataSource(Enum):
    """ There are at least three sources of events for the simulation. """
    RANDOM = 1