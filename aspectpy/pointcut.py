# aspectpy/pointcut.py
# Define pointcuts for aspect-oriented programming.

class Pointcut:
    def __init__(self, expression, func):
        self.expression = expression
        self.func = func  # função nomeada, mas o corpo é ignorado

    def __repr__(self):
        return f"<Pointcut {self.expression}>"

def pointcut(expr: str):
    """
    Decorator that registers a declarative pointcut.
    """
    def decorator(func):
        pc = Pointcut(expr, func)
        func.__pointcut__ = pc
        return pc
    return decorator
