# aspectpy/pointcut.py
# Defines pointcuts for the AspectPy framework.

from .parser import parse_pointcut

class Pointcut:
    def __init__(self, expression, func, spec):
        """
        Represents a declarative pointcut.
        
        Parameters:
            expression (str): The original DSL expression (e.g., "execution: app.* -> foo_*")
            func (callable): The annotated function (ignored at runtime, used only as a symbolic anchor)
            spec (PointcutSpec): The parsed structure produced by the ANTLR-based parser
        """
        self.expression = expression
        self.func = func
        self.spec = spec

    def __repr__(self):
        return f"<Pointcut {self.expression} spec={self.spec}>"

def pointcut(expr: str):
    """
    Decorator that registers a declarative pointcut.
    
    This function:
      1) Parses the DSL expression using ANTLR
      2) Generates a PointcutSpec object
      3) Wraps everything inside a Pointcut instance
    """
    def decorator(func):
        spec = parse_pointcut(expr)         # Parse DSL expression using ANTLR
        pc = Pointcut(expr, func, spec)     # Store the parsed pointcut
        func.__pointcut__ = pc              # Attach metadata to the function
        return pc
    return decorator
