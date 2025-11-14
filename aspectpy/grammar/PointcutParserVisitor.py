# Generated from aspectpy/grammar/PointcutParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PointcutParser import PointcutParser
else:
    from PointcutParser import PointcutParser

# This class defines a complete generic visitor for a parse tree produced by PointcutParser.

class PointcutParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PointcutParser#start.
    def visitStart(self, ctx:PointcutParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PointcutParser#pointcutExpr.
    def visitPointcutExpr(self, ctx:PointcutParser.PointcutExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PointcutParser#designator.
    def visitDesignator(self, ctx:PointcutParser.DesignatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PointcutParser#modulePattern.
    def visitModulePattern(self, ctx:PointcutParser.ModulePatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PointcutParser#moduleSegment.
    def visitModuleSegment(self, ctx:PointcutParser.ModuleSegmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PointcutParser#functionPattern.
    def visitFunctionPattern(self, ctx:PointcutParser.FunctionPatternContext):
        return self.visitChildren(ctx)



del PointcutParser