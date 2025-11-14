# aspectpy/parser.py
# Pointcut DSL parser powered by ANTLR4

from antlr4 import InputStream, CommonTokenStream, ParseTreeVisitor
from aspectpy.grammar.PointcutLexer import PointcutLexer
from aspectpy.grammar.PointcutParser import PointcutParser

# ---------------------------------------------------------------------
# PointcutSpec structure
# ---------------------------------------------------------------------
class PointcutSpec:
    """Data structure representing a parsed pointcut."""

    def __init__(self, kind, module_segments, function_pattern):
        self.kind = kind
        self.module_segments = module_segments
        self.function_pattern = function_pattern

    def __repr__(self):
        return (
            f"PointcutSpec(kind={self.kind}, "
            f"module={self.module_segments}, "
            f"function={self.function_pattern})"
        )


# ---------------------------------------------------------------------
# Visitor implementation for grammar
# ---------------------------------------------------------------------
class PointcutVisitor(ParseTreeVisitor):
    """Visits the parse tree and constructs a PointcutSpec."""

    def visitStart(self, ctx):
        return self.visit(ctx.pointcutExpr())

    def visitPointcutExpr(self, ctx):
        # 1. Designator
        kind = ctx.designator().getText()

        # 2. Module pattern
        mp = ctx.modulePattern()
        module_segments = []

        # IDENT() returns a single TerminalNode
        first_ident = mp.IDENT().getText()
        module_segments.append(first_ident)

        # moduleSegment() returns a list
        for seg in mp.moduleSegment():
            module_segments.append(seg.getText())

        # 3. Function pattern
        if ctx.functionPattern():
            func = ctx.functionPattern().getText()
        else:
            func = None

        return PointcutSpec(kind, module_segments, func)


# ---------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------
def parse_pointcut(expr: str) -> PointcutSpec:
    """Parse a pointcut DSL expression and return a PointcutSpec."""

    input_stream = InputStream(expr)
    lexer = PointcutLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = PointcutParser(tokens)

    tree = parser.start()
    visitor = PointcutVisitor()
    return visitor.visit(tree)
