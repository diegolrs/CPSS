from enum import Enum

class TokenClassf(Enum):
    INVALID = -1
    IDENTIFIER = 0
    CLASS =  1
    INCLUDE = 2
    PARENTESIS = 3
    BRACES = 4
    GETSET = 5