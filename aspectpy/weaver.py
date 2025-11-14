# aspectpy/weaver.py
# Applies aspects to modules at runtime

import inspect
import importlib
from aspectpy.joinpoint import JoinPoint
from aspectpy.matcher import matches_pointcut

# Global registry of (pointcut, advice)
ASPECTS = []


def register_aspect(pointcut, advice):
    """Registers a (pointcut, advice) pair globally."""
    ASPECTS.append((pointcut, advice))


def weave_all():
    """Weave all modules referenced in the pointcuts."""
    for pointcut, advice in ASPECTS:
        module_name = ".".join(pointcut.spec.module_segments)
        module = importlib.import_module(module_name)
        weave_module(module)


def weave_module(module):
    """Apply weaving to all functions of a module."""
    for name, obj in inspect.getmembers(module, inspect.isfunction):
        for pointcut, advice in ASPECTS:
            if matches_pointcut(pointcut.spec, obj):
                wrapped = make_wrapper(obj, advice)
                setattr(module, name, wrapped)


def make_wrapper(func, advice):
    """Wrap a function with the advice and return the wrapper."""

    def wrapper(*args, **kwargs):
        jp = JoinPoint(func, args, kwargs)
        return advice(jp)

    return wrapper
