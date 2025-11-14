# aspectpy/aspect.py
# Define aspects for aspect-oriented programming.

from .weaver import register_aspect

def aspect(pointcut_obj):

    """
    Decorator de aspect com advice 'around'.
    """
    def decorator(advice_func):
        register_aspect(pointcut_obj, advice_func)
        return advice_func
    return decorator
