# Generated from aspectpy/grammar/PointcutParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,9,42,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,3,1,21,8,1,1,2,1,2,1,3,1,3,1,3,5,3,28,8,
        3,10,3,12,3,31,9,3,1,4,1,4,1,5,1,5,1,5,3,5,38,8,5,3,5,40,8,5,1,5,
        0,0,6,0,2,4,6,8,10,0,2,1,0,1,2,1,0,6,8,39,0,12,1,0,0,0,2,15,1,0,
        0,0,4,22,1,0,0,0,6,24,1,0,0,0,8,32,1,0,0,0,10,39,1,0,0,0,12,13,3,
        2,1,0,13,14,5,0,0,1,14,1,1,0,0,0,15,16,3,4,2,0,16,17,5,3,0,0,17,
        20,3,6,3,0,18,19,5,4,0,0,19,21,3,10,5,0,20,18,1,0,0,0,20,21,1,0,
        0,0,21,3,1,0,0,0,22,23,7,0,0,0,23,5,1,0,0,0,24,29,5,8,0,0,25,26,
        5,5,0,0,26,28,3,8,4,0,27,25,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,
        29,30,1,0,0,0,30,7,1,0,0,0,31,29,1,0,0,0,32,33,7,1,0,0,33,9,1,0,
        0,0,34,40,5,7,0,0,35,37,5,8,0,0,36,38,5,7,0,0,37,36,1,0,0,0,37,38,
        1,0,0,0,38,40,1,0,0,0,39,34,1,0,0,0,39,35,1,0,0,0,40,11,1,0,0,0,
        4,20,29,37,39
    ]

class PointcutParser ( Parser ):

    grammarFileName = "PointcutParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'execution'", "'call'", "':'", "'->'", 
                     "'.'", "'**'", "'*'" ]

    symbolicNames = [ "<INVALID>", "EXECUTION", "CALL", "COLON", "ARROW", 
                      "DOT", "STARSTAR", "STAR", "IDENT", "WS" ]

    RULE_start = 0
    RULE_pointcutExpr = 1
    RULE_designator = 2
    RULE_modulePattern = 3
    RULE_moduleSegment = 4
    RULE_functionPattern = 5

    ruleNames =  [ "start", "pointcutExpr", "designator", "modulePattern", 
                   "moduleSegment", "functionPattern" ]

    EOF = Token.EOF
    EXECUTION=1
    CALL=2
    COLON=3
    ARROW=4
    DOT=5
    STARSTAR=6
    STAR=7
    IDENT=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pointcutExpr(self):
            return self.getTypedRuleContext(PointcutParser.PointcutExprContext,0)


        def EOF(self):
            return self.getToken(PointcutParser.EOF, 0)

        def getRuleIndex(self):
            return PointcutParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = PointcutParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.pointcutExpr()
            self.state = 13
            self.match(PointcutParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointcutExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def designator(self):
            return self.getTypedRuleContext(PointcutParser.DesignatorContext,0)


        def COLON(self):
            return self.getToken(PointcutParser.COLON, 0)

        def modulePattern(self):
            return self.getTypedRuleContext(PointcutParser.ModulePatternContext,0)


        def ARROW(self):
            return self.getToken(PointcutParser.ARROW, 0)

        def functionPattern(self):
            return self.getTypedRuleContext(PointcutParser.FunctionPatternContext,0)


        def getRuleIndex(self):
            return PointcutParser.RULE_pointcutExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointcutExpr" ):
                listener.enterPointcutExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointcutExpr" ):
                listener.exitPointcutExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPointcutExpr" ):
                return visitor.visitPointcutExpr(self)
            else:
                return visitor.visitChildren(self)




    def pointcutExpr(self):

        localctx = PointcutParser.PointcutExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_pointcutExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.designator()
            self.state = 16
            self.match(PointcutParser.COLON)
            self.state = 17
            self.modulePattern()
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 18
                self.match(PointcutParser.ARROW)
                self.state = 19
                self.functionPattern()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DesignatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXECUTION(self):
            return self.getToken(PointcutParser.EXECUTION, 0)

        def CALL(self):
            return self.getToken(PointcutParser.CALL, 0)

        def getRuleIndex(self):
            return PointcutParser.RULE_designator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDesignator" ):
                listener.enterDesignator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDesignator" ):
                listener.exitDesignator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDesignator" ):
                return visitor.visitDesignator(self)
            else:
                return visitor.visitChildren(self)




    def designator(self):

        localctx = PointcutParser.DesignatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_designator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModulePatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(PointcutParser.IDENT, 0)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(PointcutParser.DOT)
            else:
                return self.getToken(PointcutParser.DOT, i)

        def moduleSegment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PointcutParser.ModuleSegmentContext)
            else:
                return self.getTypedRuleContext(PointcutParser.ModuleSegmentContext,i)


        def getRuleIndex(self):
            return PointcutParser.RULE_modulePattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModulePattern" ):
                listener.enterModulePattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModulePattern" ):
                listener.exitModulePattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModulePattern" ):
                return visitor.visitModulePattern(self)
            else:
                return visitor.visitChildren(self)




    def modulePattern(self):

        localctx = PointcutParser.ModulePatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_modulePattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(PointcutParser.IDENT)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 25
                self.match(PointcutParser.DOT)
                self.state = 26
                self.moduleSegment()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModuleSegmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(PointcutParser.IDENT, 0)

        def STAR(self):
            return self.getToken(PointcutParser.STAR, 0)

        def STARSTAR(self):
            return self.getToken(PointcutParser.STARSTAR, 0)

        def getRuleIndex(self):
            return PointcutParser.RULE_moduleSegment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModuleSegment" ):
                listener.enterModuleSegment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModuleSegment" ):
                listener.exitModuleSegment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModuleSegment" ):
                return visitor.visitModuleSegment(self)
            else:
                return visitor.visitChildren(self)




    def moduleSegment(self):

        localctx = PointcutParser.ModuleSegmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_moduleSegment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionPatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(PointcutParser.STAR, 0)

        def IDENT(self):
            return self.getToken(PointcutParser.IDENT, 0)

        def getRuleIndex(self):
            return PointcutParser.RULE_functionPattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionPattern" ):
                listener.enterFunctionPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionPattern" ):
                listener.exitFunctionPattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionPattern" ):
                return visitor.visitFunctionPattern(self)
            else:
                return visitor.visitChildren(self)




    def functionPattern(self):

        localctx = PointcutParser.FunctionPatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functionPattern)
        self._la = 0 # Token type
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(PointcutParser.STAR)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(PointcutParser.IDENT)
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 36
                    self.match(PointcutParser.STAR)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





