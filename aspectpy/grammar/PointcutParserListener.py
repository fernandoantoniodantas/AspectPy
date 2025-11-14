# Generated from aspectpy/grammar/PointcutParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PointcutParser import PointcutParser
else:
    from PointcutParser import PointcutParser

# This class defines a complete listener for a parse tree produced by PointcutParser.
class PointcutParserListener(ParseTreeListener):

    # Enter a parse tree produced by PointcutParser#start.
    def enterStart(self, ctx:PointcutParser.StartContext):
        pass

    # Exit a parse tree produced by PointcutParser#start.
    def exitStart(self, ctx:PointcutParser.StartContext):
        pass


    # Enter a parse tree produced by PointcutParser#pointcutExpr.
    def enterPointcutExpr(self, ctx:PointcutParser.PointcutExprContext):
        pass

    # Exit a parse tree produced by PointcutParser#pointcutExpr.
    def exitPointcutExpr(self, ctx:PointcutParser.PointcutExprContext):
        pass


    # Enter a parse tree produced by PointcutParser#designator.
    def enterDesignator(self, ctx:PointcutParser.DesignatorContext):
        pass

    # Exit a parse tree produced by PointcutParser#designator.
    def exitDesignator(self, ctx:PointcutParser.DesignatorContext):
        pass


    # Enter a parse tree produced by PointcutParser#modulePattern.
    def enterModulePattern(self, ctx:PointcutParser.ModulePatternContext):
        pass

    # Exit a parse tree produced by PointcutParser#modulePattern.
    def exitModulePattern(self, ctx:PointcutParser.ModulePatternContext):
        pass


    # Enter a parse tree produced by PointcutParser#moduleSegment.
    def enterModuleSegment(self, ctx:PointcutParser.ModuleSegmentContext):
        pass

    # Exit a parse tree produced by PointcutParser#moduleSegment.
    def exitModuleSegment(self, ctx:PointcutParser.ModuleSegmentContext):
        pass


    # Enter a parse tree produced by PointcutParser#functionPattern.
    def enterFunctionPattern(self, ctx:PointcutParser.FunctionPatternContext):
        pass

    # Exit a parse tree produced by PointcutParser#functionPattern.
    def exitFunctionPattern(self, ctx:PointcutParser.FunctionPatternContext):
        pass



del PointcutParser