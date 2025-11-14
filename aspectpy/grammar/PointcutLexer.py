# Generated from aspectpy/grammar/PointcutLexer.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,9,60,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,6,1,
        6,1,7,1,7,5,7,49,8,7,10,7,12,7,52,9,7,1,8,4,8,55,8,8,11,8,12,8,56,
        1,8,1,8,0,0,9,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,1,0,3,3,0,
        65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,3,0,9,10,13,13,32,
        32,61,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,
        0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,1,19,1,0,0,
        0,3,29,1,0,0,0,5,34,1,0,0,0,7,36,1,0,0,0,9,39,1,0,0,0,11,41,1,0,
        0,0,13,44,1,0,0,0,15,46,1,0,0,0,17,54,1,0,0,0,19,20,5,101,0,0,20,
        21,5,120,0,0,21,22,5,101,0,0,22,23,5,99,0,0,23,24,5,117,0,0,24,25,
        5,116,0,0,25,26,5,105,0,0,26,27,5,111,0,0,27,28,5,110,0,0,28,2,1,
        0,0,0,29,30,5,99,0,0,30,31,5,97,0,0,31,32,5,108,0,0,32,33,5,108,
        0,0,33,4,1,0,0,0,34,35,5,58,0,0,35,6,1,0,0,0,36,37,5,45,0,0,37,38,
        5,62,0,0,38,8,1,0,0,0,39,40,5,46,0,0,40,10,1,0,0,0,41,42,5,42,0,
        0,42,43,5,42,0,0,43,12,1,0,0,0,44,45,5,42,0,0,45,14,1,0,0,0,46,50,
        7,0,0,0,47,49,7,1,0,0,48,47,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,
        50,51,1,0,0,0,51,16,1,0,0,0,52,50,1,0,0,0,53,55,7,2,0,0,54,53,1,
        0,0,0,55,56,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,58,1,0,0,0,58,
        59,6,8,0,0,59,18,1,0,0,0,3,0,50,56,1,6,0,0
    ]

class PointcutLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    EXECUTION = 1
    CALL = 2
    COLON = 3
    ARROW = 4
    DOT = 5
    STARSTAR = 6
    STAR = 7
    IDENT = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'execution'", "'call'", "':'", "'->'", "'.'", "'**'", "'*'" ]

    symbolicNames = [ "<INVALID>",
            "EXECUTION", "CALL", "COLON", "ARROW", "DOT", "STARSTAR", "STAR", 
            "IDENT", "WS" ]

    ruleNames = [ "EXECUTION", "CALL", "COLON", "ARROW", "DOT", "STARSTAR", 
                  "STAR", "IDENT", "WS" ]

    grammarFileName = "PointcutLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


