# aspectpy/joinpoint.py
# Represents a join point interception in aspect-oriented programming.

class JoinPoint:
    def __init__(self, func, args, kwargs, target):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.target = target  # função real

    @property
    def func_name(self):
        return self.func.__name__

    def proceed(self):
        return self.target(*self.args, **self.kwargs)
