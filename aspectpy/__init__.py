# aspectpy/__init__.py
# AspectPy - A simple aspect-oriented programming library for Python
# Developed by Fernando Pinto <fpinto@inf.puc-rio.br>
# version 0.1.0

from .pointcut import pointcut   # this is the FUNCTION
from .aspect import aspect
from .joinpoint import JoinPoint
from .weaver import weave_all

__all__ = [
    "pointcut",
    "aspect",
    "JoinPoint",
    "weave_all",
]
