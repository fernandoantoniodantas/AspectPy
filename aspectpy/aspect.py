# aspectpy/aspect.py
# Defines the @aspect decorator and registers advice into the global weaver.

from .weaver import register_aspect


def aspect(pointcut):
    """
    Decorator that associates an advice function with a pointcut.

    Usage:
        @aspect(my_pointcut)
        def advice(join_point):
            ...
    """
    def decorator(advice_func):
        # Register (pointcut, advice_func) with the global weaving engine
        register_aspect(pointcut, advice_func)
        return advice_func

    return decorator
