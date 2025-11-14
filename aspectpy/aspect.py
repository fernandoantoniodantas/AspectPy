# aspectpy/aspect.py
# Define aspects for aspect-oriented programming.

from .weaver import register_aspect

def aspect(pointcut_obj):

    """
    Decorator of aspect with 'around' advice.
    """
    def decorator(advice_func):
        register_aspect(pointcut_obj, advice_func)
        return advice_func
    return decorator
